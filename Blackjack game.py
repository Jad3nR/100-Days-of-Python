import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_bj(play):
    if play in ["y"]:
        print(logo)
        your_cards = random.sample(cards, 2)
        comp_cards = random.sample(cards, 2)
        sum_cards_user = sum(your_cards)
        print(f"Your cards are: {your_cards}, Current score: {sum_cards_user}")
        print(f"Computer's first card: {comp_cards[0]}")
        return your_cards, sum_cards_user, comp_cards
    else:
        exit()


def add_cards(play, added_yours, added_comp):
    while play == "y":
        added_yours.append(random.choice(cards))
        added_sum_cards = sum(added_yours)

        if sum(added_comp) < 17:
            added_comp.append(random.choice(cards))

        print(f"Your cards are: {added_yours}, Current score: {added_sum_cards}")
        print(f"Computer's first card: {added_comp[0]}")

        if added_sum_cards > 21:
            print("You lose!")
            exit()
        elif added_sum_cards == 21:
            print("You win!")
            exit()

        play = input("Pick another card? Type y to continue, n to pass: ").lower()

    sum_comp = sum(added_comp)

    print(f"Computer's final hand: {added_comp}, Final score: {sum_comp}")

    if sum_comp > 21 or sum_comp < added_sum_cards:
        print("You win!")
    else:
        print("You lose!")

    exit()


# Start game
choice = input("Do you want to play Blackjack? Type Y or N: ").lower()

your_cards, sum_cards_user, comp_cards = play_bj(choice)

if sum_cards_user == 21:
    print("You win!")
elif sum_cards_user > 21:
    print("You lose!")
else:
    choice = input("Type y to pick another card, type n to pass: ").lower()
    add_cards(choice, your_cards, comp_cards)
