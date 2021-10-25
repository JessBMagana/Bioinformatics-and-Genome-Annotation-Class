#!/usr/bin/env python3
# Name: Jessica Magana
# Group Members: List full names

""" This script will take a FASTQ sequence name and parse out each piece of
information in the name.

Input: @EAS139:136:FC706VJ:2:2104:15343:197393

Output:
    Instrument = EAS139
    Run ID = 136
    Flow Cell ID = FC706VJ
    Flow Cell Lane = 2
    Tile Number = 2104
    X-coord = 15343
    Y-coord = 197393 """

class FastqString(str):
    """ A class to represent a FASTQ sequence name. """

    def parse(self):
        """ Constructs all the necessary attributes for the FastqString object

        Parameters
        ----------
        instrument: str
        the first value in the sequence name. Denotes the instrument used.

        run_id: str
        the second value in the sequence name. Denotes the ID of that run.

        flow_cell_id: str
        the third value in the sequence name.

        flow_cell_lane: str
        the fourth value in the sequence name.

        tile_number: str
        the fifth value in the sequence name.

        x_coord: str
        the sixth value in the sequence name.

        y_coord: str
        the seventh value in the sequence name. """

        data_list = self.split(":")
        #a variable named data_list that holds the list created when
        #we split the sequence name by the (:) using the function .split()

        instrument = data_list[0][1:]
        #takes the first value of the sequence name without the "@"
        run_id = data_list[1]
        #takes the second value of the sequence name
        flow_cell_id = data_list[2]
        #takes the third value of the sequence name
        flow_cell_lane = data_list[3]
        #takes the fourth value of the sequence name
        tile_number = data_list[4]
        #takes the fifth value of the sequence name
        x_coord = data_list[5]
        #takes the sixth value of the sequence name
        y_coord = data_list[6]
        #takes the seventh value of the sequence name

        output = ("Instrument = " + instrument + "\n"
                  "Run ID = " + run_id + "\n"
                  "Flow Cell ID = " + flow_cell_id + "\n"
                  "Flow Cell Lane = " + flow_cell_lane + "\n"
                  "Tile Number = " + tile_number + "\n"
                  "X-coord = " + x_coord + "\n"
                  "Y-coord = " + y_coord)

        return output

def main():
    """ The main function takes the sequence name input from the user
    and runs it through the FastqString object. """
    data = input("Please enter FASTQ sequence name: ")
    #asks the user to input the FASTQ sequence name and
    #saves it to the variable "data"
    dataList = FastqString(data)
    #takes the sequence name and runs it through the FastqString object
    #then saves it to the variable "dataList"
    parsedList = dataList.parse()
    #takes the information in dataList and runs it through the parse() function
    #then saves it to the variable "parsedList"
    print(parsedList)
    #prints the final output to the console

main()
