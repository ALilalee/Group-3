# For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:

# Define the function to accept one parameter for our list
# Get the length of the list
# Append the length of the list to the end of the list
# Return the modified list
# Create a function called append_size that has one parameter named lst.

# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

# For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.

# Use the below code snippet to start the problem:

#Write your function here

def append_size(lst):                
    lst.append(len(lst))
    return lst
print(append_size([23, 42, 108]))

