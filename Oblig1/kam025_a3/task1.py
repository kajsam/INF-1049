
# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021

# import math library 
import math 

# create function with input parameters h, r
def volume(h, r): 
    """Formula to calculate volume
    h: height
    r: radius 
    """
    vol = math.pi * r**2 * h
    return vol

# only if this file is called from the terminal?
if __name__ == "__main__":

    # set parameter values
    h1 = 20 
    r1 = 15

    # make function call
    V = volume(h1, r1)

    print(f"The volume is {V: .3f}") # 3 decimals