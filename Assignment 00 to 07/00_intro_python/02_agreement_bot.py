#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!"
def favorite_animal():
    animal = input("What is your favorite animal? ")
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    favorite_animal()

