#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-02-23
Purpose: Print the reverse complement of a DNA sequence
"""

import argparse
import os


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA', metavar='DNA', help='Input sequence or file')

    return parser.parse_args()


def reverse_complement(dna):
    """Generate and return the reverse complement of the DNA sequence"""
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
        'a': 't',
        't': 'a',
        'c': 'g',
        'g': 'c'
    }
    rev_comp = ''
    i = len(dna) - 1
    while i >= 0:
        base = dna[i]
        rev_comp += complement.get(base, base)
        i -= 1
    return rev_comp


def read_dna_input(input_str):
    """Read DNA input from a file or directly from the input string"""
    absolute_path = os.path.abspath(input_str)
    if os.path.isfile(absolute_path):
        with open(absolute_path, 'rt', encoding='utf-8') as file:
            dna = file.read().strip()
    else:
        dna = input_str.strip()

    return dna


def main():
    """Main function that takes an input and prints the reverse complement"""
    args = get_args()
    dna = read_dna_input(args.DNA)
    revc = reverse_complement(dna)
    print(revc)


if __name__ == '__main__':
    main()
