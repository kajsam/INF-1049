import sys

def avg(s, n):
    return s / n

if __name__ == "__main__":

    try:
        s = float(input("Sum: "))
        n = float(input("Number of elements: "))

    except ValueError:
        print(f"Something wrong with input.")
        exit()

    try:
        avg(s,n)
    
    except ZeroDivisionError:
        print("Division by zero")
        exit()

 #   for l in n:
 #       if ord(l) < 48 or ord(l) > 57:
 #           if ord(l) != 46:
 #               print(f"Argument contains invalid character: {l}")
 #               exit()

# try: 
#    b = float("Hello")
#    23/b
# except Exception as e:
#    print(f"You generated an {type(e).__name__ }-> {e}")

# try: 
#    b = float(0)
#    23/b
# except ValueError as e:
#     print(f"You generated an {type(e).__name__ }-> {e}")
# except ZeroDivisionError as z:
#    print(f"You generated an {type(z).__name__ }-> {z} \n")
#    print("You divided by zero.")