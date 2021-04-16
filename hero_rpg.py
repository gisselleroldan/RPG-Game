# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random


class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.armor = 0
        self.evade = 0

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

    def getItem(self, item):
        pass

class Store(Character):

    def SuperTonic(self):
        hero.health + 10
        cost = 2

    def Armor(self):
        hero.armor + 2
        cost = 2

    def Evade(self):
        hero.evade + 2
        cost = 3

    
    # def Beserk():
    #     pass
    # #

    def GymMembership():
        hero.power + 3
        cost = 4
    



class Hero(Character):
    def __init__(self, health, power, armor=0):
        super().__init__(health, power)
        self.name = "Hero"
        self.armor = 0
        self.evade = 0

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

    def attack(self, enemy):
        enemy.health -= self.power
        print("The Shadow does {} damage to you.".format(self.power))

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
            enemy.health -= self.power * 5
            print(f"Sniper does {self.power * 5} damage to the {enemy.name}")
        else:
            print(f'{self.name} missed!')


def main():
    bounty = 5

    hero = Hero(50, 5)
    goblin = Goblin(6,2)
    zombie = Zombie(100, 1)
    medic = Medic(10, 4)
    shadow = Shadow(1,3)
    wizard = Wizard(10, 2)
    sniper = Sniper(10,5)

    characterList = {
        "goblin": goblin,
        "zombie": zombie,
        "medic": medic,
        "shadow": shadow,
        "wizard": wizard,
        "sniper": sniper
        }

# choose a random character and have it attack the hero if he chooses #2
    # elif raw_input == "2"

#once a character is dead, remove that character from the character list


    while hero.alive():

        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("4. Show Bounty")
        print("5. Go to store")

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

        elif raw_input == "2":
            print('Encountered an enemy!')
            enemy = random.choice(list(characterList.values())) 
            enemy.attack(hero)
            hero.print_status()
        elif raw_input == "3":
            print('Goodbye')
            break
        elif raw_input == "4":
            print(f'Your bounty total is {bounty} coins')
        elif raw_input == "5":
            print("Welcome weary traveler, below is what is available: ")
            print('Supertonic \nArmor')
            choice = input('Choose item to purchase: ')
            if choice == "Armor":
                if bounty < 2:
                    print('You do not have enough coins')
                else:
                    hero.armor += 2
                    print(f'Armor increased to {hero.armor}')
            elif choice == "Supertonic":
                hero.health = 50
                if bounty < 2:
                    print('You do not have enough coins')
                else:
                    bounty -= 2
                    print('Full health restored!')
        else:
            print("Invalid input {}".format(raw_input))
        


main()
