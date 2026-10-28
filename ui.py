import sys
import textwrap
import time

FAST = "--fast" in sys.argv #--fast to skip type effect
CHAR_D = 0.0 if FAST else 0.012
WIDTH = 72

def say(txt="", slow=False): #slow=True gives a typewriter effect
    for para in str(txt).split("\n"):
        for ln in (textwrap.wrap(para, WIDTH) or [""]):
            if slow and CHAR_D > 0: 
                for ch in ln:
                    sys.stdout.write(ch)
                    sys.stdout.flush()
                    time.sleep(CHAR_D)
                print()
            else:
                print(ln)

def talk(speak, txt): #for dialogue
    say(f"* {speak}: {txt}" if speak else f"* {txt}", slow=True)

def rule(char="-"):
    print(char*WIDTH)

def pause(msg="(press Enter)"):
    try: 
        input(f" {msg} ")
    except EOFError:
        print()
        sys.exit(0)

def ask(prompt, valid=None):
    while True:
        try:
            ans = input(prompt).strip().lower()
        except EOFError:
            print()
            sys.exit(0)
        if valid is None or ans in valid:
            return ans
        say("...option? I don't think so.")

def menu(title,options): #numbered menu
    say(title)
    for i, opt in enumerate(options,1):
        print(f"    {i}) {opt}")
    valid = [str(i) for i in range(1, len(options) + 1)]
    return int(ask("  > ", valid)) - 1

def hp_bar(hp, max_hp, size=20):
    hp = max(0, hp)
    filld = int(size * hp / max_hp) if max_hp else 0
    return "[" + "#" * filld + "-" *(size - filld) + f"] {hp}/{max_hp}"