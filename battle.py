import random
from ui import say, rule, menu, hp_bar
from items import WEAPON
from inv import inv_menu
from atk import enemy_turn

PLAYER_DMG_MULT = 3 #mult ur atk. 
MISS_CHANCE = 0.10
CRIT_CHANCE = 0.12
FLEE_CHANCE = 0.60

def calc_dmg(player, enemy):
    raw = (player.atk + random.randint(-2,2))*PLAYER_DMG_MULT
    return max(1, raw - enemy.defense)

def do_fight(player, enemy):
    say(f"\nYou atk {enemy.name} with {WEAPON[player.weapon].name}!")
    if random.random()<MISS_CHANCE:
        say("...and you miss. RIP")
        return
    dmg = calc_dmg(player, enemy)
    if random.random() < CRIT_CHANCE:
        dmg = int(dmg *1.5) +1
        say("CRITICAL HIT! lucky...")
        enemy.hp -= dmg
        say(f"{enemy.name} takes {dmg} damage!  {hp_bar(enemy.hp, enemy.max_hp)}")

def do_act(player,enemy):
    names = ["Check"] + list(enemy.acts.keys()) + ["Back"]
    pick = names[menu(f"ACT on {enemy.name}:", names)]
    if pick == "Back":
        return False
    if pick == "Check":
        say(f"{enemy.name.upper()} HP {enemy.hp}/{enemy.max_hp} ATK {enemy.atk} DEF {enemy.defense}")
        say(f"Mercy: {enemy.mercy}%    (reack 100% to spare)")
        return True
    txt, gain = enemy.acts[pick]
    say(txt)
    if enemy.block_spare:
        say(enemy.block_spare)
        return True
    enemy.mercy = min(100, enemy.mercy + gain)
    if enemy.mercy >= 100:
        say(f"{enemy.name} doesn't want to fight anymore. (You can SPARE now! (DO IT!))")
    else: 
        say(f"(Mercy {enemy.mercy}%)")
    return True

def do_mercy(player, enemy):
    opts = ["Spare", "Flee", "Back"]
    pick = opts[menu("MERCY:", opts)]
    if pick == "Back":
        return "back"
    if pick == "Spare":
        if enemy.block_spare:
            say(enemy.block_spare)
            return None
        if enemy.mercy >= 100:
            say(enemy.spare_txt, slow=True)
            return "spared"
        say(f"{enemy.name} isn't read to be spared yet...")
        return None
    if enemy.boss:
        say("NUH UH")
        return None
    if random.random()<FLEE_CHANCE:
        say("You flee.")
        return "fled"
    say("NUH UH")
    return None

def battle(player,enemy):
    rule("*")
    say(enemy.intro, slow=True)
    rule("*")
    taunt_shown = [False]*len(enemy.taunts)

    while True:
        say(f"\n{enemy.name}: {hp_bar(enemy.hp, enemy.max_hp)} mercy {enemy.mercy}%")
        say(f"{player.name}: {hp_bar(player.hp, player.max_hp)}")
        choice = ["FIGHT", "ACT", "ITEM", "MERCY"][menu("Hmm..", ["FIGHT", "ACT", "ITEM", "MERCY"])]
        turn_use = True
        if choice == "FIGHT":
            do_fight(player,enemy)
            if enemy.hp <= 0:
                say(enemy.die_txt, slow=True)
                player.kills += 1
                return "killed"
        elif choice == "ACT":
            turn_use = do_act(player, enemy)
        elif choice == "ITEM":
            turn_use= inv_menu(player, in_battle=True)
        else:
            result = do_mercy(player,enemy)
            if result == "back":
                turn_use = False
            elif result == "spared":
                player.spares += 1
                return "spared"
            elif result == "fled":
                return "fled"
        if not turn_use:
            continue

        for i, (frac, line) in enumerate(enemy.taunts):
            if not taunt_shown[i] and enemy.hp <= enemy.max_hp * frac:
                taunt_shown[i] = True
                say(line, slow=True)

        if not enemy.boss or random.random() < 0.5:
            say(random.choice(enemy.flavor))

        enemy_turn(player, enemy)
        if player.hp <= 0:
            return "dead"