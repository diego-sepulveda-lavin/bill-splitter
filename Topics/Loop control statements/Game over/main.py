scores = input().split()
# put your python code here
mistakes = 0
correct = 0
max_mistakes = 3

pointer = 0
while pointer < len(scores) and mistakes < max_mistakes:
    if scores[pointer] == 'I':
        mistakes += 1
    elif scores[pointer] == 'C':
        correct += 1
    pointer += 1

if mistakes >= max_mistakes:
    print("Game over")
else:
    print("You won")
print(correct)
