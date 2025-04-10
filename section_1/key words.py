print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

# Using keyword arguments in the print() function.
# 'end' is a keyword argument that defines what to print at the end of the output.
# Syntax: keyword=value (e.g., end=" ").
# Keyword arguments must come after positional arguments.
 
# Using the 'sep' keyword argument in the print() function.
# 'sep' defines the string used to separate the arguments in the output.

print("My", "name", "is", "Monty", "Python.", sep="-")  # Using a hyphen as the separator.

# Output:
# My-name-is-Monty-Python.

# Note: The 'sep' argument can also be an empty string.
print("My", "name", "is", "Monty", "Python.", sep="")  # No separator between arguments.

# Output:
# MynameisMontyPython.

print("My", "name", "is", "Monty", "Python.", sep=" ")  # Using a space as the separator.
# Output:
# My name is Monty Python.

