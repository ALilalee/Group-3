# 3. Larger List
# Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists. Here are the steps:

# Define the function to accept two parameters for our two lists of numbers
# Check if the length of the first list is greater than or equal to the length of the second list
# If true, then return the last element from the first list. Otherwise, return the last element from the second list
# Write a function named larger_list that has two parameters named lst1 and lst2.

# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

# Use the below code snippet to start the problem:

# #Write your function here


# #Uncomment the line below when your function is done
# #print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

def larger_list(lst1, lst2) :
    if len(lst1) >= len(lst2) :
        return lst1[-1]
    else:
        return lst2[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

