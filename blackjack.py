import math
import random
DECK = ['A', 'A', 'A', 'A', 'A', 'A', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '6', '6', '6', '6', '6', '6', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '10', '10', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'K', 'K']

def start():
    start_deck = DECK[:]
    random.shuffle(start_deck)
    return start_deck

def deal(deckinuse):
    player = [deckinuse.pop(), deckinuse.pop()]
    hidden_card = deckinuse.pop()
    dealer = [deckinuse.pop(), '?']
    print(player)
    print(dealer)
    return player, dealer, hidden_card

def player_action(player, deckinuse):
    while True:
        playerinput = input("Hit(h) or Stand(s): ")
        if playerinput == 'h':
            player.append(deckinuse.pop())
            print(player)
        elif playerinput == 's':
            print(player)
            break
        else:
            print("Please enter h or s")
    return player, deckinuse
    
def dealer_action(dealer, hidden_card, deckinuse):
    actual_dealer = dealer[:]
    actual_dealer.remove("?")
    actual_dealer.add(hidden_card)
    total_score = 0
    ace_active = False
    for i in actual_dealer:
        try:
            total_score+= int(actual_dealer[i])
        except TypeError as e:
            if actual_dealer[i] == "J" or "Q" or "K":
                total_score+=10
            elif actual_dealer[i] == "A":
                total_score+=11
                ace_active = True
    if total_score < 17:
        hit_card = deckinuse.pop()


def main():
    deckinuse = start()
    player, dealer, hidden_card = deal(deckinuse)
    player, deckinuse = player_action(player, deckinuse)
    dealer_action(dealer, hidden_card, deckinuse)


main()