import codecutil as codec
from Crypto import Random
from Crypto.Cipher import AES as _AES

class Error(Exception):
    """Exceptions"""

class AbstractCrypt(object):

    def __init__(self):
        self._rnd = None

    def rnd(self, size):
        if not self._rnd:
            self._rnd = Random.new()
        return self._rnd.read(size)

class AES(AbstractCrypt):

    def __init__(self, key = None):
        super(AES, self).__init__()
        if not key:
            key = self.rnd(32)
        self.key = key

    def enc(self, plain):
        iv = self.rnd(16)
        cipher = _AES.AESCipher(self.key, _AES.MODE_CFB, iv)
        return iv + cipher.encrypt(plain)

    def dec(self, code):
        if len(code) < 16:
            raise Error('too small')
        iv = code[:16]
        code = code[16:]
        cipher = _AES.AESCipher(self.key, _AES.MODE_CFB, iv)
        return cipher.decrypt(code)

class Crypt(AES):

     def __init__(self, *args, **kwargs):
        super(Crypt, self).__init__(*args, **kwargs)
