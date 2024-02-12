#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Define an ArgumentParser object and its command-line arguments
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')

# Define command-line arguments
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Optional motif to search for")

# Check if no command-line arguments are provided, print help, and exit if true
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the command-line arguments
args = parser.parse_args()

# Convert the sequence to uppercase
args.seq = args.seq.upper()  # Ensure uniform case for sequence comparison

# Check if the sequence consists of valid DNA or RNA characters
if re.search('^[ACGTU]+$', args.seq):
    # Determine if the sequence is DNA, RNA, or neither
    if 'T' in args.seq and 'U' not in args.seq:
        print('The sequence is DNA')
    elif 'U' in args.seq and 'T' not in args.seq:
        print('The sequence is RNA')
    elif 'T' in args.seq and 'U' in args.seq:
        print('The sequence is not DNA or RNA')
    else:
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not DNA nor RNA')

# If a motif is provided, convert it to uppercase and search for it in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: Looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
