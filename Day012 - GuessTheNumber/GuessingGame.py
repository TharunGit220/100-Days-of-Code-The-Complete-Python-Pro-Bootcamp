import random

def game(lives):
    numb = random.randint(1,101)
    print(numb)
    print(f"you have {lives} to guess the correct answer")
    while  lives != 0:
        guess = int(input("enter a guess "))
        if  guess < numb:
            print("too low ")
        elif guess > numb:
            print("too high")
        else:
            print("perfect")
            break
        lives-=1
        if lives ==0 :
            print("yo'ave run out of guesses you lose")
            continue
        print(f"you have {lives}")

            

print("welcome to the number gusiing game ")

if input("choose a diffuculty type 'esay' or 'hard' ") == "e":
    game(5)
else:
    game(8)