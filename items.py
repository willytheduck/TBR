from dataclasses import dataclass

@dataclass
class Weapon:
    name: str
    dmg: int
    desc: str

@dataclass
class Armor:
    name: str
    defense: int
    desc: str

@dataclass
class Food:
    name: str
    heal: int 
    desc: str

WEAPON = {
    "stick":    Weapon("Stick", 1, "Its bark is worse than its bite."),
    "toy_knife": Weapon("Toy Knife", 3, "Made of plastic. A rarity nowadays."),
    "ballet_shoes": Weapon("Ballet Shoes", 7, "These used shoes make you feel incredibly dangerous."),
    "burnt_pan": Weapon("Burnt Pan", 10, "Damage is rather consistent. Consumable items heal four more HP."),
    "empty_gun": Weapon("Empty Gun", 12, "An antique revolver. It has no ammo. Must be used precisely, or damage will be low."),
    "worn_dagger": Weapon("Worn Dagger", 15, "Perfect for cutting plants and vines."),
    "real_knife": Weapon("Real Knife", 25, "Here we are!"),
}

ARMOR = {
    "bandage": Armor("Bandage", 1, "It has already been used several times."),
    "ribbon": Armor("Faded Ribbon", 3, "If you're cuter, monsters won't hit you as hard."),
    "bandanna": Armor("Manly Bandanna", 7, "It has seen some wear. It has abs drawn on it."),
    "tutu": Armor("Old Tutu", 10, "Finally, a protective piece of armor."),
    "glasses": Armor("Cloudy Glasses", 5, "Glasses marred with wear."),
}

FOOD = {
    "monster_candy": Food("Monster Candy", 10, "Has a distinct, non-licorice flavor."),
    "spider_dont": Food("Spider Dont", 12, "A donut made with Spider Cider in the batter."),
    "nice_cream": Food("Nice Cream", 15, "Instead of a joke, the wrapper says something nice."),
    "hot_dog": Food("Hot Dog", 20, "The 'meat' is made of something called a 'water sausage'."),
    "glamburger": Food("Glamburger", 27, "A hamburger made of edible glitter and sequins."),
    "legendary_hero": Food("Legendary Hero", 40, "Sandwich shaped like a sword."),
    "butterscotch": Food("Butterscotch", 999, "Butterscotch-cinnamon pie, one slice."),
}