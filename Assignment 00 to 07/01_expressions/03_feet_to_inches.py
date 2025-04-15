#Converts feet to inches.
inches_per_foot=12

def feet_to_inches():
    feet=float(input("Enter number of feet: "))
    inches: float = feet * inches_per_foot
    print(f"{feet} feet is equal to {inches} iches.")

if __name__ == '__main__':
    feet_to_inches()