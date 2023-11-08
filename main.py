from characters import heros
from monsters import boss_monsters, mini_boss_monsters, basic_monsters
import random

member1 = heros[0]["name"]
member2 = heros[1]["name"]
member3 = heros[2]["name"]

start = input("Adventure awaits! Are you ready? Type 'y' or 'n'. ").lower()

if start == "y":
    print(f"You {member1} and the members of your team, {member2} & {member3}, wake up in the middle of the forest")
    level_1 =input("You look around and see a path on the left leading to a castle, and a massive cave entrance to the right, Go 'left' or 'right'? ").lower()
    if level_1 == "right":
        print("You and your team walk into the cave...")
        random_monster = random.choice(mini_boss_monsters)
        spawn = random_monster["name"]
        print(f"As you walk deeper into the cave, you come accross a sleeping {spawn}")
        level1_2 = input(f"Do you attack the sleeping {spawn} or do you escape? Type 'attack' or 'escape' ").lower()
    if level1_2 == "attack":
        pass

