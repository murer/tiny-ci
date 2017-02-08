import unittest
import supertest
import httplib
from google.appengine.ext import ndb

class OneTestCase(supertest.TestCase):

    def test_one(self):
        class TestModel(ndb.Model):
            pass
        user_key = ndb.Key('User', 'ryan')
        ndb.put_multi([TestModel(parent=user_key), TestModel(parent=user_key)])
        self.assertEqual(0, TestModel.query().count(3))
        self.assertEqual(2, TestModel.query(ancestor=user_key).count(3))

    def test_one_twice(self):
        self.test_one()

    def test_web(self):
        """self.assertEqual('pong', testcase.http_json('GET', '/s/ping')[0])"""

    def test_web_twice(self):
        self.test_web()

if __name__ == '__main__':
        unittest.main()
