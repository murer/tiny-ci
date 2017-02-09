from tinyciapi.util.singleton import SingletonMixin
from tinyciapi.util.cryptutil import Crypt as _Crypt
from tinyciapi.util import codecutil
from ent import Secret

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
