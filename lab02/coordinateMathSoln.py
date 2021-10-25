#!/usr/bin/env python3
# Name: Your full name
# Group Members: Jessica Paz, Karla Silva, Okasha Attaurrehman

'''
This script asks for three sets of atomic coordinates, all provided on a single line.

The program calculates the bond lengths and angles among the three sets of coordinates using the
Triad class.

Input: three sets of coordinates on a single line
Output: bond lengths and angles between the three points

Example:

Enter Coordinates: C = (39.447, 94.657, 11.824) N = (39.292, 95.716, 11.027) Ca = (39.462, 97.101, 11.465)

then the program will output the following three lines:

N-C bond length = 1.33
N-Ca bond length = 1.46
C-N-Ca bond angle = 124.0

Note: make sure that the angle returned is in degrees

'''

import math
class Triad:
    """
    Calculate angles and distances among a triad of points.

    Author: David Bernick
    Date: March 21, 2013
    Points can be supplied in any dimensional space as long as they are consistent.
    Points are supplied as tupels in n-dimensions, and there should be three
    of those to make the triad. Each point is positionally named as p,q,r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()

    Required Modules: math
    initialized: 3 positional tuples representing Points in n-space
             p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods:  angleP(), angleR(), angleQ() angles measured in radians
          dPQ(), dPR(), dQR() distances in the same units of p,q,r

    """

    def __init__(self,p,q,r):
        """ Construct a Triad.

        Example construction:
            p1 = Triad( p=(1.,0.,0.), q=(0.,0.,0.), r=(0.,0.,0.) ).
        """
        self.p = p
        self.q = q
        self.r = r
# private helper methods
    def d2(self,a,b): # calculate squared distance of point a to b
        return float(sum((ia-ib)*(ia-ib)  for  ia,ib in zip (a,b)))

    def dot(self,a,b): # dotProd of standard vectors a,b
        return float(sum(ia*ib for ia,ib in zip(a,b)))

    def ndot(self,a,b,c): # dotProd of vec. a,c standardized to b
        return float(sum((ia-ib)*(ic-ib) for ia,ib,ic in zip (a,b,c)))

# calculate lengths(distances) of segments PQ, PR and QR
    def dPQ(self):
        """ Provides the distance between point p and point q """
        return math.sqrt(self.d2(self.p,self.q))

    def dPR(self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.d2(self.p,self.r))

    def dQR(self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.d2(self.q,self.r))

    def angleP(self):
        """ Provides the angle made at point p by segments pq and pr (radians). """
        return math.acos(self.ndot(self.q,self.p,self.r) / math.sqrt(self.d2(self.q,self.p)*self.d2(self.r,self.p)))

    def angleQ(self):
        """ Provides the angle made at point q by segments qp and qr (radians). """
        return math.acos(self.ndot(self.p,self.q,self.r) / math.sqrt(self.d2(self.p,self.q)*self.d2(self.r,self.q)))

    def angleR(self):
        """ Provides the angle made at point r by segments rp and rq (radians). """
        return math.acos(self.ndot(self.p,self.r,self.q) / math.sqrt(self.d2(self.p,self.r)*self.d2(self.q,self.r)))

def main():
    ''' Function docstring goes here'''
    data = input("Enter Coordinates: ")
    #stores the user input in a variable called data
    split_data = data.replace("(",",").replace(")",",").replace(" ","").split(",")
    #takes the user input and replaces all instances of "(", ")", and " " in the string to ",".
    #the input is also split by ",". The edited string is stored in the variable split_data
    p_coord = float(split_data[1]), float(split_data[2]), float(split_data[3])
    #saves the numerical coordinates for the first element "p" in the edited input string
    q_coord = float(split_data[5]), float(split_data[6]), float(split_data[7])
    #saves the numerical coordinates for the second element "q" in the edited input string
    r_coord = float(split_data[9]), float(split_data[10]), float(split_data[11])
    #saves the numerical coordinates for the third element "r" in the edited input string
    data_triad = Triad(p_coord, q_coord, r_coord)
    #runs the coordinates for all three elements through the Triad class and saves it to the variable data_triad
    print("N-C bond length = {0:0.2f}".format(data_triad.dPQ()))
    #calculates the distance of the bond length between element p and element q to 2 decimal places and prints it to the console
    print("N-Ca bond length = {0:0.2f}".format(data_triad.dQR()))
    #calculates the distance of the bond length between element q and element r to 2 decimal places and prints it to the console
    print("C-N-Ca bond angle = {0:0.2f}".format(math.degrees(data_triad.angleQ())))
    #calculates the angle between element p, q, and r with element q at the center
    #converts the angle stored in the variable qAngle from radians to degrees and prints it to the console to 2 decimal places

main()
