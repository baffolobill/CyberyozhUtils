import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='Application that prints out text report data. '
                                                 'To redirect output to file.txt, use > file.txt')
    parser.add_argument('--language',
                        help='Language of the text report',
                        choices=["EN", "RU", "CN"],
                        default='EN',
                        required=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
