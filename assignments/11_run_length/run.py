#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-04-21
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression')

    parser.add_argument('text', metavar='str', help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Create RLE"""

    if not seq:
        return ''

    result = []
    prev = seq[0]
    count = 1

    for char in seq[1:]:
        if char == prev:
            count += 1
        else:
            result.append(prev if count == 1 else f'{prev}{count}')
            prev = char
            count = 1

    result.append(prev if count == 1 else f'{prev}{count}')
    return ''.join(result)


# --------------------------------------------------
def main():
    """Run RLE compression"""

    args = get_args()
    input_text = args.text

    if os.path.isfile(input_text):
        with open(input_text, encoding='utf-8') as fh:
            for line in fh:
                print(rle(line.strip()))
    else:
        print(rle(input_text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
