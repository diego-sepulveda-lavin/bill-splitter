from math import inf

min_value = inf
while True:
    try:
        user_input = float(input())
    except ValueError:
        break
    else:
        if user_input < min_value:
            min_value = user_input

print(min_value)
