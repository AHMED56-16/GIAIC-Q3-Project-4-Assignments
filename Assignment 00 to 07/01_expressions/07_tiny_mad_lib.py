#Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def mad_libs():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    sentence = f"The {adjective} {noun} loves to {verb} in the class!"
    print(sentence)
if __name__ == '__main__':
    mad_libs()