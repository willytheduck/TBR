from items import WEAPON, ARMOR, FOOD
from ui import say, rule, hp_bar

XP_P_STRENGTH = 8 #muscle point for +1 strength


class Player:
    def __init__(self, name="Frisk"):
        self.name = name
        self.max_hp = 30
        self.hp = 30
        self.strength = 1
        self.muscle = 0
        self.weapon = "stick"
        self.armor = None
        self.wpns_owned = ["stick"]
        self.arms_owned = []
        self.items = ["monster_candy", "monster_candy"]
        self.kills = 0
        self.spares = 0

    @property
    def atk(self):
        return WEAPON[self.weapon].dmg + self.strength

    @property
    def defense(self):
        return ARMOR[self.armor].defense if self.armor else 0
    
    def heal(self,amount):
        before = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - before

    def eat(self,idx):
        food = FOOD[self.items.pop(idx)]
        heald = self.heal(food.heal)
        say(f"Yum! You ate {food.name}.")
        if heald == 0:
            say("HP is already full... why? but it was tasty. YUM!")
        elif self.hp == self.max_hp:
            say(f"HP fully restored! (+{heald})")
        else:
            say(f"You recovered {heald} HP!")

    def status(self):
        rule("-")
        say(f"{self.name}   HP {hp_bar(self.hp,self.max_hp)}")
        say(f"STRENGTH {self.strength} (muscle {self.muscle}/{XP_P_STRENGTH} to next)")
        w = WEAPON[self.weapon]
        say(f"WEAPON   {w.name} (+{w.dmg})    -> total ATK {self.attack}")
        arm = ARMOR[self.armor].name if self.armor else "none"
        say(f"ARMOR    {arm} (DEF {self.defense})")
        say(f"Kills: {self.kills}   Spared: {self.spares}")
        rule("=")