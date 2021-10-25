#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: none

""" This script provides the AT ratio of a DNA sequence.
-------------
Input: The user enters a DNA sequence.
------------
Output: The ratio (a number between 0 and 1) of A's and T's in the sequence. """

class dnaString(str):
    """ A class to analyze a DNA string.
    --------
    Input: a sequence of DNA in str format.
    -------
    Output: none. """

    def length(self):
        """ returns the length of the DNA sequence to the getAT() method. """
        return len(self)

    def getAT(self):
        """ Calculates the ratio of A's and T's in the DNA sequence.
        Attributes
        ---------
        num_A: int
            counts the number of A's in the DNA sequence
        num_T: int
            counts the number of T's in the DNA sequence """
        num_A = self.count("A") #the A in count() needed ""
        num_T = self.count("T")
        return (num_A + num_T)/(self.length()) #should be length() not len()

#This line asks the user to input a DNA sequence.
#It also assigns that sequence to the variable (dna).

dna = input("Enter a DNA sequence: ")

#This line takes the DNA sequence stored in the (dna) variable and uses the
#upper() function to capitalize each nucleotide in the sequence.
#It also stores the capitalized sequence into the variable (upperDNA).

upperDNA = dna.upper()

#This line takes the capitalized DNA sequence stored in the variable upperDNA
#and runs it through the dnaString class. It also stores the output into the
#variable (coolString).

coolString = dnaString(upperDNA)

""" This line prints out the AT ratio of the given DNA sequence to three decimal places
using the getAT() function. """

print("AT content = {0:0.3f}".format(coolString.getAT())) #should be 0:0.3 to get three decimal places.
