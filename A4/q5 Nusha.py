# Combine Sort Finally, let’s create a function that combines two different lists together and then 
# sorts them. To do this we can combine the lists with an operation and then sort using a function call. 
# Here are the steps we need to use:
# Define the function to accept two parameters, one for each list. Combine the two lists together Sort 
# the result Return the sorted and combined list Write a function named combine_sort that has two 
# parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result. Return the new 
# sorted list.
new_list=[]
def combine_sort(lst1, lst2):
    new_list=sorted(lst1+lst2)
print (new_list)