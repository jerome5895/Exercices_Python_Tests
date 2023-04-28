import sys

# Function to determine the smaller 
def smaller(numbers):
    for i in numbers:
        small = i
        for j in numbers:
            if numbers[j] <= numbers[i]:
                j == small
    return small

# Globales variables
numbers = sys.argv[1]

# Print out result
smaller(numbers)