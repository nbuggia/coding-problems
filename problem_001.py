# Date: Nov 17, 2018
#
# Given a list of numbers and a number k, return whether any two numbers from 
# the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return 
# true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

l = [10, 15, 3, 7]
k = 17
matchFound = False

print(f"Inputs: \n\tlist: {l}\n\tk: {k}\n")

# Create two indexes iterating through the list twice so we can compare all 
#   the items with each otherq
for i, numberOne in enumerate(l):
    
    # stop running through the list if we've found a match. This will prevent us
    #   from finding the match twice. 
    if matchFound == True:
        break
    
    for j, numberTwo in enumerate(l):
        
        # don't waste time comparing a number to itself. This can't be a valid
        #   solution because it only really appears in the list once
        if i == j:
            continue

        elif (numberOne + numberTwo) == k:
            print(f"Found it! list[{i}] + list[{j}] = {k}.\n")
            matchFound = True
            break

if matchFound == False:
    print(f"No dice, sorry :(\n")