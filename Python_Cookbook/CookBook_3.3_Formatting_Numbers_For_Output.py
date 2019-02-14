"""
Problem
You need to format a number for output, controlling the number of digits, alignment,
inclusion of a thousands separator, and other details.
"""

# Solution
# To format a single number for output, use the built-in format() function.

x = 1234.56789
print(format(x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))

# Left justified in 10 chars, two-digit accuracy
print(format(x, '<10.2f'))

# Centered justified in 10 chars, three-digit accuracy
print(format(x, '^10.3f'))

# Inclusion of thousands separator
print(format(x, ','))
print(format(x, '0,.2f'))

# If you want to use exponential notation, change the f to an e or E, depending on the
# case you want used for the exponential specifier.
print(format(x, 'e'))
print(format(x, '0.2E'))

# The general form of the width and precision in both cases is '[<>^]?width[,]?(.dig
# its)?' where width and digits are integers and ? signifies optional parts.

print('The value is {:0,.2f}'.format(x))

swap_separators = {ord('.'):',', ord(','):'.'}
print(format(x, ',').translate(swap_separators))
