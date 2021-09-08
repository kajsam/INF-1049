
import sys
import csv

from os import read

def read_data(filename):

    if filename.endswith(".csv"):
        data = read_csv_file(filename)

    elif filename.endswith("txt"):
        data = read_text_file(filename)

    return data

def read_text_file(filename):

    try:
        with open(filename, 'r') as fp:
            data = fp.read()

    except FileNotFoundError:
        print(f"File {filename} not found.")
        exit()

    return data

def read_csv_file(filename):

    data = []

    try:
        with open(filename, 'r') as fp:
            reader = csv.reader(fp, delimiter = ",")
            for line in reader:
                print(line)
                data.append(line)

    except FileNotFoundError:
        print(f"File {filename} not found")
        exit()

    return data

if __name__ == "__main__":

    try:
        filename = sys.argv[1]

    except IndexError:
        print(f"Usage: python fileio.py <filename>")

    # data = read_text_file(filename)
    data = read_data(filename)
    print(data)
