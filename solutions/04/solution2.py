"""
Advent of Code 2019
Day 4: Secure Container

AKA Elvish Password Fiasco

Gist:
- Passwords work like this
- 1. is 6 digit number
- 2. at least two adjacent digits are same
- 3. always increasing
+ 4. rule 2 needs to be exactly two

"""

INPUT_MIN = 197487
INPUT_MAX = 673251

def is_six_digits(password):
    """ Useless function given input, but do it anyway """
    return len(password) == 6

def has_adjacent_digit(password):
    """ ^that """
    number_count = {}
    for digit in password:
        number_count[digit] = number_count.get(digit, 0) + 1
    for digit in number_count:
        if number_count[digit] == 2:
            return True
    return False

def is_always_increasing(password):
    """ Always increasing by digits """
    last_num = password[0]
    index = 1
    while index < len(password):
        if last_num > password[index]:
            return False
        last_num = password[index]
        index += 1
    return True

def solve():
    """ Solve the puzzle """
    valid_password_count = 0
    current_input = INPUT_MIN
    while current_input <= INPUT_MAX:
        password = str(current_input)
        if (has_adjacent_digit(password) and
                is_six_digits(password) and
                is_always_increasing(password)):
            valid_password_count += 1
            print(password, "YEP")
        else:
            print(password, "NOPE")
        current_input += 1
    print(valid_password_count)

solve()
