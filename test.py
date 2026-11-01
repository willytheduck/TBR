import math
import sys
import items
import story
import atk
import battle as battle_mod
import enemy as enemy_mod

WEAPON = getattr(items, "WEAPON", None) or getattr(items, "WEAPONS")
ARMOR = getattr(items, "ARMOR", None) or getattr(items, "ARMORS")
PROGRESS = [
    (3, "toy_knife", "ribbon", 34),  # RUINS
    (6, "toy_knife", "bandanna", 38),  # SNOWDIN
    (9, "ballet_shoes", "tutu", 43),  # WATERFALL
    (12, "empty_gun", "tutu", 48),  # HOTLAND
    (15, "real_knife", "tutu", 53),
]  # NEW HOE/PAPYRUS

DIV = getattr(atk, "HIT_D", 2)
MULT = getattr(battle_mod, "PLAYER_DMG_MULT", 3)


class Dummy:
    kills = 0


def report():
    print(f"Settings: enemy HIT_D={DIV}, PLAYER_DMG_MULT={MULT}\n")
    seen = []
    for i, route in enumerate(story.ROUTES):
        st, wkey, akey, hp = PROGRESS[min(i, len(PROGRESS) - 1)]
        weapon = WEAPON[wkey]
        armor = ARMOR[akey]
        attack = weapon.dmg + st
        print(f"=== {route.title}   (STR {st}, {weapon.name}, {hp} HP)===)")
        print(
            f"{'enemy':14} {'HP':>5} {'DEF':>4} {'turns to kill': >14} {'hit dmg':>8} {'hits you take':>14} flags"
        )
        for room in route.rooms:
            if room["kind"] not in ("fight", "boss"):
                continue
            seen.append(room["enemy"])
            e = enemy_mod.make_enemy(room["enemy"], Dummy())
            my_dmg = max(1, attack * MULT - e.defense)
            exp_dmg = my_dmg * 0.9 * (1 + 0.12 * 0.5)
            turns = math.ceil(e.hp / exp_dmg)
            hit = max(1, (e.atk - armor.defense) // DIV) + 0.5
            can_take = math.ceil(hp / hit)
            flags = []
            if turns > 40:
                flags.append("UNKILLABLE")
            if hit >= hp:
                flags.append("ONE-SHOT")
            elif hit >= hp / 2:
                flags.append("DEADLY")
            tag = "*" if e.boss else " "
            print(
                f"{tag}{e.name:13} {e.hp:>5} {e.defense:>4} {turns:>14} {hit:>8.1f} {can_take:>14}    {''.join(flags)}"
            )
        print()
    print(
        "* = boss. Remember each enemy turn has 1-3 attacks with up to 3-4 hits each if you miss the arrows."
    )
    if "papyrus" not in seen:
        print(
            '\n!! Papyrus isn\'t in story.py: add  B("papyrus", "...")  to the last route\'s rooms.'
        )


if __name__ == "__main__":
    report()
