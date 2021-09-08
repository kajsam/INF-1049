
import sys
from fileio import read_data

def get_some_data(filename):

    return read_data(filename)

if __name__ == "__main__":

    filename = input("Enter filename: ")

    data = get_some_data(filename)

    print(data)
