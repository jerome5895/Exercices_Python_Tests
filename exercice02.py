import sys

# Function to determine the smaller number of a list 
def smaller(numbers):
    for i in numbers:
        index = i
        for j in numbers:
            if numbers[j] < numbers[index]:
                index = j
                numbers[i], numbers[index] == numbers[index], numbers[i]
    return numbers[index]

# Globales variables
numbers = [int(numbers) for numbers in sys.argv[1]]

# Resolution
result = smaller(numbers)

# Print out result
print(result)