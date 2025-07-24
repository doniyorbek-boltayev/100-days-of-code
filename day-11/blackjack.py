import random
print("---Welcome to Blackjack!---")
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    "Returns sum of cards in given list"
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and len(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "It's draw"
    elif u_score == 0:
        return "You win. It's Blackjack!"
    elif c_score == 0:
        return "You lose. Opponent has Blackjack"
    elif u_score > 21:
        return "You lose. You went over 21"
    elif c_score > 21:
        return "You win. Opponent went over 21"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score = {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score ==0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, otherwise type 'n': ")
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final scpre = {user_score}")
    print(f"Computer's final hand: {computer_cards}, final socre = {computer_score}")
    print(compare(user_score, computer_score))

    input("Do you want to play the game of Blackjack once again. Type 'y' for yes or 'n' for no: ")

while input("Do you want to play the game of Blackjack once again. Type 'y' for yes or 'n' for no: ") == 'y':
    print("\n" * 20)
    play_game()
