import unittest
from test.supertest import TestCase
from tinyciapi.service.cryptservice import crypt
from tinyciapi.service.cryptservice import SampleToken
from tinyciapi.util import codecutil

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
        code = token.enc()
        self.assertNotEqual(code, token.enc())
        parsed = SampleToken.dec(code)
        self.assertEqual('test', parsed.name)
        self.assertEqual('any', parsed.value)
        self.assertNotEqual(token, parsed)

if __name__ == '__main__':
        unittest.main()
