import unittest
from tinyciapi.util.cryptutil import AES
from supertest import TestCase

class CodecTestCase(TestCase):

    def assertCrypt(self, crypt, plain):
        code = crypt.enc(plain)
        self.assertEqual(plain, crypt.dec(code))
        created = crypt.__class__()
        code = created.enc(plain)
        self.assertEqual(plain, created.dec(code))

    def test_AES(self):
        crypt = AES('abcdefghijklmnopqrstuvwxyz012345')
        self.assertCrypt(crypt, '')
        self.assertCrypt(crypt, 'A')
        self.assertCrypt(crypt, 'test')


if __name__ == '__main__':
        unittest.main()
