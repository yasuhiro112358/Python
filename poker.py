import random
import time


# トランプの生成（行列形式）
def cards():

    cards = [[0] * 13 for i in range(4)]

    for j in range(4):
        for i in range(13):
            cards[j][i] = str(i + 1)
            
            if cards[j][i] == '1':
                cards[j][i] = 'A'

            elif cards[j][i] == '10':
                cards[j][i] = 'T'

            elif cards[j][i] == '11':
                cards[j][i] = 'J'

            elif cards[j][i] == '12':
                cards[j][i] = 'Q'

            elif cards[j][i] == '13':
                cards[j][i] = 'K'

    for j in range(4):
        for i in range(13):
            if j == 0:
                cards[j][i] = cards[j][i] + '♠︎ '
            elif j == 1:
                cards[j][i] = cards[j][i] + '♡ '
            elif j == 2:
                cards[j][i] = cards[j][i] + '♢ '
            elif j == 3:
                cards[j][i] = cards[j][i] + '♣︎ '

    return cards


# Cards with #52（ベクトル形式）
def cards52(cards):

    cards52 = [0] * 52

    k = 0
    for j in range(4):
        for i in range(13):
            cards52[k] = cards[j][i]
            k = k + 1

    return cards52


# シャッフルデッキの生成
def deck52(cards52):
    
    lst = list(range(0, 52)) # 0-51の数列
    lst2 = random.sample(lst, len(lst)) # 0-51のランダム数列

    deck52 = [0] * 52
    j = 0
    for i in range(52):
        j = lst2[i]
        deck52[i] = cards52[j]

    return deck52

# ディーリング（５枚）
# 今は使っていないdefinition
def deal(deck52):

    dealingTime = 0.5
    sleepTime = 1.5

    numOfDeal = 5

    print('=== Board ===')
    for i in range(numOfDeal):
        print('【' + deck52[i] + '】', end = "", flush = 'True')
        time.sleep(dealingTime)

    time.sleep(sleepTime)
    print()
    print()


# Dealing
def dealing(deck52, numOfDealt, nameOfStreet, numOfCardDealing): 
    # deck52は配りたいデッキ
    # numOfDealtはここまで何枚のカードを配っているか

    dealingTime = 0.5
    sleepTime = 1.5

    print('=== ' + nameOfStreet + ' ===')
    for i in range(numOfCardDealing):
        print('【' + deck52[i + numOfDealt] + '】', end = "", flush = 'True')
        time.sleep(dealingTime)

    time.sleep(sleepTime)
    print()
    print()

    numOfDealt = numOfDealt + numOfCardDealing

    return numOfDealt




#==============
# Main
#==============

cards = cards() # トランプ（行列）の生成
cards52 = cards52(cards) # トランプ（ベクトル）の生成

numOfDealt = 0

# セリフ
sleepTime = 1.5

print()
print('''================================
        Hiro's Poker Room
================================''')
print()
time.sleep(sleepTime)
print('''Dealer: Welcome to Hiro's poker room!''')
print()
time.sleep(sleepTime)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    print('''Dealer: Want me to deal? (yes or no)''')
    print()
    time.sleep(sleepTime)

    playAgain = input()
    print()
    time.sleep(sleepTime)

    if playAgain == 'yes' or playAgain == 'y':
        shuffledDeck = deck52(cards52)
        numOfDealt = 0
        numOfDealt = dealing(shuffledDeck, numOfDealt, 'Pre-flop', 2)
        numOfDealt = dealing(shuffledDeck, numOfDealt, 'Flop', 3)
        numOfDealt = dealing(shuffledDeck, numOfDealt, 'Turn', 1)
        numOfDealt = dealing(shuffledDeck, numOfDealt, 'River', 1)

    else:
        break

print('''Dealer: Thank you for playing!

================================''')
print()

