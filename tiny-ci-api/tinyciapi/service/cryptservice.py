from tinyciapi.util.singleton import SingletonMixin
from tinyciapi.util.cryptutil import Crypt as _Crypt
from tinyciapi.util import codecutil
from tinyciapi.util.jsonutil import JSON
from ent import Secret

class Error(Exception):
    """Exceptions"""

class Crypt(_Crypt, SingletonMixin):

    def __init__(self):
        secret = Secret.get_by_id('master')
        if not secret:
            key = codecutil.enc(_Crypt().key)
            secret = Secret(
                id = 'master',
                secret = key
            )
            secret.put()
        key = codecutil.dec(str(secret.secret))
        super(Crypt, self).__init__(key)

def crypt():
    return Crypt.me()


class TokenMixin(object):

    @classmethod
    def dec(cls, code):
        code = codecutil.dec(code)
        code = crypt().dec(code)
        name, code = code.split('.')
        name += 'Token'
        if name != cls.__name__:
            raise Error('wrong class, expected: %s, but was: %s' % (cls.__name__, name))
        code = JSON.parse(code)
        ret = cls()
        ret.__dict__.update(code)
        return ret

    def enc(self):
        name = self.__class__.__name__
        if not name.endswith('Token'):
            raise Error('Token class must end with Token, but was: %s' % (name))
        name = name[:-5]
        ret = '%s.%s' % (name, JSON.stringify(self.__dict__))
        ret = crypt().enc(ret)
        ret = codecutil.enc(ret)
        return ret
