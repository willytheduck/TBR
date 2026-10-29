from ui import say, talk, rule, pause, menu, hp_bar
from player import Player
from items import FOOD
from inv import inv_menu


def title_sc():
    rule("=")
    print("   U N D E R T A L E - I N S P I R E D   R P G")
    rule("=")
    say("A fan-made terminal game :D", slow=True)
    name = input("Name your fallen human (Enter for 'Frisk'): ").strip()
    return name[:12] if name else "Frisk"


def main():
    player = Player("Tester")
    player.hp = 12
    player.wpns_owned += ["toy_knife", "ballet_shoes"]
    player.arms_owned += ["bandage", "ribbon"]
    player.items += ["hot_dog", "nice_cream"]

    while True:
        pick = menu("\nTest menu:", ["Status", "Inventory", "Quit"])
        if pick == 0:
            player.status()
        elif pick == 1:
            inv_menu(player)
        else:
            break
    say("\nWorked!")


if __name__ == "__main__":
    main()
