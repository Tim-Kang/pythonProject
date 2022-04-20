# defining variables
P = float(input('Enter the given pressure in mmHg: '))
x1 = float(input('Enter the mole fraction of component 1: '))
print('Enter the Antoine Constants A, B, C for component 1: ')
A1 = float(input('A1: '))
B1 = float(input('B1: '))
C1 = float(input('C1: '))
print('Enter the Antoine Constants A, B, C for component 2: ')
A2 = float(input('A2: '))
B2 = float(input('B2: '))
C2 = float(input('C2: '))
T = float(input('Guess Temperature: '))
# calculating the bubble point temperature
exp = x1 * (10 ** (A1 - B1 / (T+C1))) + (1 - x1) * (10 ** (A2 - B2 / (T+C2))) - P

while abs(exp) > 0.01:
    exp = x1 * (10 ** (A1 - B1 / (T + C1))) + (1 - x1) * (10 ** (A2 - B2 / (T + C2))) - P
    if exp > 0:
        T -= 0.001
    else:
        T += 0.001
else:
    print("Bubble Point Temperature: " + str(T))
    print("Component 1 Vapor Pressure: " + str(10 ** (A1 - B1 / (T + C1))))
    print("Component 2 Vapor Pressure: " + str(10 ** (A2 - B2 / (T + C2))))














