import os
from Classes import player, goblin, bandit, wolf
import random 
from random import choice


player = player(name= "Player",ATK= 10, HP= 100, MAGIC= 15)
goblin = goblin(name= "Goblin",ATK= 5, HP= 100, MAGIC= 10)
wolf = wolf(name= "Wolf",ATK= 10, HP= 100, MAGIC= 15)
bandit = bandit(name= "Bandit",ATK= 10, HP= 100, MAGIC= 15)
isinbattle = False   
encounter_choice = [goblin, bandit, wolf]

def battleover():
    print("The battle is over")


def clear():
    os.system('cls')

def enemyturn(enemy):

    if enemy.HP < (enemy.MAXHP/2): 
        healsuccess = random.randint(1,100)
        check = healsuccess % 2
        if check == 1:
            enemy.attack(player)
            print(f"{enemy.name} dealt {enemy.ATK} damage to {player.name}")
        elif check == 0:
            enemy.heal(enemy)
            print(f"{enemy.name} healed for {enemy.MAGIC} HP")
    else:
        enemy.attack(player)
        print(f"{enemy.name} dealt {enemy.ATK} damage to {player.name}")
            
    
    

    


def encounterstart(): #battle begins
    isinbattle = True
    enemy = random.choice(encounter_choice)
    print(f"Alert! A(n) {enemy.name} approaches!!!")
    while isinbattle:
        
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f"{player.name} has {player.HP} / {player.MAXHP} HP")
        print(f"{enemy.name} has {enemy.HP} / {enemy.MAXHP} HP")
        print("1.Attack")
        print("2.Heal")
        print("3.Run away")
        act = (input("What will you do?. Choose a number: "))
        if act == "1":
            player.attack(enemy)
            print(f"{player.name} dealt {player.ATK} damage to {enemy.name}")
        if act == "2":
            player.heal(player)
            print(f"{player.name} healed for {player.MAGIC} HP")
        if act == "3":
            runsuccess = random.randint(0,100)
            check = runsuccess % 2
            if check == 0:
                print("You ran away")
                isinbattle = False
                battleover()
            else:
                print("You failed to run away")
        if isinbattle == True :
            enemyturn(enemy)

        if player.HP == 0:
            print("You died")
            isinbattle = False
            battleover()
            
    

    
    
