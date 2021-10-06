def check_palindrome(word):
    left_pointer = 0
    right_pointer = len(word) - 1
    while left_pointer < right_pointer:
        if word[left_pointer] != word[right_pointer]:
            return "Not palindrome"
        left_pointer += 1
        right_pointer -= 1
    return "Palindrome"


user_word = input()
result = check_palindrome(user_word)
print(result)
