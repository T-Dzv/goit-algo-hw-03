import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
    # excluding not valid arguments: min should be >=1, max should be <= 1000. 
    # also we excluded cases when min is larger then max and when 
    # min-max difference won't allow us generate needed quantity of unique numbers
    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return numbers
    else:
        # convirting list to set to genarate only unique numbers
        unique_numbers = set(numbers)
        # in each loop function will generate random number in a range. 
        # Loop will continue until there will be required quantity of unique numbers in a set
        while len(unique_numbers) < quantity:
            number = random.randint(min, max)
            unique_numbers.add(number)
        # converting set back to list and sorting it
        numbers = list(unique_numbers)
        numbers.sort()
        return numbers
    
#test cases. Uncomment to check. Run second test case 3 times to make sure it works correctly (unique numbers and sorted)

# print(get_numbers_ticket(1, 3, 3)) # should return a list [1, 2, 3]
# print(get_numbers_ticket(1, 100, 10)) # should return a list with 10 sorted unique numbers
# print(get_numbers_ticket(-5, 100, 5)) # should return empty list
# print(get_numbers_ticket(100, 1001, 5)) # should return empty list
# print(get_numbers_ticket(100, 10, 5)) # should return empty list
# print(get_numbers_ticket(1, 5, 10)) # should return empty list
