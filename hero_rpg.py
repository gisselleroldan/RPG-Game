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

    def attack(self, enemy):
        if enemy.armor == 0:
            enemy.health -= self.power
            new_power = self.power
        elif enemy.armor == 2:
            enemy.health -= self.power -1
            new_power = self.power -1
        elif enemy.armor == 4:
            enemy.health -= self.power -2
            new_power = self.power -2
        elif enemy.armor == 6:
            enemy.health -= self.power -3
            new_power = self.power -3
        elif enemy.armor == 8:
            enemy.health -= self.power -4
            new_power = self.power -4
        elif enemy.health == 10:
            enemy.health -= self.power -5
            new_power = self.power -5
        print(f'{self.name} does {new_power} damage!')

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
        hero.health = 50
        cost = 2

    def Armor(self):
        hero.armor + 2
        cost = 2

    def Evade(self):
        hero.evade + 2
        cost = 3


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

    def alive(self):
        return True
        
class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"
        self.bounty = 4

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


class Wizard(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Wizard"
        self.bounty = 4

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

    hero = Hero(100, 10)
    goblin = Goblin(12,4)
    zombie = Zombie(100, 4)
    medic = Medic(20, 5)
    shadow = Shadow(1,6)
    wizard = Wizard(15, 8)
    sniper = Sniper(20,6)

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
        print("6. Show Stats")

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
            elif userChoice == "shadow":
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
            chance = random.randint(0,100)
            enemy = random.choice(list(characterList.values())) 
            #if hero has 0 evade, enemy will attack
            if hero.evade == 0:
                enemy.attack(hero)
            #if evade is 1-2, hero has 10% chance of dodging the attack
            elif hero.evade == 2:
                if chance < 90:
                    enemy.attack(hero)
                else:
                    print("Enemy missed!")
                #if evade is 3-5, hero has 15% chance of dodging the attack
            elif hero.evade >= 4 and hero.evade <= 6:
                if chance < 85:
                    enemy.attack(hero)
                else:
                    print("Enemy missed!")
            #if evade is 6-10, hero has 25% chance of dodging the attack        
            elif hero.evade >= 8 and hero.evade <= 10:
                if chance < 75:
                    enemy.attack(hero)
                else:
                    print("Enemy missed!")

            # if hero.armor == 0:
            #     enemy.attack(hero)
            #     hero.print_status()
            # else: 
            #     hero.health += hero.armor
            #     hero.print_status()
        elif raw_input == "3":
            print('Goodbye')
            break
        elif raw_input == "4":
            print(f'Your bounty total is {bounty} coins')
        elif raw_input == "5":
            print("Welcome weary traveler, below is what is available: ")
            print('Supertonic \nArmor\nEvade\nGym membership')
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
            elif choice == "Gym membership":
                hero.power += 3
                if bounty < 4:
                    print('You do not have enough coins')
                else:
                    bounty -= 4
                    print(f'Power increased to {hero.power}')
            
            elif choice == "Evade":
                # max evade is 10. If hero's evade is <= 8, you can add more evade. Else "max evade reached"
                if hero.evade <= 8:
                    if bounty < 2:
                        print('You do not have enough coins')
                    else:
                        hero.evade += 2
                        print(f'Evade increased to {hero.evade}')
                else:
                    print(f'Hero evade is {hero.evade}')
                    print('MAX EVADE REACHED')
        elif raw_input == "6":
            print(f'\nSTATS:\nEvade: {hero.evade}\nHealth: {hero.health}\nArmor {hero.armor}\n Gym Membership: {hero.power}')
        else:
            print("Invalid input {}".format(raw_input))
        


main()
