# TypeCasting is the process of converting a variable from one type to another. In Python, you can use built-in functions to perform type casting. (str(), int(), float(), etc.)

# Example of type casting:
Name = "John"
Age = 30
Is_Teacher = True
gpa = 3.5

# Converting variables to different types
new_Gpa = int(gpa)  # Converts float to int
print(new_Gpa)  # Output: 3

# The code below will raise an error. 
new_Name = float(Name)
print(new_Name)  # This will raise a ValueError because "John" cannot be converted to a float
