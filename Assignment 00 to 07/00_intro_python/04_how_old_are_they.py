def age_riddle():
    age_of_anthon=21
    age_of_beth=age_of_anthon+6
    age_of_chen=age_of_beth+20
    age_of_drew=age_of_anthon+age_of_chen
    age_of_ethan=age_of_chen
    print(f"Anthon is {age_of_anthon}")
    print(f"Beth is {age_of_beth}")
    print(f"Chen is {age_of_chen}")
    print(f"Drew is {age_of_drew}")
    print(f"Ethan is {age_of_ethan}")
if __name__ == '__main__':
    age_riddle()