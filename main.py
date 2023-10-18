from characters import heros

member0 = heros[0]["name"]
member1 = heros[1]["name"]
member2 = heros[2]["name"]

start = input("Adventure awaits! Are you ready? Type 'y' or 'n'. ").lower()

if start == "y":
    print(f"You and the members of your team, {member1} & {member2}, wake up in the middle of the forest")
    level_1 =input("You look around and see a path on the left leading to a castle, and a massive cave entrance to the right, Go 'left' or 'right'? ")
