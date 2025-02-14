def calculate_resistance(rho, length, area):
    return (rho * length) / area

def calculate_inductance(XL, f):
    return XL / (2 * 3.1416 * f)

def calculate_capacitance(area, distance):
    epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)
    return (epsilon_0 * area) / distance

# Taking input for resistor parameters
print("Enter resistor parameters:")
rho = float(input("Enter value of rho: "))
length = float(input("Enter length l: "))
area = float(input("Enter area A: "))

# Taking input for inductor parameters
print("\nEnter inductor parameters:")
f = float(input("Enter frequency f: "))
XL = float(input("Enter XL: "))

# Taking input for capacitor parameters
print("\nEnter capacitor parameters:")
f_cap = float(input("Enter frequency: "))
area_cap = float(input("Enter area of plates: "))
distance_cap = float(input("Enter distance between plates: "))

# Calculating values
resistance = calculate_resistance(rho, length, area)
inductance = calculate_inductance(XL, f)
capacitance = calculate_capacitance(area_cap, distance_cap)

# Displaying results
print(f"\nResistance = {resistance:.6f} ohm's")
print(f"Inductance = {inductance:.6f} Henry")
print(f"Capacitance = {capacitance:.6e} farad")
