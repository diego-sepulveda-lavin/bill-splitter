# write your code here
print("Enter the number of friends joining (including you):")
people_qty = int(input())
people = {}

if people_qty < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(people_qty):
        name = input()
        people[name] = 0
    print(people)
