total_sum = 0
total_numbers = 0

while True:
    try:
        number = int(input())
    except ValueError:
        break
    else:
        total_sum += number
        total_numbers += 1
print(total_sum / total_numbers)
