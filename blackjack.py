import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def clear():
    'Clear is used to clear the terminal.'
    print('\033[H\033[2J', end='', flush=True)


def deal_card():
    """Returns a random card from a deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return he score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw (:"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack :o"
    elif user_score == 0:
        return "Win with a Blackjack :8"
    elif user_score > 21:
        return "You went over 21. You lose ;)"
    elif computer_score > 21:
        return "Opponent went over 21. You win :D"
    elif user_score > computer_score:
        return "You win (:"
    else:
        return "You lose ;("


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer`s first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            while True:
                if user_should_deal == 'y':
                    user_cards.append(deal_card())
                    break
                elif user_should_deal == 'n':
                    is_game_over = True
                    break
                else:
                    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(f"  Computer1s final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))



while True:
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if play == 'y':
        clear()
        play_game()
    elif play == 'n':
        break
    else:
        continue
