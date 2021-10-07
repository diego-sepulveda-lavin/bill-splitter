consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

user_string = input()

for char in user_string:
    if char.lower() in consonants:
        print("consonant")
    elif char.lower() in vowels:
        print("vowel")
    else:
        break
