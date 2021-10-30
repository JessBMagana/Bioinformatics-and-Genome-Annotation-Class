#!/usr/bin/env python3
# Name: Jessica Magana
# Date: 10/11/21
# Group: <Your group members>

"""
This script takes in a FASTA file as input.
It then calculates the nucleotide content,
the sequence length, the GC content, and
the amino acid composition.

Attributes
----------
seq: str
    the DNA sequence in the FASTA file,
    saved in the variable "seq" after the
    header has been removed by the for loop in main().

Methods
-------
aComposition():
    finds the ratio of "A" nucleotides in seq.
tComposition():
    finds the ratio of "T" nucleotides in seq.
cComposition():
    finds the ratio of "C" nucleotides in seq.
gComposition():
    finds the ratio of "G" nucleotides in seq.
gcContent():
    finds the ratio of G's and C's in seq.
sequenceLength():
    finds the length of the sequence.
aaComposition():
    finds the ratio of each of the 20 amino acids in seq.

Input:

FASTA file (sequence.fasta)

Output:

% of As: XXX %
% of Ts: XXX %
% of Cs: XXX %
% of Gs: XXX %
GC content: XXX %
Sequence Length = XXX bp
A = XXX %
T = XXX %
I = XXX %
M = XXX %
L = XXX %
G = XXX %
R = XXX %
S = XXX %
N = XXX %
V = XXX %
P = XXX %
E = XXX %
D = XXX %
_ = XXX %
F = XXX %
Y = XXX %
W = XXX %
C = XXX %
Q = XXX %
K = XXX %
H = XXX %

"""

import sys

dnaCodonTable = {
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
	'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
	}

class nucParams(object):
    """
    This class represents a FASTA file object.

    Attributes
    ----------
    seq: str
        the DNA sequence in the FASTA file, saved in the variable "seq" after the header has been
        removed by the for loop in main().

    Methods
    -------
    aComposition():
        finds the ratio of "A" nucleotides in seq.
    tComposition():
        finds the ratio of "T" nucleotides in seq.
    cComposition():
        finds the ratio of "C" nucleotides in seq.
    gComposition():
        finds the ratio of "G" nucleotides in seq.
    gcContent():
        finds the ratio of G's and C's in seq.
    sequenceLength():
        finds the length of the sequence.
    aaComposition():
        finds the ratio of each of the 20 amino acids in seq.

    """
    def __init__(self, seq):
        """
        Creates the attribute needed for each method

        Attribute
        ---------
        seq: str
            the DNA sequence in the FASTA file,
            saved in the variable "seq" after the
            header has been removed by the for loop in main().
        """
        self.seq = seq

    def aComposition(self):
        """
        Finds the ratio of "A" nucleotides in seq.

        Uses the method count() to count the number of A's
        in the sequence and divides it by the length of
        the sequence.

        """
        return (self.seq.count("A")/len(self.seq)) * 100

    def tComposition(self):
        """
        Finds the ratio of "T" nucleotides in seq.

        Uses the method count() to count the number of T's
        in the sequence and divides it by the length of
        the sequence.

        """
        return (self.seq.count("T")/len(self.seq)) * 100

    def cComposition(self):
        """
        Finds the ratio of "C" nucleotides in seq.

        Uses the method count() to count the number of C's
        in the sequence and divides it by the length of
        the sequence.

        """
        return (self.seq.count("C")/len(self.seq)) * 100

    def gComposition(self):
        """
        Finds the ratio of "G" nucleotides in seq.

        Uses the method count() to count the number of G's
        in the sequence and divides it by the length of
        the sequence.

        """
        return (self.seq.count("G")/len(self.seq)) * 100

    def gcContent(self):
        """
        Finds the ratio of "C" and "G " nucleotides in seq.

        Uses the method count() to count the number of C's
        and G's in the sequence and divides it by the length of
        the sequence.

        """
        return ((self.seq.count("G") + self.seq.count("C"))/len(self.seq)) * 100

    def sequenceLength(self):
        """
        Finds the length of the sequence using the method len()
        """
        return len(self.seq)

    def aaComposition(self):
        """
        Finds the ratio of each of the 20 amino acids in the sequence.

        Attributes
        ----------
        seq: str
            the DNA sequence in the FASTA file.

        codon_to_aa: list
            a list of all three letter code amino acids in the DNA sequence starting from index 0.

            a for loop iterates through the DNA sequence three characters at a time and
            matches the codon with the keys of codons in the dictionary dnaCodonTable.

            the value of each key is then saved in this list.

            the codons in this list are capitalized using the method upper() to match the keys in
            the dictionary short_AA.

        aa_to_short_aa: list
            a list of all one letter code amino acids that match the list codon_to_aa.

            a for loop iterates through the list codon_to_aa and matches the upper cased
            three letter amino acid code key in the dictionary short_AA with its one letter
            amino acid code value.

            the values are then saved in this list.

        output: list
            returns the list aa_to_short_aa which contains a list of one letter code
            amino acids.

        """
        clean_seq = "" # an empty string

        for i in self.seq: # iterates through each nucleotide in self.seq
            if i == "N": # if the nucleotide is denoted by the letter N
                pass # skip it
            else: # if the nucleotide is anything besides an N (i.e. A, T, C, G)
                clean_seq += i # add the nucleotide to the growing string

        codon_to_aa = [] # an empty list that will save each three letter amino acid found in the sequence.
        # aa_to_short_aa = [] # an empty list that will save each one letter amino acid matched from the list codon_to_aa

        for k in range(0,len(clean_seq),3):
        # iterates through the sequence starting from zero until
        # the length of the sequence by steps of three.
            codon = clean_seq[k:k+3] # iterates through each set of three nucleotides in the sequence
            if len(codon) < 3:
                pass # ignores extra bases in the sequence
            else:
                codon_to_aa.append(dnaCodonTable.get(codon))
                # finds the value of the key, codon, and saves it into the list
                # codon_to_aa. The value is also capitalized by the method upper()
                # so that it matches with the keys in the dictionary short_AA.

        # for k in range(len(codon_to_aa)): # iterates through the list codon_to_aa.
        #     aa_to_short_aa.append(short_AA.get(codon_to_aa[k]))
        #     # takes the value of the key "k" in codon_to_aa matched to the dictionary
        #     # short_AA. Saves the values into the list aa_to_short_aa.

        return codon_to_aa

