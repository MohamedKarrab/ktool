import itertools
import os


def w_gen(args):
    def generate_wordlist(min_length, max_length, charset):
        for length in range(min_length, max_length + 1):
            for word in itertools.product(charset, repeat=length):
                yield "".join(word)

    if args.min_length > args.max_length:
        print("min_length can't exceed max_length")
        return True

    if args.max_length > 5:
        print("MAX LENGTH CAN'T EXCEED 5, YOU DON'T WANNA RUN OUT OF STORAGE, THIS WILL BE FIXED SOON!")
        return True

    try:
        args.output = os.path.abspath(args.output)
        with open(args.output, 'w') as f:
            for word in generate_wordlist(args.min_length, args.max_length, args.charset):
                f.write(word + '\n')
        print("wordlist generated in " + args.output)
    except Exception as e:
        print(e)
        return True


def w_mod(args):
    try:
        args.output = os.path.abspath(args.output)
        args.wordlist = os.path.abspath(args.wordlist)

        with open(args.wordlist, errors='ignore') as input_file:
            words = input_file.read().splitlines()

        with open(args.output, 'w') as output_file:
            for word in words:
                w_len = len(word)
                if args.min_length <= w_len <= args.max_length:
                    output_file.write(word + "\n")
        print("wordlist generated in " + args.output)

    except Exception as e:
        print(e)
        return True
