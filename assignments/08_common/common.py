#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@gmail.com>
Date   : 2025-03-31
Purpose: Find common words between two files
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find common words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("file1",
                        metavar="FILE1",
                        help="Input file 1",
                        type=argparse.FileType("rt"))

    parser.add_argument("file2",
                        metavar="FILE2",
                        help="Input file 2",
                        type=argparse.FileType("rt"))

    parser.add_argument(
        "-o",
        "--outfile",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
        help="Output file",
    )

    return parser.parse_args()


# --------------------------------------------------
def get_words(file_handle):
    """Extract words from a file handle and return a set"""
    words = set()
    for line in file_handle:
        for word in line.split():
            words.add(word)
    return words


# --------------------------------------------------
def main():
    """Main program logic"""
    args = get_args()

    words1 = get_words(args.file1)
    words2 = get_words(args.file2)

    common = sorted(words1 & words2)

    for word in common:
        print(word, file=args.outfile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
