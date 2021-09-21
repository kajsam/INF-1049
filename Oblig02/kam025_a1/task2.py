# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

# Task 2 

# (a)

import csv # to read csv files, I think
import sys # for command line arguments
from os import read # to read files

def read_csv(filename): 
    """This function takes a filename as input, 
    and returns a list of lists, given that the file
    is a .csv file. Each line is a list. 
    """

    data = [] # declare an empty list

    # first, the file is opened ('r' for read mode), and we name a pointer 'fp'
    with open(filename, 'r') as fp: 
        # we now can read the file using the pointer
        reader = csv.reader(fp, delimiter = ",")
        
        for line in reader:
            data.append(line)

    return data


# (b) everything involving 'skiplines' is a modification

# added keyword argument with default = 0
def read_csv_skipline(filename, skiplines = 0): 
    """This function takes a filename as input, 
    and returns a list of lists, given that the file
    is a .csv file. An optional argument, 'skiplines', 
    allows you to skip one or more lines. If 'skiplines' is empty, 
    then the default 0 makes sure that no line is skipped. 
    """

    data = [] # declare an empty list
    float_data = [] # declare another empty list for (c)

    # first, the file is opened ('r' for read mode), and we name a pointer 'fp'
    with open(filename, 'r') as fp: 
        # we now can read the file using the pointer
        reader = csv.reader(fp, delimiter = ",")

        for i in range(skiplines): # skips lines
            next(reader)

        for line in reader:
            data.append(line)

            # (c) Convert all numbers to type 'float'
            str = " " # start an empty string
            str = str.join(line) # convert list to string
            str = str.split() # split the string

            # convert each element to float
            float_line = [float(i) for i in str]

            # add the list of floats
            float_data.append(float_line)

    return data, float_data # return data and float_data

if __name__ == "__main__":

    try: 
        filename = sys.argv[1]
    except IndexError:
        print(f"Usage: python task2.py <filename> or python task2.py <filename> <number of lines to skip>")

    # call function with single input argument from terminal
    if len(sys.argv) == 2:
        data = read_csv(filename)
        print(data)

    # call function with extra input 'skiplines' from terminal

    elif len(sys.argv) == 3:
        skiplines = int(sys.argv[2])
        data, float_data = read_csv_skipline(filename, skiplines)
        print(data)

        print(float_data)