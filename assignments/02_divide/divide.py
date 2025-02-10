#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-02-9
Purpose: Divide two integers using floor division
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Divide two numbers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "ints", metavar="INT", type=int, nargs=2, help="Numbers to divide"
    )

    args = parser.parse_args()

    if args.ints[1] == 0:
        parser.error("Cannot divide by zero, dum-dum!")

    return args


# --------------------------------------------------
def main():
    """Main execution"""

    args = get_args()
    num1, num2 = args.ints
    result = num1 // num2
    print(f"{num1} / {num2} = {result}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
