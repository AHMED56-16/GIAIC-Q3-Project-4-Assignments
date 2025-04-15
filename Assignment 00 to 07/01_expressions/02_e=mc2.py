C: int = 299792458  

def mass_to_energy():
    mass_in_kg: float = float(input("Enter mass in kg  to have its equivalent energy in joules : "))
    energy_in_joules: float = mass_in_kg * (C ** 2)
    print(f"{energy_in_joules} Joules of energy!")
if __name__ == '__main__':
    mass_to_energy()