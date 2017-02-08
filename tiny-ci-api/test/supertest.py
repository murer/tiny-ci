import unittest
import httplib
import json as JSON
from gaeserver import GaeTestServer
from tinyciapi.httputil import Request as HTTP

class Error(Exception):
    """ Error """

gae = GaeTestServer()

class TestCase(unittest.TestCase):

    def setUp(self):
        from tinyciapi import main
        gae.boot_gae()
        gae.boot_web(8080, main.app)
        gae.server_forever_background()

    def tearDown(self):
        gae.shutdown()

class R(HTTP):

    def __init__(self, *args, **kwargs):
        super(R, self).__init__(*args, **kwargs)
        self._url = 'http://localhost:%s%s' % (gae.port, self._url)
