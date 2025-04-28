#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-04-28
Purpose: Emulate grep to search for patterns in files
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search (default: False)',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file (default: stdout)',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Search for PATTERN in FILE(s)"""

    args = get_args()
    pattern = args.pattern
    files = args.files
    insensitive = args.insensitive
    out_fh = args.outfile

    flags = re.IGNORECASE if insensitive else 0
    regex = re.compile(pattern, flags)

    multiple_files = len(files) > 1

    for fh in files:
        filename = fh.name
        for line in fh:
            line = line.rstrip()
            if regex.search(line):
                if multiple_files:
                    print(f'{filename}:{line}', file=out_fh)
                else:
                    print(line, file=out_fh)

    if out_fh is not sys.stdout:
        out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
