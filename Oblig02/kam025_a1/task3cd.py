# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

import sys
import os.path # to check if a file exists
import datetime # get datetime

# Task 3

# (c) and (d)

def log_entry(filename, string):
    """This function logs activity. You need to state which activity. 
    """
    timedate  = datetime.datetime.today()
    

    if os.path.isfile(filename):
        with open(filename, 'a') as fp: 
            fp.write("\n" + str(timedate) + ":\n  " + string)
            fp.close() # close file

        print(f"'{string}' has now been added to {filename}.")
    
    else: # if file does not exist
        newfilename = "log.txt"
        fp = open(newfilename, "a") 
        fp.write("\n" + str(timedate) + ":\n  " + string)
        fp.close() # close file

        print(f"'{filename}' does not exist.")
        print(f"'{string}' has therefore been added to '{newfilename}'.")


if __name__ == "__main__":

    try: # try this first
        filename = sys.argv[1]
        string = sys.argv[2]
    except IndexError: # if it doesn't work, do exception handling
        print(f"You need to provide a message.")
        print(f"Usage: python task3cd.py <filename> <message>")
        exit()

log_entry(filename, string)

