from math import floor

atp = 196
atk_type = 0.18
sharp = 1.30
hitzone = 0.80
defence = 1.0
rage = 1.0
var = 1.0
wep_class = 1.4

element = 520
esharp = 1.0625
elmzone = 0.30
divider = 10
elmvar = 1.0625

#HR + Monster check

#hitzone check - assume weakest area

#weapon class check. SnS/DS = 1.4 Lance/Gunlance = 2.3 GS/LS = 4.8 Hammer/HH = 5.2

#attack type check - assume strongest attack for now. add in support for averaging the attacks out later.

#raw sharpness check - Purple: 1.50, White: 1.30, Blue: 1.25, Green: 1.125, Yellow: 1.0, Orange: 0.75, Red: 0.50

#element check - is there one?

#

#raw damage formula
def melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, wep_class): 
    return ((atp * atk_type * sharp * hitzone * defence * rage * var) / wep_class)
 
#element damage formula
def element_calc(element, esharp, elmzone, divider):
    return ((element * esharp * elmzone) / divider)

raw_total = melee_calc(atp, atk_type, sharp, hitzone, defence, rage, var, wep_class)    

#raw_total = round(raw_total, 0)

print raw_total

elm_total = element_calc(element, esharp, elmzone, divider)

#elm_total = round(elm_total, 0)

print elm_total

total = floor(raw_total + elm_total)

print total
