#!/usr/bin/env python3
"""
Author : Nicholas Accomazzo <naccomazzo@arizona.edu>
Date   : 2025-03-10
Purpose: DNA to RNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Transcribe DNA into RNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="+",
        type=argparse.FileType("rt"),
        help="Input DNA file",
    )

    parser.add_argument(
        "-o",
        "--out_dir",
        metavar="DIR",
        type=str,
        default="out",
        help='Output directory (default: "out")',
    )

    return parser.parse_args()


# --------------------------------------------------
def transcribe_dna_to_rna(dna):
    """Convert DNA sequence to RNA (T → U)"""
    return dna.replace("T", "U").replace("t", "u")


# --------------------------------------------------
def main():
    """Process input files and write transcribed RNA to output files"""
    args = get_args()
    out_dir = args.out_dir

    # Create output directory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    num_files = 0
    num_sequences = 0

    for file in args.files:
        output_file_path = os.path.join(out_dir, os.path.basename(file.name))
        num_files += 1

        with open(output_file_path, "wt", encoding="utf-8") as out_fh:
            for line in file:
                rna_seq = transcribe_dna_to_rna(line.strip())
                out_fh.write(rna_seq + "\n")
                num_sequences += 1

    if num_sequences == 1:
        sequence_word = "sequence"
    else:
        sequence_word = "sequences"

    if num_files == 1:
        file_word = "file"
    else:
        file_word = "files"

    msg = (
        f"Done, wrote {num_sequences} {sequence_word} "
        f'in {num_files} {file_word} to directory "{out_dir}".'
    )

    print(msg)


# --------------------------------------------------
if __name__ == "__main__":
    main()
