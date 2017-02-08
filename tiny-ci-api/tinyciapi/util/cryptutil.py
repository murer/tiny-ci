import codecutil as codec

def parse(key):
    return Crypt('abc', 'def')

def create():
    return Crypt('abc', 'def')

class Crypt(object):

    def __init__(self, secret, salt):
        self.secret = secret
        self.salt = salt

    def enc(self, plain):
        return codec.b64enc(plain)

    def dec(self, data):
        return codec.b64dec(data)

def __main():
    key = create()
    data = key.enc('test')
    print data
    print key.dec(data)

if __name__ == '__main__':
    __main()
