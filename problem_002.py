# Date: Dec 12, 2018
#
# Given an array of integers, return a new array such that each element at index 
# i of the new array is the product of all the numbers in the original array 
# except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
# be [2, 3, 6].
# 
# Follow-up: what if you can't use division?

input = [3, 2, 1]
output = list()

print(f"Inputs: \n\tinput: {input}\n\t")

# Approach 1 (with division)
# Compute the product of all the numbers in the list
total = input[0]
for index, value in enumerate(input[1:len(input)]):
    total *= value

# Create a new list. Each element removes the product of input[index] from total 
for index, value in enumerate(input):
    output.append(total / input[index])

print(f"Output (using division): \n\toutput: {output}\n\t")

# Approach 2 (without division)
# todo 