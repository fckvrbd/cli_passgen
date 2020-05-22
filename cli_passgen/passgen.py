import argparse
import random
import string


class Generator():
    def __init__(self, **chars: int):
        self.chartypes = {}
        self.password = []
        for chartype, charamount in chars.items():
            self.chartypes[chartype] = charamount
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.specials = string.punctuation

    def generator(self):
        if self.chartypes.get("letters"):
            self.password.append(''.join(
                random.choice(self.letters) for i in range(
                    self.chartypes.get("letters"))))
        if self.chartypes.get("numbers"):
            self.password.append(''.join(
                random.choice(self.numbers) for i in range(
                    self.chartypes.get("numbers"))))
        if self.chartypes.get("specials"):
            self.password.append(''.join(
                random.choice(self.specials) for i in range(
                    self.chartypes.get("specials"))))
        return ''.join(random.sample(list(''.join(self.password)), sum(
            len(char) for char in self.password)))


def main():
    parser = argparse.ArgumentParser(
        prog="cli-passgen", usage='%(prog)s [option] [amount]',
        description="Generates password with users wishes \
            \nDon't give any parameters if you want a randomnly generated \
            24 character password")
    parser.add_argument(
        '--letters', type=int,
        help="How many letters would you like in your password?")
    parser.add_argument(
        '--numbers', type=int,
        help="How many numbers would you like in your password?")
    parser.add_argument(
        '--specials', type=int,
        help="How many special characters would you like in your password?")
    args = parser.parse_args()
    if args.letters is None and args.numbers is None and args.specials is None:
        args.letters, args.numbers, args.specials = 8, 8, 8
    return args


if __name__ == "__main__":
    args = main()
    gen = Generator(
        letters=args.letters,
        numbers=args.numbers,
        specials=args.specials)
    print(gen.generator())
