# Kajsa Mollersen (kajsa.mollersen@uit.no)
# September 2021
# INF-1049
# Oblig 2.1

# Task 1 b)

import Module_1 # faktisk kjore koden

# from Module_1 import conversation # importing the function conversation from the file Module_1

if __name__ == "__main__":

    # Module_1.conversation()

    print("\nWith proper use of name-equals-main, we can control what is imported and what is not.")
    print("Everything inside name-equals-main will only be executed when the module is called.")
    print("Everyhting else will be executed also when the module is imported.")

    # print(Module_1.x_y(8))