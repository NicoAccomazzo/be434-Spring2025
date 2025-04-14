#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-04-13
Purpose: Find conserved sequence
"""

import argparse
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find conserved bases",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "FILE", metavar="FILE", help="Input file", type=argparse.FileType("rt")
    )

    return parser.parse_args()


def main():
    """Main program logic"""

    args = get_args()
    sequences = []

    for line in args.FILE:
        line = line.strip()
        if line:
            sequences.append(line)

    if len(sequences) < 2:
        sys.exit("ERROR: Need at least two sequences")

    # Check all sequences are the same length
    length = len(sequences[0])
    if not all(len(seq) == length for seq in sequences):
        sys.exit("ERROR: Sequences are not the same length")

    for seq in sequences:
        print(seq)

    # Generate conservation line
    conserved = []
    for i in range(length):
        chars = {seq[i] for seq in sequences}
        if len(chars) == 1:
            conserved.append("|")
        else:
            conserved.append("X")

    print("".join(conserved))


if __name__ == "__main__":
    main()
