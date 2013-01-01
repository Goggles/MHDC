from math import floor

# example figures taken as Bone Shooter vs Giadrome
atp = 156
pwr = 0.06 * 0.01
bowgun_range = 1.5
crit = 1.25
hitzone = 10.0
defense = 1.0
rage = 1.0
bowgun_class = 1.2
dam = 0.0

element = 7
elem_hitzone = 0.6

def bowgun_calc(atp, pwr, bowgun_range, crit, hitzone, defense, rage, bowgun_class, dam):
    return ((atp * pwr * bowgun_range * crit * hitzone * defense * rage) / bowgun_class + (dam * defense))
    
def elem_bowgun_calc(element, elem_hitzone, defense, rage):
    return ((element * elem_hitzone * defense * rage)) / bowgun_class
    
raw_total = bowgun_calc(atp, pwr, bowgun_range, crit, hitzone, defense, rage, bowgun_class, dam)

print raw_total

elem_total = elem_bowgun_calc(element, elem_hitzone, defense, rage)

print elem_total

total = floor(raw_total + elem_total)

print total
