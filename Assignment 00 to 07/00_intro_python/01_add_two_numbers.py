#Write a Python program that takes two integer inputs from the user and calculates their sum.
def sum_two_numbers():
    print("This is a Python program to calculate the sum of two numbers.")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    total = a + b
    print(f"The sum of your given two numbers is {total}.")

if __name__ == '__main__':
    sum_two_numbers()
