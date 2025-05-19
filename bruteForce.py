import time
from hash_Func import sha256_hash, sha1_hash, md5_hash

def get_hash_function(hash_type):
    hash_map = {
        'sha256': sha256_hash,
        'sha1': sha1_hash,
        'md5': md5_hash
    }
    return hash_map.get(hash_type.lower())

# Attempt brute-force attack with given hash and wordlist
def brute_force_attack(target_hash, hash_type, wordlist, delay=0):
    hash_func = get_hash_function(hash_type)
    if hash_func is None:
        raise ValueError(f"Unsupported hash type: {hash_type}")

    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                password = line.strip()
                hashed = hash_func(password)

                if hashed == target_hash:
                    return password  # Match found

                if delay:
                    time.sleep(delay)
    except FileNotFoundError:
        raise FileNotFoundError(f"Wordlist file not found: {wordlist_path}")

    return None  # No match found
