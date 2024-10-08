# Lab Exercise 1: Square of Odd Integers
# Features: Takes a list of integers and creates a new list with the square of only the odd elements.
# Procedure:
# 1. Use list comprehension to compute the square of odd integers from a given list.
# 2. Return the new list containing the squared odd integers.

def square_of_odds(lst):
    """Return a list with the square of odd integers from the input list.

    Args:
        lst (list of int): The list of integers to process.

    Returns:
        list of int: A new list containing the square of only the odd integers.
    """
    return [item ** 2 for item in lst if isinstance(item, int) and item % 2 != 0]

# Sample lists for testing the function
list_1 = [2, 4, 3]
list_2 = [0, 0, 1, 1]

# Print the result of squaring the odd numbers in the sample lists
print("Squared odd numbers from list_1:", square_of_odds(list_1))
print("Squared odd numbers from list_2:", square_of_odds(list_2))
