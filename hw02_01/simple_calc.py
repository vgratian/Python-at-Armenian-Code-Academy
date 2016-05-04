# Simple Calculator capable only of one simple calculation
# Accepted input format: integer operator integer (divided by space!)
# Accepted operators: '+', '-', '*', '/'.

string_input = raw_input('Hi, I am Simple Calc 1.0 \nHow can I help you? \n')

# Splits input into 3 elements (integer operator integer)
split_string = string_input.split()

# Identifies operator and prints result of calculation
if split_string[1] == '+':
    print int(split_string[0]) + int(split_string[2])
elif split_string[1] == '-':
    print int(split_string[0]) - int(split_string[2])
elif split_string[1] == '*':
    print int(split_string[0]) * int(split_string[2])
elif split_string[1] == '/':
    print int(split_string[0]) / int(split_string[2])
else:
    print 'Error, invalid operator "' + split_string[1] + '" not recognized'
