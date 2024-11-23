# Starting numbers - can be 17, 25
num1 = 17
num2 = 25

# Growth rules
# Rule 1: If both numbers end with the same digit,
# from the second-to-last number.
# multiply the number of digits in the second-to-last number to the most recent number.
# Rule 2: If the last number has an odd number of digits, add the square of the sum of its digits
# from the second-to-last number.
# Rule 3: If none of these conditions are met, then multiply the sum of the two numbers by 2


sequence = []
sequence.append(num1)
sequence.append(num2)

# Using a while loop to generate first N number of the sequence:

count = 0
n = 8
# Minus by 1 to control index, as index begins from 1, this will always be the most recent number

while count < n:
    # Important to include this inside the while loop so it continues to update as the sequence
    # grows
    length_sequence = len(sequence) - 1
    # If the last digits of both two numbers are the same
    if str(sequence[length_sequence - 1])[-1:] == str(sequence[length_sequence])[-1:]:

        num1_str = str(sequence[length_sequence])
        result = sequence[length_sequence - 1] * len(num1_str)
        sequence.append(result)
        count += 1
    # Check if the most recent number has odd number of digits
    # if the length of the digits is not even of the newest number is not even
    elif len(str(sequence[length_sequence])) % 2 != 0:
        num2_list_digits = [int(digit)
                            for digit in str(sequence[length_sequence - 1])]
        result = sequence[length_sequence] + (sum(num2_list_digits) ** 2)
        sequence.append(result)
        count += 1
    # If none of the previous 2 rules are met
    else:
        num1 = sequence[length_sequence - 1]
        num2 = sequence[length_sequence]
        result = (num1 + num2) * 2
        sequence.append(result)
        count += 1

print(sequence)
