import random
import time
from ui import say, ask, hp_bar

ARROW = {"w": "^", "a": "<", "s": "v", "d": ">"}
HIT_D = 4  # dmg/hit = (enemy atk - your def)/this. made it become 4 due to toriel being hard :kek:
BASE_T = 2.5
TIME_P_A = 0.9
SP_TIME = 4.0  # for blue/orange atk

_legend_shown = False


def hit_dmg(player, enemy):
    return max(1, (enemy.atk - player.defense) // HIT_D + random.randint(0, 1))


def dodge_atk(player, enemy, kind):
    global _legend_shown
    per_hit = hit_dmg(player, enemy)
    hits = 0
    if kind == "dodge":
        n = random.randint(*enemy.seq_len)
        seq = [random.choice("wasd") for _ in range(n)]
        say("\n>> ATK INCOMING! " + " ".join(ARROW[c] for c in seq))
        if not _legend_shown:
            say("   Type the matching keys FAST: w=^ a=< s=v d=>    ")
            _legend_shown = True
            limit = BASE_T + TIME_P_A * n
            start = time.time()
            ans = "".join(ask("    dodge> ").split())
            elapsed = time.time() - start
            miss = sum(1 for i, c in enumerate(seq) if i >= len(ans) or ans[i] != c)
            miss += max(0, len(ans) - n)
            if elapsed > limit:
                miss += 1
                say(f"  Bruh.. You're too slow! ({elapsed:.1f}s/{limit:.1f}s)")
            hits = min(miss, n)
        elif kind == "blue":
            say("\n>> BLUE ATK! DON'T MOVE! type  stop  to hold still.")
            start = time.time()
            ans = ask("    dodge> ")
            if ans != "stop" or time.time() - start > SP_TIME:
                hits = 2
        if hits == 0:
            say("   Dam you're good. You dodged it all! WOW")
            return
        dmg = hits * per_hit
        player.hp -= dmg
        say(f"  You took {hits} hit(s)! -{dmg} HP   {hp_bar(player.hp, player.max_hp)}")

def enemy_turn(player, enemy):
    for _ in range(random.randint(*enemy.volleys)):
        dodge_atk(player, enemy, random.choice(enemy.kinds))
        if player.hp <= 0:
            return
