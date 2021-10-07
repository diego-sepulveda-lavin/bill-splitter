guests = []

while True:
    name = input()
    if name == "":
        print("Please enter a valid name")
    elif name == ".":
        break
    else:
        guests.append(name)

print(guests)
print(len(guests))
