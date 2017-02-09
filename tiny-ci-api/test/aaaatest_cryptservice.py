import unittest
from tinyciapi.service.cryptservice import crypt
from supertest import TestCase

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

if __name__ == '__main__':
        unittest.main()
