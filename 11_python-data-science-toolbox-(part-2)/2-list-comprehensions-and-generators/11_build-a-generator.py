'''
11 - Build a generator

In previous exercises, you've dealt mainly with writing generator expressions, which uses
comprehension syntax. Being able to use comprehension syntax for generator expressions made
your work so much easier!

Now, recall from the video that not only are there generator expressions, there are generator
functions as well. Generator functions are functions that, like generator expressions, yield
a series of values, instead of returning a single value. A generator function is defined as
you do a regular function, but whenever it generates a value, it uses the keyword yield
instead of return.

In this exercise, you will create a generator function with a similar mechanism as the
generator expression you defined in the previous exercise:

lengths = (len(person) for person in lannister)

Instructions:

- Complete the function header for the function get_lengths() that has a single parameter,
  input_list.

- In the for loop in the function definition, yield the length of the strings in input_list.

- Complete the iterable part of the for loop for printing the values generated by the
  get_lengths() generator function. Supply the call to get_lengths(), passing in the list lannister.
'''
# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)
        
# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)
