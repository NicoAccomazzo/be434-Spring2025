#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-05-05
Purpose: Encode or decode a message from a file using the Caesar Shift cipher
         by shifting each letter in the alphabet by a specified number of
         positions.
"""

import argparse
import sys


# --------------------------------------------------
def build_substitution_table(shift, decode=False):
    """Build a Caesar cipher substitution table based on shift and mode
    (encode/decode)."""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = {}

    for i, from_letter in enumerate(alpha):
        to_index = (i + shift) % 26 if not decode else (i - shift) % 26
        to_letter = alpha[to_index]
        table[from_letter] = to_letter

    return table


# --------------------------------------------------
def process_text(text, table):
    """Apply the substitution table to the input text and return transformed
    result."""
    result = []
    for char in text:
        upper_char = char.upper()
        if upper_char in table:
            result.append(table[upper_char])
        else:
            result.append(char)
    return "".join(result).upper()


# --------------------------------------------------
def get_args():
    """Parse and return the command-line arguments."""
    parser = argparse.ArgumentParser(
        description="caesar shift",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("FILE",
                        type=argparse.FileType("r"),
                        help="Input file")

    parser.add_argument("-n",
                        "--number",
                        type=int,
                        default=3,
                        help="A number to shift")

    parser.add_argument("-d",
                        "--decode",
                        action="store_true",
                        help="A boolean flag")

    parser.add_argument("-o",
                        "--outfile",
                        type=argparse.FileType("w"),
                        default=sys.stdout,
                        help="Output file (default: std.out)")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program logic: read input, encode/decode, write output."""
    args = get_args()
    shift = args.number % 26
    sub_table = build_substitution_table(shift, args.decode)

    for line in args.FILE:
        transformed = process_text(line.rstrip(), sub_table)
        print(transformed, file=args.outfile)


if __name__ == "__main__":
    main()
