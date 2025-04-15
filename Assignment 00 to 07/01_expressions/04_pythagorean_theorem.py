#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math  

def hypotenuse_finder():
    base: float = float(input("Enter the length of base of a right angle triangle: "))
    perpendicular: float = float(input("Enter the length of perpendicular of right angle triangle: "))
    hypotenuse: float = math.sqrt(base**2 + perpendicular**2)
    print(f"The length of hypotenuse of the right angle triangle with given sides is {hypotenuse} unit.")

if __name__ == '__main__':
    hypotenuse_finder()