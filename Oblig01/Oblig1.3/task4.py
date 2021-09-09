# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021

# This is Task 4 from Deloppgave 1.3 from Oblig 1 in INF-1049 at UiT.
# Four functions to calculate statistics. Point being that they call each other.

import sys, math # just always import sys and math

def mean(x):
    """Function that calculates the mean from a list."""

    # checking that the input argument is a list
    if isinstance(x, list): 
        try:
            s = sum(x) # sum of all observations
            n = len(x) # number of observations (sample size)
            m_x = s/n # the sample mean

        except ValueError:
            print(f"It's a list alright, but some of the elements are of weird types.")
            exit()

    else:
        print(f"This functions demands a list.")
        exit() # seems like I need this exit, or else I'm trying to return m not declared

    return m_x

def variance(x):
    """Function that calculates the variance from a list."""

    mx = mean(x) # call the mean function, which then checks if the input x fits

    dev_x = [elem - mx for elem in x] # calculate the deviations from the mean

    sq_dev_x = [elem**2 for elem in dev_x] # square the deviations

    var_x = sum(sq_dev_x)/(len(x)-1) # sum the squared deviations and divide by n-1

    return var_x

def std_dev(x):

    var_x = variance(x)

    std_dev_x = math.sqrt(var_x)

    return std_dev_x

# only if this file is called from the terminal?
if __name__ == "__main__":

    print("A statistic, Y, is a random variable defined as a real-valued function, T(), \
of a random sample (X_1, ..., X_n): Y = T(X_1, ..., X_n)")

    # declare a list
    x1 = [1, 8, 3]

    print(f"For the observations {x1}")

    m_x = mean(x1)

    print(f"the mean is {m_x}")

    var_x = variance(x1)

    print(f"the variance is {var_x:.2f}")

    std_dev_x = std_dev(x1)

    print(f"the standard deviation is {std_dev_x:.2f}")

    

    

    

    
