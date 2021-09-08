# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021

import sys


def mean(x):
    """Function that calculates the mean from a list."""

    if isinstance(x, list):
        try:
            s = sum(x)
            n = len(x)
            m = s/n

        except ValueError:
            print(f"It's a list alright, but some of the elements are of weird types.")
            exit()

    else:
        print(f"This functions demands a list.")

    return m

def variance(x):
    """Function that calculates the variance from a list."""

    mx = mean(x) # call the mean function

    dev_x = [elem - mx for elem in x] # calculate the deviations from the mean

    sq_dev_x = [elem**2 for elem in dev_x] # square the deviations

    var_x = sum(sq_dev_x)/(len(x)-1) # sum the squared deviations and divide by n-1

    return var_x

def std_dev(x):

    from math import sqrt

    var_x = variance(x)

    std_dev_x = sqrt(var_x)

    return std_dev_x



# only if this file is called from the terminal?
if __name__ == "__main__":

    print("A statistic, Y, is a random variable defined as a real-valued or vector-valued function, T(), \
of a random sample (X_1, ..., X_n): Y = T(X_1, ..., X_n)")

    # declare a list
    x1 = [1, 8, 3]

    print(f"For the observations {x1}")

    m_x = mean(x1)

    print(f"the mean is {m_x}")

    var_x = variance(x1)

    print(f"the variance is {var_x: .2f}")

    std_dev_x = std_dev(x1)

    print(f"the standard deviation is {std_dev_x: .2f}")

    

    

    

    
