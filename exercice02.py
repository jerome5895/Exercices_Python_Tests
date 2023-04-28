import sys

# Function to determine the smaller number of a list 
def smaller(list):
    for i in list:
        index = i
        for j in list:
            if list[j] < list[index]:
                index = j
                list[i], list[index] == list[index], list[i]
    return list[index]

# Globales variables
list = [int(list) for list in sys.argv[1]]

# Resolution
result = smaller(list)

# Print out result
print(result)