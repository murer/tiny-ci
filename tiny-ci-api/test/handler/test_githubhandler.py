from test.supertest import TestCase
from test.supertest import R
from google.appengine.ext import ndb
import unittest
from tinyciapi.handler import githubhandler

class OneTestCase(TestCase):

    def test_web(self):
        token = githubhandler.GithubToken()
        token.gh = 'any'
        resp = R('POST', '/api/github/computeurl').send_json({
            'token': token.enc(),
            'project': 'murer/tiny-ci'
        }).execute()
        self.assertEqual('application/json; charset=utf-8', resp.headers['content-type'])
        obj = resp.body_json()
        token = githubhandler.GithubProjectToken.dec(obj['code'])
        self.assertEqual('murer/tiny-ci', token.prj)
        self.assertTrue(token.gh)
        self.assertTrue(obj['url'])

if __name__ == '__main__':
        unittest.main()
