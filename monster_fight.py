import random

#see how quickly you can kill a random monster. It will ha vunerabilty to one damage, immune to another and reistance to the last.
#Give the monster 10 HP.
monster = 10
hero = 10

#Decide on the vunerabilty at random.
weak = random.randint(0,3)

#define the weakness multiplier P/S/B
vun_list = [[1,1,1], [2,1,0.5], [1,0.5,2], [0.5,2,1]]
multiplier = vun_list[weak]

#define the weapon
weapon = int(input("Choose your weapon! 1-Rapier\n2-Longsword\n3-Hammer\n--->"))
while (weapon > 3 or weapon <1):
    print("Invalid choice. Please try again.")
    weapon = int(input("Choose your weapon! 1-Rapier/n2-Longsword/n3-Hammer/n--->"))

print("Move to combat!")

turn =1
while (monster>0):
    dmg = random.randint(0,5) * multiplier[weapon-1] #calcs damage to the monster
    monster = monster - dmg #reduces hitpoints
    if (dmg == (5*multiplier[weapon-1])):
        print("Max damage! The monster has ", monster, " HP remaining!")
    elif (dmg > 2):
        print("You've dealt ", dmg, " damage this turn. The monster has ", monster, " HP remaining!")
    else:
        strike = random.randint(0,10) * 0.5
        hero = hero - strike
        print("You've been hit! You lost ", strike, "HP!")
        if(hero<1):
            print("You DIED...")
            break
        else:
            continue
    turn = turn +1

print("Congratulations brave hunter, it took you ", turn, " turns to win this fight. You have ", hero," remaining.")



