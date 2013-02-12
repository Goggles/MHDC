from math import floor
from itertools import chain

#: The weapon classes
WEAPON_CLASSES = {
    1.4: ("Sword and Shield", "SnS", "Dual Swords", "DS"),
    2.3: ("Lance", "L", "Gunlance", "GL"),
    4.8: ("Long Sword", "LS", "Great Sword", "GS"),
    5.2: ("Hammer", "H", "Hunting Horn", "HH"),
}

#: Each of the short weapon identifiersdddddd
WEAPON_CLASS_IDS = [w for w in chain(*WEAPON_CLASSES.values()) if len(w) <= 2]

#HR + Monster check
defence = 1.0
rage = 1.0
var = 1.0
#hitzone check - assume weakest area
hitzone = 0.80

#attack power

print "What is the attack power of the weapon: "
atp = int(raw_input("> "))

def input_weapon_class():
    print "What is the weapons class?"
    weapon = raw_input("[{}] > ".format(", ".join(WEAPON_CLASS_IDS)))
    
    # Find the weapon that has been selected
    for weapon_class, weapon_names in WEAPON_CLASSES.items():
        if weapon in weapon_names:
            return weapon_class

    # Raise an error if a nonexisted weapon was selected
    raise KeyError("Selected weapon does not exist ({})".format(weapon))

weapon_class = input_weapon_class()

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

#raw damage formula
def melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, weapon_class):
    return ((atp * atk_type * sharp * hitzone * defence * rage * var) / weapon_class)
 
#element damage formula
def element_calc(element, esharp, elmzone, divider):
    return ((element * esharp * elmzone) / divider)

raw_total = melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, weapon_class)    

print raw_total

elm_total = element_calc(element, esharp, elmzone, divider)

print elm_total

total = floor(raw_total + elm_total)

print total
