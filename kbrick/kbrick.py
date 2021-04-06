import argparse


def parse_args():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("hello")
    parser.add_argument("-n", "--name", type=str,
                        help='Your name')

    return parser.parse_args()


def main():
    args = parse_args()
    name = args.name
    print(hello(name))


def hello(name):
    if name:
       greeting = f"Hello, {name}!"
    else:
        greeting = "Hello World!"
    return greeting

if __name__ == '__main__':
    main()
