# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

import sys # terminal input
import os.path # to check if a file exists
import datetime # get datetime

# Task 3

# (c) and (d)

def log_entry(filename, string):
    """This function logs activity. You need to state which activity. 
    Time and date is retrieved automatically. 
    """
    timedate  = datetime.datetime.today() # gets time and date
    
    if os.path.isfile(filename): # if file exists
        with open(filename, 'a') as fp: # opens file and creates handle
            fp.write("\n" + str(timedate) + ":\n  " + string) # add this to txt-file

        print(f"'{string}' has now been added to {filename}.") # output to the user
    
    else: # if file does not exist
        newfilename = "log.txt" # defines new file name
        with open(newfilename, "a") as fp: # makes and opens file, creates handle
            fp.write("\n" + str(timedate) + ":\n  " + string) # add this to txt-file

        # output to user
        print(f"'{filename}' does not exist. '{string}' has therefore been added to '{newfilename}'.")


if __name__ == "__main__":

    try: # try this first, two terminal inputs
        filename = sys.argv[1]
        string = sys.argv[2]
    except IndexError: # if it doesn't work, do exception handling
        print(f"You need to provide a message.")
        print(f"Usage: python task3cd.py <filename> <message>")
        exit()

log_entry(filename, string) # call function

