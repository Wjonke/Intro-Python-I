"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""
import operator

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
# Way 1
x = slice(1, 2)
print(a[x])


# Way 2
def convert(the_list):
    return tuple(i for i in the_list)


x = slice(1, 2)
tuple_list = convert(a)
print(tuple_list[x])

# Way 3
print(operator.itemgetter(1)(a))

# Output the second-to-last element: 9
# Way 1
x = slice(len(a) - 2, len(a) - 1)
print(a[x])

# Way 2
print(operator.itemgetter(-2)(a))

# Output the last three elements in the array: [7, 9, 6]
# Way 1
x = slice(len(a) - 3, len(a))
print(a[x])

# Way 2
print(list(operator.itemgetter(-3, -2, -1)(a)))





# Output the two middle elements in the array: [1, 7]
#will also return middle element of length is odd
mid_index = int(len(a) / 2)
print("mid_index", mid_index)

if len(a) % 2 == 0:
    x = slice(mid_index - 1, mid_index +1)

elif len(a) % 2 != 0:
    x = slice(mid_index, mid_index +1)

print("middle of the list ---->", a[x])



# Output every element except the first one: [4, 1, 7, 9, 6]

x = slice(1, len(a))
print(a[x])


# Output every element except the last one: [2, 4, 1, 7, 9]
x = slice(0, len(a)-1)
print(a[x])


# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print()
