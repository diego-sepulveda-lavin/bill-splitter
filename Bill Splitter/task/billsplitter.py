# write your code here
try:
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

        print("Enter the total bill value:")
        bill_total = int(input())
        bill_per_person = round(bill_total / people_qty, 2)

        for person in people:
            people[person] = bill_per_person
        print(people)
except ValueError:
    print("Please enter a valid number")
