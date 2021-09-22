# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

# Task 1 a)

import random #pseudo-random number generator

def conversation(): # define a function

    """Ada gives a prediction for three colours, starting with uppercase or lowercase.
       For any other input, Ada asks for a positive integer. 
       If the user provides a non-positive integer, Ada asks again. 
       If the user still provides a non-positive integer, she quits. 
    """

    print("Ada: Hi! My name is Ada, and I am a fortune teller.") # Ada Lovelace
    print("Ada: Tell me, what is your favourite colour?")
    col = input() # User input

    if col == "red" or col == "Red":
        print("Ada: Look out for a big suprise this weekend.")
    elif col == "blue" or col == "Blue":
        print("Ada: By tomorrow night, something good will happen.")
    elif col == "green" or col == "Green":
        print("Ada: A ghost from the past will come back and hunt you.")
    else:
        print("Ada: Tell me more. What is your favourite positive integer?")
        number = int(input())
        if number < 1: # this is not a positive integer
            print("Ada: I asked for a positive integer. Try again:")
            number = int(input())
            if number < 1: # still not a positive integer
                print("Ada: You're not cooperating. I quit!")
                exit() # exit the function


        random.seed(number) # set random seed

        new_number  = random.randrange(0,number) # sample a new number

        print(f"Ada: {number} is a great one, but I recommend you to change to {new_number} which is even better!")


print("kajsa")

def x_y(x):
    y = x
    return y

if __name__ == "__main__": # does not run when imported

    conversation()
    print(x_y(4))