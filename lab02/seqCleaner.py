#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: List full names

'''
Read a DNA string from user input and return a collapsed substring of embedded
Ns to: {count}.

Input: a DNA string
Output: a capitalized DNA string with any N's found collapsed into an int within {}.

Example:
input: AaNNNNNNGTC
output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

class DNAstring(str):
    """ A class to represent a DNA string. """
    def length(self):
        return (len(self))

    def purify(self):
        """ Return an uppercased version of the string,
        collapsing a single run of Ns.

        Parameters:
        ------------
        numN: int
            counts the number of N's found in the DNA string
        N_index: int
            finds the first instance of a string of N's within the DNA string
            using the find() function. Stores the index of the first N.
        """
        if "N" in self: #if there are N's in my string
            numN = self.count("N")
            #Variable named (numN) that counts the number of N's
            #in the given sequence.
            N_index = self.find("N")
            #Variable named (N_index) that gives the start index
            #of the N sequence.
            return self[0:N_index] + "{" + str(numN) + "}" + self[(N_index+numN):]
            #returns a capitalized clean version of the DNA sequence given
            #with the number of N's.
        else: #if there are no N's in my string
            return self

def main():
    ''' Get user DNA data and clean it up.'''
    data = input('Enter DNA sequence: ')
    #stores user input into a variable called data
    thisDNA = DNAstring(data.upper())
    #capitalizes the DNA sequence provided and runs it through the DNAstring class
    pureData = thisDNA.purify()
    #runs the capitalized DNA string through the purify() function
    print(pureData)
    #prints the output to the console

main()
