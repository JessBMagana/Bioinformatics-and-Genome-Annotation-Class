#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: none

""" Creates an object of class Announcer. Prints out a name.

Input:  Announcer class
	A variable named student with the string: "Hello [name]"

Output: Hello [name] """

class Announcer (str): # Announcer is now defined as a kind of python string.
    """
    A class to represent an announcer.

    ----

    Attribute: a message in str format.

    -------

    Methods

    ------

    printMe(self):
         Prints the message given
    """

    def printMe (self):
        """
        Prints the message provided.
	"""
        print (self)

""" This line takes a string inside the Announcer class.
It also assigns it to the variable (student).  """

student = Announcer ('Hello Jessica')

""" This line prints the string given under the (student) variable. """

student.printMe()




