import random

money = 100

def coin_flip(bet, call):
    flip = random.randint(1,2)

    if flip == 1:
        print('The coin showed Heads!')
        if call == 'Heads':
            print('You won $' + str(bet))
            return bet
    elif flip == 2:
        print('The coin showed Tails!')
        if call == 'Tails':
            print('You won $' + str(bet))
            return bet

    print("You lost $" + str(bet))
    return bet * -1

def cho_han(bet, call):
    toss = random.randint(1,6) + random.randint(1, 6)

    if toss % 2 == 0:
        print('The toss was Even! ' + str(toss))
        if call == 'Even':
            print('You won $' + str(bet))
            return bet
    else:
        print('The toss was Odd! ' + str(toss))
        if call == 'Odd':
            print('You won $' + str(bet))
            return bet

    print('You lost $' + str(bet))
    return bet * -1

def card_game(bet):
    deck = []
    for i in range(1, 14):
        deck += [i, i, i, i] 
    random.shuffle(deck)
    player_card = deck.pop()
    computer_card = deck.pop()

    print('You drew a', end=' ')
    if player_card == 11:
        print('Jack')
    elif player_card == 12:
        print('Queen')
    elif player_card == 13:
        print('King')
    else:
        print(player_card)
    print('The computer drew a', end=' ')
    if computer_card == 11:
        print('Jack')
    elif computer_card == 12:
        print('Queen')
    elif computer_card == 13:
        print('King')
    else:
        print(computer_card)

    if player_card == computer_card:
        print('You tied! No money lost or won!')
        return 0
    elif player_card > computer_card:
        print('You won $' + str(bet))
        return bet
    else:
        print('You lost $' + str(bet))
        return bet * -1

def roulette(bet, call):
    #finish me
    num = random.randint(0, 37)
    num = str(num)

    if num == '37':
        num = '00'
    print('Number ' + num + '!')

    if num != 0 and num != 00:
        if call == 'Even':
            if int(num) % 2 == 0:
                print('You won $' + str(bet))
                return bet
        elif call == 'Odd':
            if int(num) % 2 == 1:
                print('You won $' + str(bet))
                return bet
    
    if num == call:
        print('You won $' + str(bet * 35))
        return bet * 35

    print('You lost $' + str(bet))
    return bet * -1


print(money)
money += coin_flip(15, 'Heads')
money += cho_han(15, 'Odd')
money += card_game(15)
money += roulette(15, '00')
print(money)