from math import floor

#HR + Monster check
defence = 1.0
rage = 1.0
var = 1.0
#hitzone check - assume weakest area
hitzone = 0.80

#attack power

atp = raw_input("Attack Power of weapon: ")
#weapon class check. SnS/DS = 1.4 Lance/Gunlance = 2.3 GS/LS = 4.8 Hammer/HH = 5.2
wep_class_q = raw_input("What weapon are you using? (SnS, DS, Lance, Gunlance, Great Sword, Long Sword, Hammer, Hunting Horn) ")
if wep_class_q == "SnS" or wep_class_q == "DS":
    wep_class = 1.4
elif wep_class_q == "Lance" or wep_class_q == "Gunlance":
    wep_class = 2.3
elif wep_class_q == "Long Sword" or wep_class_q == "Great Sword":
    wep_class = 4.8
elif wep_class_q == "Hammer" or wep_class_q == "Hunting Horn":
    wep_class = 5.2


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
def melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, wep_class): 
    return ((atp * atk_type * sharp * hitzone * defence * rage * var) / wep_class)
 
#element damage formula
def element_calc(element, esharp, elmzone, divider):
    return ((element * esharp * elmzone) / divider)

raw_total = melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, wep_class)    

print raw_total

elm_total = element_calc(element, esharp, elmzone, divider)

print elm_total

total = floor(raw_total + elm_total)

print total
