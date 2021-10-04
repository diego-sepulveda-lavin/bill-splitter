# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# your code here
final_groups = dict.fromkeys(groups)
groups_qty = int(input())

for i in range(groups_qty):
    children_qty = int(input())
    final_groups[groups[i]] = children_qty

print(final_groups)
