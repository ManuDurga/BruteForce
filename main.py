import argparse
from bruteForce import brute_force_attack

def parse_arguments():
    parser = argparse.ArgumentParser(description="Brute Force Attack Simulator with Rate Limiting")

    parser.add_argument("--mode",choices=["simulate", "verify"],required=True,help="Choose the mode: 'simulate' to run brute force attack, 'verify' to test one password against hash")
    parser.add_argument("--hashfile",type=str,required=True,help="Path to file containing SHA256 hashed password(s)")
    parser.add_argument("--wordlist",type=str,required=False,help="Path to file containing wordlist for brute force")
    parser.add_argument("--rate",type=int,default=5,help="Max attempts per second (default: 5)")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    delay = 1 / args.rate if args.rate > 0 else 0
    try:
        with open(args.hashfile, "r") as f:
            target_hash = f.readline().strip()
    except Exception as e:
        print(f"[!] Failed to read hash file: {e}")
        exit(1)
    if args.mode == "simulate":
        if not args.wordlist:
            print("Wordlist required for simulate mode.")
            exit(1)

        result = brute_force_attack(target_hash,hash_type="sha256",wordlist=args.wordlist,delay=delay)
        if result:
            print("Password found: ",result)
        else:
            print("password not found in wordlist")
    elif args.mode == "verify":
        password = input("Enter the password to verify: ").strip()
        from hash_func import sha256_hash
        if sha256_hash(password) == target_hash:
            print("Password matches the hash.")
        else:
            print("Password does not match.")

