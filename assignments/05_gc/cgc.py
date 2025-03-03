#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-03-03
Purpose: Compute GC content
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Compute GC content",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "FILE",
        metavar="FILE",
        type=argparse.FileType("rt"),
        nargs="?",
        default=sys.stdin,
        help="Input sequence file",
    )
    return parser.parse_args()


# --------------------------------------------------
def read_fasta(file):
    """Read FASTA file and return dict of {ID: sequence}"""

    sequences = {}
    current_id = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            sequences[current_id] = ""
        else:
            sequences[current_id] += line
    return sequences


# --------------------------------------------------
def gc_content(sequence):
    """Calculate GC content percentage of a sequence"""
    gc_count = sum(1 for base in sequence if base in "GCgc")
    return (gc_count / len(sequence)) * 100 if sequence else 0


# --------------------------------------------------
def main():
    """Find the sequence with the highest GC content"""

    args = get_args()
    sequences = read_fasta(args.FILE)

    highest_id, highest_gc = "", 0.0
    for seq_id, sequence in sequences.items():
        gc = gc_content(sequence)
        if gc > highest_gc:
            highest_gc = gc
            highest_id = seq_id

    print(f"{highest_id} {highest_gc:.6f}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
