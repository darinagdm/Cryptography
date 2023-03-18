import rsa

class KeyPair:
    def __init__(self):
        self.public_key = rsa.PublicKey
        self.__private_key = rsa.PrivateKey

    def gen_key_pair(self):
        key_pair = rsa.newkeys(2048)
        self.public_key = key_pair[0]
        self.__private_key = key_pair[1]
        with open("private_key.pem", "wb") as f:
            f.write(self.__private_key.save_pkcs1("PEM"))
        with open("public_key.pem", "wb") as f:
            f.write(self.public_key.save_pkcs1("PEM"))
        return self

    def print_key_pair(self):
        print(self.public_key.save_pkcs1("PEM").decode())
        print(self.__private_key.save_pkcs1("PEM").decode())

    def to_string(self):
        return f"""{self.__private_key.save_pkcs1("PEM").decode()}
{self.public_key.save_pkcs1("PEM").decode()}"""
