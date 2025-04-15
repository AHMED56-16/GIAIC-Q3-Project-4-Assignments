#Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
def remainder_and_quotient():
    dividend: int = int(input("Please enter a divided: "))
    divisor: int = int(input("Please enter a divisor: "))

    quotient: int = dividend // divisor 
    remainder: int = dividend % divisor 
    
    print(f"The quotient and remainder of your given numbers are {quotient} and {remainder} respectively.")

if __name__ == '__main__':
    remainder_and_quotient()