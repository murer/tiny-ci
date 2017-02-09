from tinyciapi.util.singleton import SingletonMixin
from tinyciapi.util.cryptutil import Crypt as _Crypt

class Crypt(_Crypt, SingletonMixin):

    def __init__(self):
        super(Crypt, self).__init__('aaaaaaaaaabbbbbbbbbbccccccccccdd')

def crypt():
    return Crypt.me()
