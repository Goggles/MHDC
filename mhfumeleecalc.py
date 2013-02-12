from math import floor
from itertools import chain

#: The weapon classes
WEAPON_CLASSES = {
    1.4: ("Sword and Shield", "SS", "Dual Swords", "DS"),
    2.3: ("Lance", "L", "Gunlance", "GL"),
    4.8: ("Long Sword", "LS", "Great Sword", "GS"),
    5.2: ("Hammer", "H", "Hunting Horn", "HH"),
}

#: Each of the short weapon identifiers
WEAPON_CLASS_IDS = [w for w in chain(*WEAPON_CLASSES.values()) if len(w) <= 2]

def select_weapon_class(name):
    """Select a weapon class from a given name"""
    for weapon_class, weapon_names in WEAPON_CLASSES.items():
        if name in weapon_names:
            return weapon_class

    # Raise an error if a nonexisted weapon was selected
    raise KeyError("Selected weapon does not exist ({})".format(weapon))

def melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, weapon_class):
    """Calculates the melee damage"""
    damage = (atp * atk_type * sharp * hitzone * defence * rage * var)
    return damage / select_weapon_class(weapon_class)

def element_calc(element, esharp, elmzone, divider):
    """Calculates the elemental damage"""
    return ((element * esharp * elmzone) / divider)

def total(melee, elemental):
    """The total damage"""
    return floor(raw_total + elm_total)

#HR + Monster check
defence = 1.0
rage = 1.0
var = 1.0
#hitzone check - assume weakest area
hitzone = 0.80

#attack power

print "What is the attack power of the weapon: "
atp = int(raw_input("> "))

print "What is the weapons class?", "[" + ", ".join(WEAPON_CLASS_IDS) + "]"
weapon_class = raw_input("> ")

#attack type check - assume strongest attack for now. add in support for averaging the attacks out later.
atk_type = 0.18
#raw sharpness check - Purple: 1.50, White: 1.30, Blue: 1.25, Green: 1.125, Yellow: 1.0, Orange: 0.75, Red: 0.50
sharp = 1.30
#element check - is there one?
element = 520
#derive elemental sharpness from raw sharpness
esharp = 1.0625

#elmzone
elmzone = 0.30

#divider is always 10.

divider = 10

#elmvar
elmvar = 1.0625

raw_total = melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, weapon_class)    
elm_total = element_calc(element, esharp, elmzone, divider)

print
print "Total melee damage:", raw_total
print "Total elemental damage:", elm_total
print "Total damage:", total(raw_total, elm_total)
