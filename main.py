from ui import say, talk, rule, pause, menu, hp_bar
from player import Player
from items import FOOD

def title_sc():
    rule("=")
    print("   U N D E R T A L E - I N S P I R E D   R P G")
    rule("=")
    say("A fan-made terminal game :D", slow=True)
    name = input("Name your fallen human (Enter for 'Frisk'): ").strip()
    return name[:12] if name else "Frisk"

def main():
    player = Player(title_sc())
    player.hp #temp
    while True:
        pick = menu("\nTest menu:", ["Status", "Eat food", "Quit"])
        if pick == 0:
            player.status()
        elif pick == 1:
            if not player.items:
                say("Welp, no more food.")
                continue
            names = [FOOD[k].name for k in player.items]
            idx = menu("HMM", names)
            player.eat(idx)
        else:
            break
    say("\nWork!")

if __name__ == "__main__":
    main()