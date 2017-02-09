from unittest import TestCase
from tinyciapi.util.cryptutil import AES
from tinyciapi.util.cryptutil import Crypt

class CryptTestCase(TestCase):

    def assertOneCrypt(self, crypt, plain):
        code1 = crypt.enc(plain)
        self.assertEqual(plain, crypt.dec(code1))
        code2 = crypt.enc(plain)
        self.assertEqual(plain, crypt.dec(code2))
        self.assertNotEqual(code1, code2)

    def assertCrypt(self, plain):
        self.assertOneCrypt(AES('abcdefghijklmnopqrstuvwxyz012345'), plain)
        self.assertOneCrypt(AES(), plain)
        self.assertOneCrypt(Crypt('abcdefghijklmnopqrstuvwxyz012345'), plain)
        self.assertOneCrypt(Crypt(), plain)

    def test_crypt(self):
        self.assertCrypt('')
        self.assertCrypt('A')
        self.assertCrypt('test')
        self.assertCrypt('\x00\x00\x00')

if __name__ == '__main__':
        unittest.main()
