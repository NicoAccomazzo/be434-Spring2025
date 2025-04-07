#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@gmail.com>
Date   : 2025-04-07
Purpose: Filter a delimited file for a value, optionally in a specific column
"""

import argparse
import csv
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Filter delimited records",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        type=argparse.FileType("r"),
        required=True,
        help="Input file",
    )

    parser.add_argument(
        "-v",
        "--val",
        required=True,
        help="Value for filter",
    )

    parser.add_argument(
        "-c",
        "--col",
        help="Column name for filter",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        type=argparse.FileType("w"),
        default="out.csv",
        help="Output filename",
    )

    parser.add_argument(
        "-d",
        "--delimiter",
        default=",",
        help="Input delimiter",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Run the program"""

    args = get_args()
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if reader.fieldnames is None:
        print("No header found in input file", file=sys.stderr)
        sys.exit(1)

    if args.col and args.col not in reader.fieldnames:
        fields = ", ".join(reader.fieldnames)
        print(
            f'--col "{args.col}" not a valid column! Choose from {fields}',
            file=sys.stderr,
        )
        sys.exit(1)

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    search_term = args.val
    num_written = 0

    for rec in reader:
        if args.col:
            value = rec.get(args.col, "")
            if re.search(search_term, value, re.IGNORECASE):
                writer.writerow(rec)
                num_written += 1
        else:
            values = (str(v) for v in rec.values())
            if any(
                    re.search(search_term, val, re.IGNORECASE)
                    for val in values):
                writer.writerow(rec)
                num_written += 1

    print(f'Done, wrote {num_written} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == "__main__":
    main()
