# RPG Game
In this exercise, you will develop a hero RPG (*Role Playing Game*) using all of the cool new python knowledge you've acquired. This game will be created using **Object Oriented Programming**.

The game starts off with 2 characters: a `hero` and a `goblin`. Each character will be given a starting health and starting value. 

Each character also has a power that can be used to attack their opponent. In the initial scenario, the `hero's` opponent is the `goblin`, and the `goblin's` opponent is the `hero`.

When either character attacks his/her opponent, the opponent's health will decrease by the amount of power of the attacking character.

For example
>
>If the hero starts off with the following: 
>
>- health = 9
>- power = 4
>
>And the `goblin` starts off with the following:  
>
>- health = 7
>- power = 3
>
>Then when the hero attacks the goblin, the goblin's health will decrease by 4.
>
>The result of goblin's health after being attacked
>
>- health = 3  ==> (7 - 4)
>- power = 3
>

Video solutions have been provided for each step of part 1. Try your best not to look at the solutions. **Try this on your own first**. Part 2 is where you will start to implement custom features to your game. There are no video solutions for part 2. 

# RPG Game Part 1

Take the RPG game and rewrite it using objects.

Run following command to clone this repository onto your local computer

```bash
git clone https://github.com/DigitalCraftsStudents/python-rpg-starter.git
cd python-rpg-starter
rm -rf .git
git init
```

Use `hero_rpg.py`, located in this repository, as a starting point for your game.

As you complete each step, commit, push, and tag the final working version. In the future we'll base a refactor off of one the steps.

## Step 1
Make a Hero class to store the health and power of the hero, and make a `Goblin` class to store the health and power of the goblin. Use a hero object in place of the variables `hero_health` and `hero_power` and use a goblin object in place of the variables `goblin_health` and `goblin_power` all through out the app.

[Video Walk through](https://youtu.be/0pCEAP9eyg4)

## Step 2
Take the code for the hero attacking the goblin and extract it into a method (call it `attack`) of the `Hero` class. Replace the existing code with a call to the attack method. Hint: `attack` should take in the goblin (enemy) as a parameter: `hero.attack(goblin)`
[Video Walk through](https://youtu.be/in5hLnhX_eA)

## Step 3
Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it `attack`) of the Goblin class. Replace the existing code with a call to the attack method. It should look like `goblin.attack(hero)`.

[Video Walk through](https://youtu.be/epSo2TpHy2w)

## Step 4
Refactor the while condition:

`while goblin.health > 0 and hero.health > 0:`

to

`while goblin.alive() and hero.alive():`

The health checks should be moved to within the alive methods of Hero and Goblin respectively.

[Video Walk through](https://youtu.be/KW4LPZusrD0)

## Step 5
Take the code for printing the health status of the hero and move it into a method called `print_status` of `Hero`. Do the same for the goblin.

[Video Walk through](https://youtu.be/zwraV0P_jmI)

## Step 6
Do you see a lot of duplicated or similar code between `Hero` and `Goblin`? What if you can share the duplicated code between them? You can by using inheritance! Create a new class called `Character` and make both `Hero` and `Goblin` inherit from it.

[Video Walk through](https://youtu.be/1Y4FG8TpfKM)

## Step 7
The alive methods on `Hero` and `Goblin` should be identical. Move it into `Character`, and remove them from `Hero` and `Goblin` - now they can simply inherit it from `Character`.

[Video Walk through](https://youtu.be/gNeRHK3RhlM)

## Step 8: Bonus Challenge
The methods `attack` and `print_status` method in `Hero` and `Goblin` look almost identical, but not quite. Is it possible to move them into the `Character` class as well? Give it a try.

[Video Walk through](https://youtu.be/kscrMuuOZJA)

## Step 9: Bonus Challenge 2
Create a zombie character that cannot die and have it fight the hero instead of the goblin.

[Video Walk through](https://youtu.be/fE1jqzSvfz0)

# RPG Game Part 2

Follow the link below to continue building new characters with new abilities to your game.

- [RPG Part 2](./RPG-Part2.md)