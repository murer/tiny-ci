from supertest import TestCase
from supertest import R
from google.appengine.ext import ndb

class OneTestCase(TestCase):

    def test_web(self):
        resp = R('POST', '/api/github/computeurl').execute()
        self.assertEqual('application/json; charset=utf-8', resp.headers['content-type'])
        self.assertEqual('OK', resp.body_json())

if __name__ == '__main__':
        unittest.main()
