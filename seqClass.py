#!/usr/bin/env python
import sys, re  # Importing necessary modules
from argparse import ArgumentParser  # Importing ArgumentParser from the argparse module

# Creating an ArgumentParser object with a description
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')

# Adding command-line arguments for sequence and motif
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence (required)")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search in the sequence")

# Checking if no command-line arguments are provided, then printing help and exiting
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parsing command-line arguments
args = parser.parse_args()

# Converting the sequence to uppercase
args.seq = args.seq.upper()  # Note we just added this line

# Checking if the sequence contains only valid nucleotides (ACGTU)
if re.search('^[ACGTU]+$', args.seq):
    # Checking if 'U' is present in the sequence to determine if it's RNA
    if 'U' in args.seq:
        print('The sequence is RNA')
    else:
        print('The sequence is DNA')
else:
    print('The sequence is not DNA nor RNA')

# Checking if a motif is provided
if args.motif:
    args.motif = args.motif.upper()  # Converting the motif to uppercase
    # Printing a message indicating motif search is enabled
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence')
    # Searching for the motif in the sequence and printing the result
    if re.search(args.motif, args.seq):
        print("The motif was FOUND in the sequence")
    else:
        print("The motif was NOT FOUND in the sequence")
