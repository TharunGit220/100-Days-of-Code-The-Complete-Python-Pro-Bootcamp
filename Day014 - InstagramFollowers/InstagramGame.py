import gamedata
import random
import art
print(art.logo)

def getthehigh(A,B):
    if A > B:
        return "A" 
    else:
        return "B"

point =0

A = gamedata.data[random.randint(0,len(gamedata.data)-1)]
while True:
    B = gamedata.data[random.randint(0,len(gamedata.data)-1)]
    
    print(f"compare {A['name']},{A['description']},from {A['country']} \n")
    print(art.vs)
    print(f"compare {B['name']},{B['description']},from {B['country']} ")
   
    result = getthehigh(A['follower_count'],B['follower_count'])
    if input("who has the highest A or B ") == result:
        A = B
        point +=1
        print(f"you right {point}")
    else:
        print(f"Nope your score is {point} ")
        break
    
    


