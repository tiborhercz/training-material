import os

NAME = os.getenv('NAME')


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi(NAME)
