# A string is a sequence of characters enclosed in quotes, while an integer is a whole number without quotes.
# A string can contain letters, numbers, and symbols, while an integer can only contain digits. 
# Strings are used when text needs to be processed (such as names of any kind, addresses, novels, etc.), not numbers.
# How can a quote be encoded within a string that is already delimited by quotes?
# Message:
# I like "Monty Python"
# Two possible solutions.

# The first solution uses the escape character (\):
print("I like \"Monty Python\"")

# The second solution uses apostrophes to delimit the string:
print('I like "Monty Python"')

# How can an apostrophe be inserted into a string that is delimited by two apostrophes?
# The answer is to use the escape character (\):
print('I\'m learning Python!') 
#or
print("I'm learning Python!")


