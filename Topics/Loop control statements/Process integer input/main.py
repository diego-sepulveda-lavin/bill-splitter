# put your python code here
lower_limit = 10
higher_limit = 100

while True:
    number = int(input())
    if number < lower_limit:
        continue
    elif number > higher_limit:
        break
    else:
        print(number)
