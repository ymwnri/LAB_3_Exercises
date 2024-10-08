# Lab Exercise 2: Create List of Tuples
# Features: Takes two lists of equal length and creates a new list of tuples by pairing corresponding elements.
# Procedure:
# 1. Define two lists of equal length.
# 2. Use list comprehension to pair elements from both lists into tuples.
# 3. Return the resulting list of tuples.

# Define two lists
list_1 = [1, 2, 3]
list_2 = ["Aidan", "John", "Pork"]

# Create a list of tuples by pairing elements from both lists using list comprehension
list_of_tuple = [(item1, item2) for item1, item2 in zip(list_1, list_2)]

# Print the resulting list of tuples
print("Resulting list of tuples:", list_of_tuple)
