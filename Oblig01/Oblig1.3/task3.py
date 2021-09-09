# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021

# This is Task 3 from Deloppgave 1.3 from Oblig 1 in INF-1049 at UiT
# Calculates the value of a function, accepts argument from the terminal. Returns function value. 

# importing the sys library to take input arguments from the terminal
import sys 

# in the function I'm including try-except, just for the fun of it. 

def f_split(x):
    """A mathematical function, discontinuous at x -> 5 from above."""

    try: 
        if x <= 5: 
            fx = 3 * x + 1
        else:
            fx = 3 * x**2 + 6
    except TypeError: # this error occurs if the input x is not a real number (int/float/...)
        typ = type(x).__name__
        print(f"The function does not accept input of type {typ}")
        exit()
        
    return fx # the value of f(x) is returned

# only if this file is called from the terminal
if __name__ == "__main__":

    # input parameter
    x1 = float(sys.argv[1]) #
    
    f_x = f_split(x1)

    print(f"f({x1}) = {f_x}") 
