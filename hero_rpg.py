# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random

#Character (parent class)
class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power

    # def attack(self, enemy):
    #     pass

    def alive(self):
        if self.health > 0:    
            return True
        else:
            print(f'{self.name} is dead.')
            return False

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

#Hero Character
class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Hero"

    def attack(self, enemy):

        chance = random.randint(0,100)
        if chance > 20:
            print('Hero has double damage power! \n')
            enemy.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the {enemy.name}")
        else:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy.name}")
        

class Zombie(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Zombie"

    def attack(self, enemy):
        enemy.health -= self.power
        print("The zombie does {} damage to you.".format(self.power))

    def alive(self):
        return True
        
class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"
        self.bounty = 4

    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))

class Shadow(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Shadow"
        self.bounty = 10

class Medic(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Medic"
        self.bounty = 1

    def attack(self, enemy):
        enemy.health -= self.power
        print("The Medic does {} damage to you.".format(self.power))

class Wizard(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Wizard"
        self.bounty = 4

    def attack(self, enemy):
        enemy.health -= self.power
        print("The wizard does {} damage to you.".format(self.power))   

class Sniper(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Sniper"
        self.bounty = 3    

    def attack(self, enemy):
        chance = random.randint(0,100)
        if chance > 70:
            print('Target Locked! \n')
            enemy.health -= self.power * 3
            print(f"You do {self.power * 3} damage to the {enemy.name}")
        else:
            print(f'{self.name} missed!')


def main():
    bounty = 0

    hero = Hero(50, 5)
    goblin = Goblin(6,2)
    zombie = Zombie(100, 1)
    medic = Medic(10, 4)
    shadow = Shadow(1,3)
    wizard = Wizard(10, 2)
    sniper = Sniper(10,2)

    characterList = {
        "goblin": goblin,
        "zombie": zombie,
        "medic": medic,
        "shadow": shadow,
        "wizard": wizard,
        "sniper": sniper
        }


    while hero.alive():

        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("4. Show Bounty")

        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            for character in characterList:
                print(character)
            userChoice = input('Who do you want to fight? ').lower()
            if userChoice == "medic":
                chance = random.randint(0,100)
                if chance > 20:
                    hero.attack(medic)
                else:
                    hero.attack(medic)
                    (medic.health + 2)
                    print("Medic has recuperated 2 health!")
            if userChoice == "shadow":
                chance = random.randint(0,100)
                if chance > 90:
                    hero.attack(shadow)
                else:
                    print('Hero missed!')
            else:
                hero.attack(characterList[userChoice])
            
            if characterList[userChoice].alive():
                characterList[userChoice].print_status()
            else:
                print(f'Collected {characterList[userChoice].bounty} Bounty')
                bounty += characterList[userChoice].bounty


                # # Hero attacks chosen character 
                # hero.attack(characterList[userChoice])
                # if characterList[userChoice].alive():
                #     characterList[userChoice].print_status()

            # if zombie.alive():
            #     zombie.print_status()
            # if goblin.alive():
            #     goblin.print_status()
        elif raw_input == "2":
            zombie.attack(hero)
        elif raw_input == "3":
            print('Goodbye')
            break
        elif raw_input == "4":
            print(f'Your bounty total is {bounty}')
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.alive():
            # Goblin attacks hero
            zombie.attack(hero)
            if hero.alive():
                hero.print_status()

main()

