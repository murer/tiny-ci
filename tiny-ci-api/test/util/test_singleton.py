from unittest import TestCase
from tinyciapi.util.singleton import SingletonMixin
import unittest

class A1(SingletonMixin):
    """ singleton """

class A2(SingletonMixin):
    """ singleton """

class CodecTestCase(TestCase):

    def test_singleton(self):
        self.assertEqual(A1.me(), A1.me())
        self.assertNotEqual(A1(), A1.me())

        self.assertEqual(A2.me(), A2.me())
        self.assertNotEqual(A2(), A2.me())

        self.assertNotEqual(A1.me(), A2.me())

if __name__ == '__main__':
        unittest.main()
