import unittest
from tinyciapi.util import codecutil as codec
from supertest import TestCase

class CodecTestCase(TestCase):

    def assertB64(self, plain, code):
        self.assertEqual(code, codec.b64enc(plain))
        self.assertEqual(plain, codec.b64dec(code))

    def assertUB64(self, plain, code):
        self.assertEqual(code, codec.ub64enc(plain))
        self.assertEqual(plain, codec.ub64dec(code))
        self.assertEqual(code, codec.enc(plain))
        self.assertEqual(plain, codec.dec(code))

    def test_b64(self):
        self.assertB64('\x00\x00\x00', 'AAAA')
        self.assertB64('\x00\x00', 'AAA=')
        self.assertB64('\x00', 'AA==')
        self.assertB64('\x00\x00\x00\x00\x00\x00', 'AAAAAAAA')
        self.assertB64('\x00\x00\x00\x00\x00', 'AAAAAAA=')
        self.assertB64('\x00\x00\x00\x00', 'AAAAAA==')
        self.assertB64('test', 'dGVzdA==')
        self.assertB64('a', 'YQ==')
        self.assertB64('\x03\xF0\x7E', 'A/B+')
        self.assertB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45\xD2\x7D\x00', 'Tq5PFtu1e+hW7n0/7vBzNMpF0n0A')
        self.assertB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45\xD2\x7D', 'Tq5PFtu1e+hW7n0/7vBzNMpF0n0=')
        self.assertB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45\xD2', 'Tq5PFtu1e+hW7n0/7vBzNMpF0g==')
        self.assertB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45', 'Tq5PFtu1e+hW7n0/7vBzNMpF')
        self.assertB64('', '')

    def test_ub64(self):
        self.assertUB64('\x00\x00\x00', 'AAAA')
        self.assertUB64('\x00\x00', 'AAA')
        self.assertUB64('\x00', 'AA')
        self.assertUB64('\x00\x00\x00\x00\x00\x00', 'AAAAAAAA')
        self.assertUB64('\x00\x00\x00\x00\x00', 'AAAAAAA')
        self.assertUB64('\x00\x00\x00\x00', 'AAAAAA')
        self.assertUB64('test', 'dGVzdA')
        self.assertUB64('a', 'YQ')
        self.assertUB64('\x03\xF0\x7E', 'A_B-')
        self.assertUB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45\xD2\x7D\x00', 'Tq5PFtu1e-hW7n0_7vBzNMpF0n0A')
        self.assertUB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45\xD2\x7D', 'Tq5PFtu1e-hW7n0_7vBzNMpF0n0')
        self.assertUB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45\xD2', 'Tq5PFtu1e-hW7n0_7vBzNMpF0g')
        self.assertUB64('\x4E\xAE\x4F\x16\xDB\xB5\x7B\xE8\x56\xEE\x7D\x3F\xEE\xF0\x73\x34\xCA\x45', 'Tq5PFtu1e-hW7n0_7vBzNMpF')
        self.assertUB64('', '')

if __name__ == '__main__':
        unittest.main()
