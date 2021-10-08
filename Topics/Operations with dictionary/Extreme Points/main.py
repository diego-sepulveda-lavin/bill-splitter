from math import inf
# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
min_item = [None, inf]
max_item = [None, -inf]


for key, value in test_dict.items():
    if value < min_item[1]:
        min_item[1] = value
        min_item[0] = key
    if value > max_item[1]:
        max_item[1] = value
        max_item[0] = key


print("min:", min_item[0])
print("max:", max_item[0])
