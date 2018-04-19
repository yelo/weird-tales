#!/bin/env python
import random
import sys

from weirdtales import WeirdTales


def main():
    """
    The main method.
    """
    path = 'input.txt'
    ngram = 3
    rounds = 50

    if len(sys.argv) > 1:
        path = sys.argv[1]
    if len(sys.argv) > 2:
        ngram = int(sys.argv[2])
    if len(sys.argv) > 3:
        rounds = int(sys.argv[3])

    wt = WeirdTales(path, ngram)
    print(wt.generate_output(rounds))


if __name__ == '__main__':
    main()
