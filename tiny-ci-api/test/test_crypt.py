import unittest
from tinyciapi.util.cryptutil import AES
from tinyciapi.util.cryptutil import Crypt
from supertest import TestCase

class CodecTestCase(TestCase):

    def assertOneCrypt(self, crypt, plain):
        code = crypt.enc(plain)
        self.assertEqual(plain, crypt.dec(code))

    def assertCrypt(self, plain):
        self.assertOneCrypt(AES('abcdefghijklmnopqrstuvwxyz012345'), plain)
        self.assertOneCrypt(AES(), plain)
        self.assertOneCrypt(Crypt('abcdefghijklmnopqrstuvwxyz012345'), plain)
        self.assertOneCrypt(Crypt(), plain)

    def test_AES(self):
        self.assertCrypt('')
        self.assertCrypt('A')
        self.assertCrypt('test')
        self.assertCrypt('\x00\x00\x00')

if __name__ == '__main__':
        unittest.main()
