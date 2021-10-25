#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: none

""" This script will provide the user with the length of their DNA sequence and with a count
of each nucleotide (A, T, G, C).

Input: a string of DNA.

Output: a message providing the number of nucleotides in the given sequence
	and the count of each nucleotide. """

class dnaString (str):
    """ a class that represents a DNA string. """
    def length(self):
	""" returns the lenth of the DNA string to the method getAT() """
        return (len(self))

    def getAT(self):
	""" returns the number of each nucleotide in the DNA sequence.
	....
	Attributes
	---------
	num_A: int
	    the number of A's in the DNA sequence.
	num_T: int
	    the number of T's in the DNA sequence.
	num_G: int
	    the number of G's in the DNA sequence.
	num_C: int
	    the number of C'c in the DNA sequence. """
        num_A = self.count("A")
        num_T = self.count("T")
        num_G = self.count("G")
        num_C = self.count("C")
        return ("number As = " + str(num_A) + " number Cs = " + str(num_C)
               + " number Gs = " + str(num_G) + " number Ts = " + str(num_T))

""" This line asks the user to input a DNA sequence. It also assigns the
sequence to the variable (dna).  """

dna = input("Enter a dna sequence: ")

""" This line takes the DNA sequence given and capitalizes all the letters.
It also assigns the sequence in capital letters to the variable (upperDNA).  """

upperDNA = dna.upper()

""" This line takes the upper case DNA sequence and runs it through the dnaString class.
It also assigns it to the variable coolString. """

coolString = dnaString(upperDNA)

# Add code below
""" This line will print the following message with a count of the number of nucleotides in
the given DNA sequence under the variable (dna). """

print("Your sequence is " + str(len(dna)) +
     " nucleotides long with the following breakdown of bases:")

""" This line will print out the number of each nucleotide in the given DNA sequence. """

print(coolString.getAT())
