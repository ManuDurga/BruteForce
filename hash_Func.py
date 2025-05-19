import hashlib

# Hashing function for SHA256
def sha256_hash(data):
    #make sure data is a string otherwise value error
    if not isinstance(data, str):
        raise ValueError("Input data must be a string")
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Hashing function for SHA1
def sha1_hash(data):
    if not isinstance(data, str):
        raise ValueError("Input data must be a string")
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

# Hashing function for MD5
def md5_hash(data):
    if not isinstance(data, str):
        raise ValueError("Input data must be a string")
    return hashlib.md5(data.encode('utf-8')).hexdigest()
