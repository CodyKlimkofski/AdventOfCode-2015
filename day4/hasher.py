import hashlib

class Hasher:
    def md5_hash(self, input_string):
        return hashlib.md5(input_string.encode()).hexdigest()
    
    def is_valid_hash(self, hash_string, leading_zeros=5):
        return hash_string.startswith('0' * leading_zeros)