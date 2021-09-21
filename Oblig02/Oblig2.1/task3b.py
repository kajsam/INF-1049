# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

import sys # for terminal input
import os.path # to check if a file exists
import datetime # get datetime

# Task 3

# (b)

def log_entry(filename, string):
    """This function logs activity. You need to state which activity. 
    Date and time is retrieved automatically. 
    """
    timedate  = datetime.datetime.today() # retrieves current time and date
    
    if os.path.isfile(filename): # if the file exists
        with open(filename, 'a') as fp: # open and create handle 
            fp.write("\n" + str(timedate) + ":\n  " + string) # add this at the end of txt-file  

        print(f"'{string}' has now been added to {filename}.") # output to the user
    
    else: # if file does not exist
        newfilename = "log.txt" # 
        with open(newfilename, "a") as fp: # with gives better syntax
            fp.write("\n" + str(timedate) + ":\n  " + string) # add at the end of txt-file

        # output to the user
        print(f"'{filename}' does not exist. '{string}' has therefore been added to '{newfilename}'.")


if __name__ == "__main__": # if file is called from the terminal

    try: # try to read terminal input
        filename = sys.argv[1]
    except IndexError: # error handling with instructions to user
        print(f"Usage: python task3b.py <filename>")
        exit()

    string = input("Write your recent activity here: ") # terminal input from user
    
    log_entry(filename, string) # call function

