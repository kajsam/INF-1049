
# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021

# This is Task 1 from Deloppgave 1.3 from Oblig 1 in INF-1049 at UiT
# Calculates the volume of a sylinder.

# import math library to access pi. could've imported only pi, but since there's so much candy 
# in here, I import the entire library as default. 
import math 

# create function with input parameters h, r
def volume(h, r): 
    """Formula to calculate volume of a sylinder
    h: height
    r: radius 
    """
    vol = math.pi * r**2 * h
    return vol

# only if this file is called from the terminal 
if __name__ == "__main__":

    # set parameter values
    h1 = 20 
    r1 = 15

    # make function call and return value
    V = volume(h1, r1)

    print(f"The volume of a sylinder with height {h1} and radius {r1} is {V:.3f}") # 3 decimals