def main():
    """
    Takes in the FASTA file as input.
    It then opens and reads the FASTA file.
    It runs the file through a for loop that
    skips the header of the file that starts
    with ">" and saves the rest of the file
    containing the DNA sequence in the variable seq.

    the main function then creates an instance of the
    nucParams class using the seq variable.

    lastly, the main function prints each output.

    """
    seq = "" # this is an empty string named "seq"
    # this chunk of code uses the open() method to open and read the
    # FASTA file given through the terminal.
    # In the terminal, the line "python3 nucParams.py sequence.fasta" should be provided
    # sys.argv[1] is the FASTA file
    with open(sys.argv[1]) as fasta_data: #opens the fasta file and saves it into the variable fasta_data
        for line in fasta_data: # iterates through each line in the FASTA file
            line = line.rstrip() # the rstrip() function removes any trailing spaces
            if line[0] == ">": # if the first character in the file is ">"
                pass #skips the line
            else: # if the first character is not ">"
                seq += line.upper() # save all other lines into the variable "seq"

    # creates an instance of the class nucParams with the FASTA file provided.
    # saves it into the variable fasta_seq.
    fasta_seq = nucParams(seq)

    print("% of A's: {0:0.0f}".format(fasta_seq.aComposition()) + " %")
    # prints the ratio of "A" nucleotides in the sequence as a whole number and a percentage.
    print("% of T's: {0:0.0f}".format(fasta_seq.tComposition()) + " %")
    # prints the ratio of "T" nucleotides in the sequence as a whole number and a percentage.
    print("% of C's: {0:0.0f}".format(fasta_seq.cComposition()) + " %")
    # prints the ratio of "C" nucleotides in the sequence as a whole number and a percentage.
    print("% of G's: {0:0.0f}".format(fasta_seq.gComposition()) + " %")
    # prints the ratio of "G" nucleotides in the sequence as a whole number and a percentage.
    print("GC Content: {0:0.2f}".format(fasta_seq.gcContent()) + " %")
    # prints the ratio of G's and C's in the sequence as a whole number and a percentage.
    print("Sequence Length: " + str(fasta_seq.sequenceLength()) + " bp")
    # prints the length of the sequence

    #Extra Credit:
    my_AAs = fasta_seq.aaComposition()
    # saves the output of the method aaComposition into the variable my_AAs

    unique_aa = [] # an empty list that will hold each unique amino acid in the sequence

    for i in my_AAs: # iterates through the amino acids list
        if i not in unique_aa: # if this amino acid is not in the list my_AAs
            unique_aa.append(i) # add that amino acid to the list

    for aa in unique_aa:
        print("{0} = {1:.0f} %".format(aa,(my_AAs.count(aa)/len(my_AAs))*100))
    # prints the amino acid composition for each unique amino acid as a whole number

# Run the function main()
main()
