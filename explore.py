from ui import say, rule, pause, menu, hp_bar
from items import WEAPON, ARMOR, FOOD
from inv import inv_menu
from gym import gym
from battle import battle
from enemy import make_enemy

INV_LIMIT = 8


def give_loot(player, room):
    kind, key = room["loot"], room["key"]
    if room["text"]:
        say(room["text"], slow=True)
    if kind == "weapon":
        w = WEAPON[key]
        say(f"You found: {w.name} (+{w.dmg})! {w.desc}")
        if key not in player.wpns_owned:
            player.wpns_owned.append(key)
        if w.dmg > WEAPON[player.weapon].dmg:
            player.weapon = key
            say(f"You equipped the {w.name}.")
    elif kind == "armor":
        a = ARMOR[key]
        say(f"You found: {a.name} (DEF {a.defense})! {a.desc}")
        if key not in player.arms_owned:
            player.arms_owned.append(key)
            if a.defense > player.defense:
                player.armor = key
                say(f"You equipped the {a.name}.")
    elif kind == "food":
        f = FOOD[key]
        say(f"You found: {f.name}! {f.desc}")
        if len(player.items) >= INV_LIMIT:
            say("OOF... Your pocket are full... you have to leave something behind..")
        else:
            player.items.append(key)
            say("Added to you inventory. nice!")
    elif kind == "hpup":
        player.max_hp += key
        player.hp += key
        say(f"MAX HP UP! +{key} (now {player.max_hp}) WOW!")


def room_menu(player, room, state, quiet):
    while True:
        opts = ["Continue", "Inv", "Status"]
        if room["kind"] == "gym":
            opts.append("Train (weighlifting)")
        if quiet and not state["heal_used"]:
            opts.append("Rest (one-time full heal for this route)")
        choice = opts[menu("\nWhat now? hmm..", opts)]

        if choice == "Continue":
            return
        if choice == "Inv":
            inv_menu(player)
        elif choice == "Status":
            player.status()
        elif choice.startswith("Train"):
            gym(player, room["name"], state)
        elif choice.startswith("Rest"):
            state["heal_used"] = True
            player.hp = player.max_hp
            say(
                "You rest. A warm feeling fills you with d e t e r m i n a t i o n.",
                slow=True,
            )
            say(f"HP fully restored!    {hp_bar(player.hp, player.max_hp)}")


def run_route(player, route, index):
    state = {"heal_used": False, "gym": {}}
    rule("=")
    say(f"ROUTE {index + 1}: {route.title}")
    rule("=")
    say(route.intro, slow=True)
    pause()

    for n, room in enumerate(route.rooms, 1):
        rule()
        say(f"[{route.title}    room {n}/{len(route.rooms)}]")
        kind = room["kind"]

        if kind in ("story", "gym"):
            say(room["text"], slow=True)
            room_menu(player, room, state, quiet=True)
        elif kind == "loot":
            give_loot(player, room)
            room_menu(player, room, state, quiet=True)
        else:  # either fight or boss
            if room["text"]:
                say(room["text"], slow=True)
                pause()
            result = battle(player, make_enemy(room["enemy"], player))
            if result == "dead":
                return "dead"
            if kind == "boss":
                player.last_boss = result
            say(
                {
                    "killed": "\nYou won... but at what cost?..",
                    "spared": "\nYou chose mercy. They can live another day..",
                    "fled": "\nYou escaped. They can find you another day..",
                }[result]
            )
            room_menu(player, room, state, quiet=False)

    if route.outro:
        rule()
        say(route.outro, slow=True)
        pause()
    return "cleared"
