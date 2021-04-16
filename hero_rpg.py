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

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

#Hero Character
class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Hero"

    def attack(self, enemy):

        choice = random.randint(0,100)
        if choice > 20:
            print('Hero has double damage power! \n')
            enemy.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the {enemy.name}")
        else:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy.name}")

        
        

# Zombie character
class Zombie(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Zombie"

    def attack(self, enemy):
        enemy.health -= self.power
        print("The zombie does {} damage to you.".format(self.power))

    def alive(self):
        return True

        
# Goblin Character
class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = "Goblin"

    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))

        
#maybe put the power as a random int and put 0 through max so there is a chance you could miss your attack
def main():
    hero = Hero(10, 5)
    goblin = Goblin(6,2)
    zombie = Zombie(100, 1)


    while zombie.alive() and hero.alive():
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks zombie
            
            hero.attack(zombie)
            if zombie.alive():
                zombie.print_status()
        elif raw_input == "2":
            zombie.attack(hero)
        elif raw_input == "3":
            print('Goodbye')
            break
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.alive():
            # Goblin attacks hero
            zombie.attack(hero)
            if hero.alive():
                hero.print_status()
            else:
                print(f'You are dead')

main()

