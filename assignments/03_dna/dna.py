#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-02-17
Purpose: Tetranucleotide frequency
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Tetranucleotide frequency",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("DNA", metavar="str", help="Input DNA sequence")

    return parser.parse_args()


# --------------------------------------------------
def count_bases(dna):
    """Count the frequency of bases A, C, G, T in a DNA sequence."""
    a_count = dna.count("A")
    c_count = dna.count("C")
    g_count = dna.count("G")
    t_count = dna.count("T")

    return a_count, c_count, g_count, t_count


# --------------------------------------------------
def main():
    """Main execution function"""

    args = get_args()
    a, c, g, t = count_bases(args.DNA)

    print(a, c, g, t)


# --------------------------------------------------
if __name__ == "__main__":
    main()
