

import sting

def contains_digit(passw):
    return set(passw).difference(string.digits)

def contains_lowercase(passw):
    return set(passw).difference(string.armscii_lowercase)

def contains_uppercase(passw):
    return set(passw).difference(string.armscii_uppercase)

def contains_punctuation(passw):
    return set(passw).difference(string.punctuation)

def long_enough(passw):
    return True if len(passw) > 7 else False

passw_accepted = False
conditions = [contains_digit(passw), contains_lowercase(passw), contains_uppercase(passw), contains_punctuation(passw), long_enough(passw)]

while not passw_accepted:
    passw = input('Please enter password')

    if all(conditions):
        print('Password accepted.')
        passw_accepted = True
    else:
        print('Password must be 8 chars, contain digit, punctuation, lower & uppercase.')
