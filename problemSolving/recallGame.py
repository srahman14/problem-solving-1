import random
import numpy as np
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Get grid size and ensure it's between 3 and 10
n = 0
while n < 3 or n > 5:
    n = int(input("Enter the grid size 3-10: "))
n_max = n * n

# Defining sets with repeated symbols to compensate for values of n > 3
setA = [1, 2, 3, 4, 5, 6, 7, 8, 9] * (n_max // 10 + 1)
setB = ['١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩'] * (n_max // 10 + 1)

# Splice the sets to get up to the minimum amount of elements needed and shuffle the values
setA = setA[:n_max]
setB = setB[:n_max]

print(setA)
print(setB)

# Get a copy of original sets which will be used to save original sets
# This is useful to compare matching pairs using index of elements
originalSetA = setA.copy()
originalSetB = setB.copy()

random.shuffle(setA)
random.shuffle(setB)

# Converting sets into matrices using numpy
setA_matrix = np.array(setA).reshape(n, n)
setB_matrix = np.array(setB).reshape(n, n)

# Create the asterisks to fill the matrix using numpy
displayA = np.full((n, n), "  *  ")
displayB = np.full((n, n), "  *  ")

# Start
# To track how many positions correctly guessed
guessed = 0
# To track all correctly guessed choices
guessedChoices = []

# while True:
#     print(setA_matrix)
#     print(setB_matrix)
#     # Base case if all positions guessed:
#     if guessed / 2 == n_max:
#         break

#     time.sleep(1.3)
#     print("\nSet A:")
#     print(displayA)
#     print("\nSet B:")
#     print(displayB)

#     # Ask the user of the choices
#     x1, y1 = map(int, input("Enter your choice: (row, col) ").split())

#     if (x1 > n) or (y1 > n):
#         print(Fore.YELLOW +
#               f"This position is out of bounds! Max (row), (col) is {n}")
#         print(Fore.RED + f"You entered: {x1}, {y1}")
#         time.sleep(1)
#         continue

#     x2, y2 = map(int, input("Enter your choice: (row, col) ").split())

#     if (x2 > n) or (y2 > n):
#         print(Fore.YELLOW +
#               f"This position is out of bounds! Max (row), (col) is {n}")
#         print(Fore.RED + f"You entered: {x2}, {y2}")
#         time.sleep(1)
#         continue

#     # Subtract 1 from all entries as python lists are zero-indexed
#     x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

#     # Attain the actual value of the choice the user selected
#     choice1 = setA_matrix[x1, y1]
#     choice2 = setB_matrix[x2, y2]

#     # Check if position
#     if (x1, y1) in guessedChoices or (x2, y2) in guessedChoices:
#         print(Fore.YELLOW + "These positions have already been guessed correctly!")
#         continue

#     # Reveal their guesses
#     print(Fore.YELLOW + "Guess 1: ", choice1)
#     print(Fore.YELLOW + "Guess 2: ", choice2)
#     time.sleep(1.3)

#     # Set the asterisks matrice at position x1, y2 ... to correspond to the guesses
#     displayA[x1, y1] = "  " + str(choice1) + "  "
#     displayB[x2, y2] = "  " + str(choice2) + "  "

#     # Print the positions briefly
#     print("\nSet A:")
#     print(displayA)
#     print("\nSet B")
#     print(displayB)

#     # Use the actual value to compare the indexes of the choices from the original sets
#     # They are expected to be the same if true
#     indexA = originalSetA.index(choice1)
#     indexB = originalSetB.index(choice2)

#     # Compare if they are the same
#     if indexA == indexB:
#         # If they are the same then update the guessing matrix
#         displayA[x1, y1] = f"  {str(choice1)}  "
#         displayB[x2, y2] = f"  {str(choice2)}  "
#         print(Fore.GREEN + f"\n {choice1} and {choice2} are matches!")
#         guessedChoices.append((x1, y1))
#         guessedChoices.append((x2, y2))
#         guessed += 1
#     else:
#         # Reset the asterisks matrice back to original since the values did not match
#         displayA[x1, y1] = "  *  "
#         displayB[x2, y2] = "  *  "
#         print(Fore.RED + f"\n {choice1} and {choice2} are not matches.")
