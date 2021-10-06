# put your python code here
total_sum = 0
squares_sum = 0

while True:
    try:
        number = int(input())
    except ValueError:
        print("Please enter a valid number")
        break
    total_sum += number
    squares_sum += number ** 2
    if total_sum == 0:
        break


print(squares_sum)
