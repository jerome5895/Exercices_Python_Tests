import sys

# Function to determine the smaller 
def smaller(numbers):
    for i in numbers:
        index = i
        for j in numbers:
            if int(numbers[j]) < int(numbers[index]):
                index = j
                numbers{i}, numbers{index} == numbers{index}, numbers{i}
    return 

# Globales variables
numbers = sys.argv[1]

# Print out result
result = smaller(numbers)

# Print out result
print(result)