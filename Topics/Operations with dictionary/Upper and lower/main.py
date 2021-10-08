# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
my_dict = {key.upper(): key.lower() for key in some_iterable}

print(my_dict)
