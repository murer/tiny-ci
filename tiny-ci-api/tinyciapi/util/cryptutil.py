import codecutil as codec
from Crypto import Random
from Crypto.Cipher import AES

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
