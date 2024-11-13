# Starting numbers - can be 0, 1
num1 = 17
num2 = 25

# Growth rules
# Rule 1: Add the number of digits in the second-to-last number to the most recent number.
# Rule 2: If the last number has an odd number of digits, subtract the sum of its digits from the second-to-last number.
# Rule 3: If both the last two numbers end in the same digit, multiply their sum by 3.


def add_second_to_last(num1, num2):
    # Convert second to last number into a string so I can count the digits
    # Add the number of digits to the last number
    num1_str = str(num1)
    return num2 + len(num1_str)


def check_if_odd(num1, num2):
    # If so, add the sum of the digits to the second to last number
    # Create a list for each digit in the number
    # Convert the number into a string and then back to an interger
    num2_list_digits = [int(digit) for digit in str(num2)]
    # If the number of digits are odd, then return sum of the second-to-last number with the
    # sum of the digits

    return num1 - sum(num2_list_digits)


def check_last_digit(num1, num2):
    # Use index splicing to access the last digit for both numbers, after converting the numbers
    # to strings to check if they are the same, if so then add the sum and multiply the sum by
    # three
    return (num1 + num2) * 3


sequence = []
sequence.append(num1)
sequence.append(num2)

# Using a while loop to generate first N number of the sequence:

count = 0
n = 6
# Minus by 1 to control index, as index begins from 1, this will always be the most recent number

while count < n:
    # Important to include this inside the while loop so it continues to update as the sequence
    # grows
    length_sequence = len(sequence) - 1
    if str(sequence[length_sequence - 1])[-1:] == str(sequence[length_sequence])[-1:]:
        result = check_last_digit(
            sequence[length_sequence], sequence[length_sequence - 1])
        sequence.append(result)
        count += 1
    # Check if the most recent number has odd number of digits
    elif len(str(sequence[length_sequence])) % 2 != 0:
        result = check_if_odd(
            sequence[length_sequence - 1], sequence[length_sequence])
        sequence.append(result)
        count += 1
    else:
        result = add_second_to_last(
            sequence[length_sequence - 1], sequence[length_sequence])
        sequence.append(result)
        count += 1

print(sequence)
