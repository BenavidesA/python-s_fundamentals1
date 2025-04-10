"""
elements to create a variable:
- name: str
- type: str
- value: str

#rules to name a variable:
    # The name of the variable must consist of uppercase letters, lowercase letters, digits, and the underscore (_) character.
    # The name of the variable must begin with a letter.
    # The underscore (_) character is considered a letter.
    # Uppercase and lowercase letters are treated differently (e.g., "Alice" and "ALICE" are different variable names in Python).
    # Variable names cannot be the same as any of Python's reserved keywords (keywords will be explained later).
#nomenclature:
    # Variable names should be in lowercase, with words separated by underscores to improve readability (e.g., var, my_variable)
    # Function names follow the same convention as variable names (e.g., fun, my_function)
    # MixedCase names (e.g., myVariable) are also possible but should only be used in contexts where that style is already predominant, to maintain backward compatibility with the adopted convention.
"""

# Variable declaration and assignment
# Variable declaration is the process of creating a variable and assigning it a value.
# In Python, variable declaration and assignment are done in a single step.
# The syntax is as follows:
# variable_name = value
# For example:
my_variable = 5
print("the value of \"my_variable\" is : ", my_variable)  # Output: 5