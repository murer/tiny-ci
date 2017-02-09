from supertest import TestCase
from supertest import R
from google.appengine.ext import ndb

class OneTestCase(TestCase):

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
        resp = R('GET', '/api/ping').execute()
        self.assertEqual('application/json; charset=utf-8', resp.headers['content-type'])
        self.assertEqual('OK', resp.body_json())

    def test_web_twice(self):
        self.test_web()

if __name__ == '__main__':
        unittest.main()
