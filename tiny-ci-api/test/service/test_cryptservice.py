import unittest
from test.supertest import TestCase
from tinyciapi.service.cryptservice import crypt
from tinyciapi.util.jsonutil import JSON

class SampleToken(object):

    def __init__(self):
        self.name = None
        self.value = None

    def enc(self):
        return JSON.stringify(self.__dict__)

class CryptTestCase(TestCase):

    def assertOneCrypt(self, crypt, plain):
        code1 = crypt.enc(plain)
        self.assertEqual(plain, crypt.dec(code1))
        code2 = crypt.enc(plain)
        self.assertEqual(plain, crypt.dec(code2))
        self.assertNotEqual(code1, code2)

    def assertCrypt(self, plain):
        self.assertOneCrypt(crypt(), plain)
        self.assertOneCrypt(crypt(), plain)
        self.assertOneCrypt(crypt(), plain)

    def test_crypt(self):
        self.assertCrypt('')
        self.assertCrypt('A')
        self.assertCrypt('test')
        self.assertCrypt('\x00\x00\x00')

    def test_token(self):
        token = SampleToken()
        token.name = 'test'
        token.value = 'any'
        print 'code', token.enc()

if __name__ == '__main__':
        unittest.main()
