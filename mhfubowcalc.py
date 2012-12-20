from math import floor

# example figures from Dragonhead Harp III vs Rathalos
atp = 240
charge = 1.5
arrow = 0.12
bow_range = 1.5
hitzone = 0.55
defence = 1.0
rage = 1.0


element = 300
elem_charge = 1.0
elem_hitzone = 0.30


def bow_calc(atp, arrow, bow_range, charge, hitzone, defence, rage): 
    return ((atp * arrow * bow_range * charge * hitzone * defence * rage) / 1.2)

def elem_bow_calc(element, elem_charge, elem_hitzone, defence, rage):
    return((element * elem_charge * elem_hitzone * defence * rage) / 10)

raw_total = bow_calc(atp, arrow, bow_range, charge, hitzone, defence, rage)    

print raw_total

elm_total = elem_bow_calc(element, elem_charge, elem_hitzone, defence, rage)

print elm_total

total = floor(raw_total + elm_total)

print total
