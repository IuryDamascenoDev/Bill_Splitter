import random

people_wanna_join = int(input("Enter the number of friends joining (including you): "))
print()

friends_keys = set()
lucky_friend = None

def split_bill(bill_value):

    splitted_bill = total_bill_value / people_wanna_join
    splitted_bill = splitted_bill.__round__(2)

    return splitted_bill

def luckyless_split_bill(bill_value):

    splitted_bill = total_bill_value / (people_wanna_join - 1)
    splitted_bill = splitted_bill.__round__(2)

    return splitted_bill

if people_wanna_join > 0:
    print("Enter the name of every friend (including you), each on a new line: ")

    i = 0
    while i < people_wanna_join:
        friend_name = input()
        friends_keys.add(friend_name)
        i += 1

    print()
    friends = dict.fromkeys(friends_keys, 0)

    total_bill_value = int(input("Enter the total bill value: "))
    print()

    bill = split_bill(total_bill_value)

    for friend in friends:
        friends[friend] = bill

    use_who_is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if use_who_is_lucky == 'Yes':
        friends_names = list(friends)
        lucky_friend_index = random.randrange(0, len(friends_names), 1)
        lucky_friend = friends_names[lucky_friend_index]
        print(f"{lucky_friend} is the lucky one!\n")

        lucky_bill = luckyless_split_bill(total_bill_value)

        for friend in friends:
            friends[friend] = lucky_bill

        friends[lucky_friend] = 0
        print(friends)

    else:
        print("\nNo one is going to be lucky\n")
        print(friends)
else:
    print("No one is joining for the party")