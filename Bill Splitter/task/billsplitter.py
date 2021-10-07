from random import choice


def lucky_winner(luck_enabled, payment_detail):
    luck_enabled = luck_enabled.lower()

    if luck_enabled == 'no' or luck_enabled == 'n':
        print("No one is going to be lucky")
        return None
    elif luck_enabled == "yes" or luck_enabled == 'y':
        participants = []
        for friend_name in payment_detail:
            participants.append(friend_name)
        winner = choice(participants)
        print(f"{winner} is the lucky one!")
        return winner
    else:
        print('Incorrect choice. "NO" is assumed')
        return None


def calculate_bill(friends_number, payment_detail, total, winner):
    if winner:
        friends_number -= 1
    payment_per_person = round(total / friends_number, 2)

    for friend in payment_detail:
        if winner == friend:
            continue
        payment_detail[friend] = payment_per_person


def generate_empty_bill(friends_number):
    payment_detail = {}
    for i in range(friends_number):
        name = input()
        payment_detail[name] = 0
    return payment_detail


try:
    print("Enter the number of friends joining (including you):")
    friends_qty = int(input())
    if friends_qty < 1:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        bill_detail = generate_empty_bill(friends_qty)

        print("Enter the total bill value:")
        bill_total = int(input())

        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        luck_feature = input()

        lucky_one = lucky_winner(luck_feature, bill_detail)
        calculate_bill(friends_qty, bill_detail, bill_total, lucky_one)

        print(bill_detail)

except ValueError:
    print("Please enter a valid number")
