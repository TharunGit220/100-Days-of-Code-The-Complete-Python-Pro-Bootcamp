import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# print(random.choice(cards))
print(art.logo)
play = True
mycards = []
computer = []
def deal():
    global mycards,computer
    mycards = []
    computer = []
    for i in range(2):
        mycards.append(random.choice(cards))
        computer.append(random.choice(cards))
    

deal()
if sum(mycards) > 21:
    print(f'you final hand {mycards}: {sum(mycards)} ')
    print(f'computer  final hand {computer}: {sum(computer)} ')
    print("you went over lose sucker ")
    play = False

while play:
    print(f"your cards: {mycards} {sum(mycards)} ")
    print(f"computer cards: {computer[0]}")
    if input("do you want another card ") == 'y':
        mycards.append(random.choice(cards))
        if sum(mycards) > 21:
            # print(f'you final hand {mycards}: {sum(mycards)} ')
            # print(f'computer  final hand {computer}: {sum(computer)} ')
            print("you went over lose sucker ")
            
        elif sum(mycards) < 21:
            print(f'your hand {mycards}: {sum(mycards)} ')
            continue
        else:
            print("21 and a hole")
    else:
        if sum(computer) < 17:
            while sum(computer) > 17:
                computer.append(random.choice(cards))
        if sum(computer) > 17:
            if sum(mycards) > sum(computer):
                print("you win")
            elif sum(mycards) == sum(computer):
                print("draw")
            else:
                print("you lose")
            
    if input("do you play again  ") == 'y': 
        deal()   
    else:
        play = False
    
