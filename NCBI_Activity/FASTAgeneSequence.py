#!/usr/bin/env python3
# Name: Jessica Magana
# Date: 10/29/21

import sys

"""
This program opens and reads a FASTA and a GFF file.

It then saves the DNA sequence of the FASTA file and all
gene coordinates in the GFF file.

Finally, it extracts all of the genes in the FASTA file
based on the coordinates in the GFF file.

Input (using the command line): python_script.py filename.fna filename.gff

Output: ['DNA string', 'DNA string', .....]
"""

with open(sys.argv[1]) as fasta_data: #opens the fasta file and saves it into the variable fasta_data
    fasta_seq = "" # an empty string
    for line in fasta_data: # iterates through each line in the FASTA file
        line = line.rstrip() # the rstrip() function removes any trailing spaces
        if line[0] == ">": # if the first character in the file is ">"
            pass #skips the line
        else: # if the first character is not ">"
            fasta_seq += line.upper() # save all other lines into the variable "seq"


with open(sys.argv[2]) as gff_data: #opens the gff file and saves it into the variable gff_data
    gff_lists = [] # an empty list
    for line in gff_data: # iterates through every line in the gff file
        if line[0] != "N": # if the line does not start with the letter N
            pass # skip the line
        else: # in the line starts with the letter N
            line = line.split("\t")
            # split the line by each tab. this will make a list of every line in the gff file.
            if line[2] == 'gene': # if the list component at index 2 is 'gene'
                gff_lists.append(line)
                # append each list into the list gff_lists. this will make a nested list.
                # this nested list has 42,792 components.

gff_gene_cord = [] #an empty list that will hold the coordinates of each gene in the gff file

for list in gff_lists: # for each nested list in the list gff_lists
    gff_gene_cord.append((int(list[3]),int(list[4])))
    # append each start and stop coordinate as pairs in
    # the empty list gff_gene_cord.
    # this becomes a list of start and stop coordinate pairs

fasta_gene_list = []
# an empty list that will hold the DNA sequence
# of each gene in the FASTA file based on the
# coordinates in the gff file.

for cord in gff_gene_cord: # for each coordinate pair in the list of coordinates
    fasta_gene_list.append(fasta_seq[cord[0]:cord[1]])
    # append the DNA sequence of the FASTA file starting
    # from the start cord index to the stop cord index.

print(fasta_gene_list)
