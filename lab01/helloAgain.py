#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: none

""" Build a Person object and have it introduce itself.

input: A string for [name] and [pet] in the form ([name], [pet])

output: greeting printed to screen """

class Person:
    """ A class to represent a person.

    Attributes
    -------
    name: str
        first name of the person.
    pet: str
        the person's favorite pet.

    Methods
    ------
    introduce():
        Prints the person's name and their favorite pet. """

    def __init__(self,name,pet):
        """ Constructs the necessary attributes for the person object.

	Parameters
	-------
	    name: str
		first name of the person
	    pet:
		the person's favorite pet
	 """

        self.myName = name
	""" This is an attribute that will contain the parameter name. """

        self.myPet  = pet
	""" This is an attribute that will contain the parameter pet. """

    def introduce (self):
	""" Prints the person's name and their favorite pet. """

        print ("Hi there, I am {0}, and I like {1}s".format(self.myName,self.myPet))


# put your new code here.
""" The Person function assigned to the variable student takes two strings that will 
be assigned to name and pet. """

student = Person("Jessica", "dog")


student.introduce()

""" This line of code takes the strings assigned to the variables name and pet
by the Person class and assigns that to a new variable student. The function
introduce is then run with the student parameter to execute the message:
"Hi there, I am [name], and I like [pet]s" """

