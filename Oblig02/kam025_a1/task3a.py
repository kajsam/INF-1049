# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

import sys
import os.path # to check if a file exists

# Task 3

# (a)

def write_string(filename): 
    """This function writes a string to a text file in a new line. 
    If the file does not exist, the string is added to log.txt
    """
    string = input("Write your string here: ")
    
    if os.path.isfile(filename):
        with open(filename, 'a') as fp: 
            fp.write("\n" + string)
            fp.close() # close file

        print(f"'{string}' has now been added to {filename}.")
    
    else: # if file does not exist
        newfilename = "log.txt"
        fp = open(newfilename, "a") 
        fp.write("\n" + string) 
        fp.close() 

        print(f"'{filename}' does not exist.")
        print(f"'{string}' has therefore been added to '{newfilename}'.")


if __name__ == "__main__":

    try: 
        filename = sys.argv[1]
    except IndexError:
        print(f"Usage: python task3.py <filename>")

    write_string(filename)

