user_number = int(input())


def is_prime(n):
    if n == 1:
        print("This number is not prime")
        return False

    for current_number in range(2, n):
        if n % current_number == 0:
            print("This number is not prime")
            return False

    print("This number is prime")
    return True


is_prime(user_number)
