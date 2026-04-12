import math
a = float(input("Enter the length of the first leg: "))
b = float(input("Enter the length of the second leg: "))
c = math.sqrt(pow(a, 2) + pow(b, 2)) 
print(f"The length of the hypotenuse is: {c}")