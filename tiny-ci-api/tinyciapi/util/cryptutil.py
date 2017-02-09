import codecutil as codec
from Crypto import Random
from Crypto.Cipher import AES as _AES

class Error(Exception):
    """Exceptions"""

class AES(object):

    def __init__(self, key = None):
        if not key:
            key = 'aaaaaaaaaabbbbbbbbbbccccccccccdd'
        self.key = key
        print 'creating', key, self.key

    def enc(self, plain):
        iv = '1234567890123456'
        cipher = _AES.AESCipher(self.key, _AES.MODE_CFB, iv)
        print 'enc', self.key, iv, plain
        return iv + cipher.encrypt(plain)

    def dec(self, code):
        if len(code) < 16:
            raise Error('too small')
        iv = code[:16]
        code = code[16:]
        cipher = _AES.AESCipher(self.key, _AES.MODE_CFB, iv)
        print 'dec', self.key, iv, code
        return cipher.decrypt(code)

"""
def parse(key):
    return Crypt('abc', 'def')

def create():
    random = Random.new()
    key = random.read(32)
    iv = random.read(16)
    return Crypt(key, iv)

class Crypt(object):

    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.cipher = AES.AESCipher(self.key, AES.MODE_CFB, self.iv)

    def secret(self):
        return codec.b64enc(self.key), codec.b64enc(self.iv)

    def enc(self, plain):
        ciphered = self.iv + self.cipher.encrypt(plain)
        return codec.b64enc(ciphered)

    def dec(self, data):
        print 'xxxx', data
        return codec.b64dec(data)

def __main():
    key = create()
    print 'key', key.secret()
    data = key.enc('test')
    print 'data', data
    print 'plain', key.dec(data)

if __name__ == '__main__':
    __main()
"""
