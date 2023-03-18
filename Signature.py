import rsa

class Signature:
    def sign_data(private_key, data):
        signature = rsa.sign(data.encode(), private_key, "SHA-256")
        return (signature)

    def verify_signature(signature, data, public_key):
        try:
            if isinstance(rsa.verify(data.encode(), signature, public_key), str):
                return True
            else:
                return False
        except:
            return False

    def to_string(signature):
        return f"""{signature}"""

    def print_signature(signature):
        print(signature)
