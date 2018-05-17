# messy_list = [4, 2, 1, 3, 5]
# slices work with start index: end index but don't include the value of the end index
# slices return a list
# to get first position it would be messy_list[0:1] which returns [4]
# .sort() sorts in ascending order ; add reverse=True sorts it in descending order

# messy_list.sort(reverse=True)
# print(messy_list)

numbers = list(range(20))
num = [1, 2, 3, 4, 5]
# range returns a range object
print(numbers)

# 3 pieces to a slice start:stop:step -1 step allows you to reverse a list
# to print even numbers
print(numbers[::2])
print(numbers[2::2])


# get first 4 and last 4 items of an iterable
def first_and_last_4(le_list):
    print(le_list[0:4] + le_list[-4:])


# Make a function named reverse_evens that accepts a single iterable as an argument.
# Return every item in the iterable with an even index...in reverse.
# For example, with [1, 2, 3, 4, 5] as the input, the function would return [5, 3, 1]

def reverse_evens(le_list):
    if len(le_list) % 2 == 0:
        print(le_list[-2::-2])
    else:
        print(le_list[-1::-2])

reverse_evens(num)

# This one will be named sillycase and it'll take a single string as an argument.
# sillycase should return the same string; first half should be lowercased and the second half should be uppercased

def sillycase(single_string):
    halfway_point = len(single_string)//2
    return (single_string[:halfway_point]).lower() + (single_string[halfway_point:]).upper()


sillycase("Treehouse")
