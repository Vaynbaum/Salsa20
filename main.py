import sys
from cipher import Cipher
from work_file import *


def main():
    key_file = sys.argv[1]
    in_file = sys.argv[2]
    out_file = sys.argv[3]
    text = read_full_file(in_file)
    key_json = read_json_file(key_file)
    cipher = Cipher()
    enc = cipher.Encrypt(text, key_json["key"], key_json["nonce"])
    write_file(out_file, enc)


if __name__ == "__main__":
    main()
