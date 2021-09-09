
# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021

# This is Task 2 from Deloppgave 1.3 from Oblig 1 in INF-1049 at UiT
# Sorts elements of a list according to type.


############ This is from stackoverflow and a bit on the side ########################
from typing import Iterable # it is for the flatten function that I found on stackoverflow

def flatten(items):
    """Yield items from any nested iterable. This I found here
    https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x
###################### end stackoverflow function ###################################

# define function, one argument
def list_fun(liste): 
    """Function that sorts the elements of a list according the following types:
    int, float, string, complex
    and returns four lists.
    Any other type is disregarded with a friendly warning.
    Elements that are lists have a special warning. 
    """

    int_list = [] # empty list of integers
    float_list = [] # empty list of floats
    str_list = [] # empty list of strings
    complex_list = [] # emptly list of complex's

    for elem in liste: # iterate through the list
        if isinstance(elem, int): # if the current element is an integer
            int_list.append(elem) # add it to the list

        elif isinstance(elem, float): # if the current element is a float
            float_list.append(elem) # add it to the list

        elif isinstance(elem, str): # if the current element is a string
            str_list.append(elem) # add it to the list

        elif isinstance(elem, complex): # if the current element is a complex
            complex_list.append(elem) # add it to the list

        elif isinstance(elem, list): # if there is a list within the list
            print(f"Your list contains a list, {elem}, that will be disregarded. \
I could flatten it, but I won't.")
        else:
            typ = type(elem).__name__
            print(f"The element {elem} is a {typ} and is disregarded.")

    return int_list, float_list, str_list, complex_list

# only if this file is called from the terminal
if __name__ == "__main__":

    # trying four different lists
    list1 = ['s', [2, 4.0, 's', [5j], (3, 4), 0j]]

    list2 = [2, 4, 's', [5j]]

    sublist = [2, 4.0, 's', [5j], (3, 4), 0j]

    flatlist = list(flatten(list1)) # demonstrating the stackoverflow function

    # make function call
    integers, floats, strings, complexes = list_fun(sublist)

    print(f"Integers: {integers} \nFloats: {floats} \nStrings: {strings} \nComplex's: {complexes}")