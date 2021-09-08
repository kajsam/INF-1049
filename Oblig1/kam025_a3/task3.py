# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021

import sys

def f_split(x):
    """A mathematical function"""

    try: 
        if x <= 5:
            fx = 3 * x + 1
        else:
            fx = 3 * x**2 + 6
    except TypeError:
        typ = type(x).__name__
        print(f"The function does not accept input of type {typ}")
        exit()
        
    return fx

# only if this file is called from the terminal?
if __name__ == "__main__":

    # input parameter
    x1 = float(sys.argv[1])
    
    f_x = f_split(x1)

    print(f"f({x1}) = {f_x}") # but how to return it to the terminal, I don't know
