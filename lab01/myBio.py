#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: none

""" Build a Person object and have it introduce itself.

input: a series of variables that contain strings with information about the person.

output: lines of text introducing the person with the information provided. """

class Person:
    """ A class to represent a person.

     Attributes
     ------------
     name: str
         first name of the person
     username: str
         the username of the person's student email
     student_type: str
         what level of student the person is
     major: str
         the person's field of study
     reason_for_taking_class: str
         the person's reasoning for taking this class
     biology_interest: str
         the person's interest in the biology field
     coding_experience: str
         the person's prior experience with coding languages and which languages

     Methods
     ---------
     introduce()
         Prints the person's bio
    """

    def __init__(self,name,username,student_type,major,reason_for_taking_class,biology_interest,coding_experience):
        """ Constructs all the necessary attributes for the Person object.

	    Parameters
	    ------------
	    name: str
		first name of the person
	    username: str
		the username of the person's student email
	    student_type: str
		what level of student the person is
  	    major: str
		the person's field of study
	    reason_for_taking_class: str
		the person's reasoning for taking this class
	    biology_interest: str
		the person's interest in the biology field
	    coding_experience: str
		the person's prior experience with coding languages and which languages """

        self.myName = name
        self.myUsername = username
        self.myStudentType = student_type
        self.myMajor = major
        self.myReasonForTakingClass = reason_for_taking_class
        self.myBioInterest = biology_interest
        self.myCodingExperience = coding_experience

    def introduce (self):
        """ Prints the person's bio """

        print ("My name is {0}".format(self.myName))
        print ("My username is {0}".format(self.myUsername))
        print ("I am a {0}".format(self.myStudentType))
        print ("My major is {0}".format(self.myMajor))
        print ("{0}".format(self.myReasonForTakingClass))
        print ("{0}".format(self.myBioInterest))
        print ("I have prior programming experience using {0}".format(self.myCodingExperience))

#The following variables are meant to contain information about the person's biography.

name = 'Jessica Magana'
username = 'jmagana5'
student_type = 'second year Master student'
major = 'Cell and Molecular Biology'
reason_for_taking_class = 'I am taking this class because I am interested in genetics and I have really enjoyed learning how to code.'
biology_interest = 'I am interested in genetic diseases and helping find treatments or cures for them.'
coding_experience = 'R and Python.'

#This line inputs the variables created into the Person class.
#These variables contain strings with the required information.
#It also assigns the Person class into the variable (student).

student = Person(name,username,student_type,major,reason_for_taking_class,biology_interest,coding_experience)

#This line takes the information assigned to (student) and passes it through the
#introduce function. It outputs each message created in the function.

student.introduce()
