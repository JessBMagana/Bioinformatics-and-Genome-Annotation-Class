#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: List full names

'''
This script will convert DNA or RNA codons into their respective amino acids
using the dictionary "RNA_codon_table" and "dnaCodonTable".

It will also convert the one letter abbreviation of the amino acid to its three
letter code using the dictionary "short_AA".

It will also convert the three letter amino acid code to its one letter code
also using the dictionary "short_AA".

Input: three letter or one letter code (str)
Output: Three letter or one letter amino acid name

Example:

if I enter “ATG” (without quotes), then the program will output:
ATG = MET

if I enter “UAG” (without quotes), then the program will output:
UAG = ---

if I enter “E” (without quotes), then the program will output:
E = GLU

if I enter “Asp” (without quotes), then the program will output:
ASP = D

'''
short_AA = {
            'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
            'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
            }

long_AA = {value:key for key,value in short_AA.items()}

RNA_codon_table = {
# Second Base
# U             C             A             G
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
#C
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}
dnaCodonTable = {key.replace('U','T'):value for key, value in RNA_codon_table.items()}

class Converter(str):

    def convert(self):
        if self in short_AA: #if the input is in the short_AA dictionary
            return(short_AA.get(self)) #prints the value corresponding to the input key
        elif self in long_AA: #if the input is in the long_AA dictionary
            return(long_AA.get(self)) #prints the value corresponding to the input key
        elif self in RNA_codon_table: #if the input is in the RNA_codon_table dictionary
            return(RNA_codon_table.get(self)) #prints the value corresponding to the input key
        elif self in dnaCodonTable: #if the input is in the dnaCodonTable dictionary
            return(dnaCodonTable.get(self)) #prints the value corresponding to the input key
        else: #if the input is not in any of the dictionaries
            return("unknown")


def main():
    ''' Function docstring goes here'''
    data = input("Enter amino acid code: ")
    #asks the user to enter an amino acid code
    data_upper = Converter(data.upper())
    #capitalizes the input and runs it through the Converter class.
    #Then stores it in a variable called data_upper.
    convert_data = data_upper.convert()
    #runs the input stored in data_upper through the function convert().
    print(convert_data)
    #prints the output to the console

main()
