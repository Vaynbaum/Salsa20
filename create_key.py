import random
import string
import sys

from work_file import write_json_file


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = "".join(random.choice(letters) for i in range(length))
    return rand_string


def main():
    out_file = sys.argv[1]
    data = {"key": generate_random_string(32), "nonce": generate_random_string(8)}
    write_json_file(out_file, data)


if __name__ == "__main__":
    main()
