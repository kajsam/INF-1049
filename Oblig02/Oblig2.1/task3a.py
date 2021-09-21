# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

import sys # for terminal input
import os.path # to check if a file exists

# Task 3

# (a)

def write_string(filename): 
    """This function writes a string to a text file in a new line. 
    If the file does not exist, the string is added to log.txt
    """
    string = input("Write your string here: ") # takes user input from the terminal
    
    if os.path.isfile(filename): # if file exists
        with open(filename, 'a') as fp: # opens a file and creates a pointer/handle/object
            fp.write("\n" + string) # writes to file at the end
            # if using 'with', no closing is needed

        print(f"'{string}' has now been added to {filename}.") # prints to terminal, so the user knows what was done
    
    else: # if file does not exist
        newfilename = "log.txt" # defines the filename
        fp = open(newfilename, "a")  # makes and opens file simultaneously 
        fp.write("\n" + string) 
        fp.close() # close file (is smart to do)

        # prints to terminal, so the user knows what was done
        print(f"'{filename}' does not exist. '{string}' has therefore been added to '{newfilename}'.")


if __name__ == "__main__": # if called from the terminal

    try: 
        filename = sys.argv[1] # if filename was given as terminal input
    except IndexError: # error handling, giving feedback to the user
        print(f"Usage: python task3a.py <filename>")
        exit() # exit the file

    write_string(filename)

