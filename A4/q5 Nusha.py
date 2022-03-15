# 5. Combine Sort
# Finally, let’s create a function that combines two different lists together and
#  then sorts them. To do this we can combine the lists with an operation and then
#  sort using a function call. Here are the steps we need to use:

# Define the function to accept two parameters, one for each list.
# Combine the two lists together
# Sort the result
# Return the sorted and combined list
# Write a function named combine_sort that has two parameters named lst1 and lst2.

# The function should combine these two lists into one new list and sort the result.
#  Return the new sorted list.

# Use the below code snippet to start the problem:


def combine_sort(lst1, lst2):
    new_list = sorted(lst1 + lst2)
    return new_list
print (combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

