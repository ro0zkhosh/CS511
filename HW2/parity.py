from z3 import *

# declaring propositional variables
p1, p2, p3, p4 = Bools('p1 p2 p3 p4')

def lrarrow(p1, p2):
    return And(Implies(p1, p2), Implies(p2, p1))

CNF = And( Or(Not(p1), Not(p2), Not(p3), p4), Or(Not(p1), Not(p2), p3, Not(p4)), Or(Not(p1), p2, Not(p3), Not(p4)), Or(Not(p1), p2, p3, p4), Or(p1, Not(p2), Not(p3), Not(p4)), Or(p1, Not(p2), p3, p4), Or(p1, p2, Not(p3), p4), Or(p1, p2, p3, Not(p4)))

DNF = Or( And(p1,p2,p3,p4), And(p1,p2,Not(p3),Not(p4)), And(p1,Not(p2),p3,Not(p4)), And(p1,Not(p2),Not(p3),p4), And(Not(p1),p2,p3,Not(p4)), And(Not(p1),p2,Not(p3),p4), And(Not(p1),Not(p2),p3,p4), And(Not(p1),Not(p2),Not(p3),Not(p4)))


BICON = lrarrow(lrarrow(lrarrow(p1, p2), p3), p4)

s = Solver()
s.add(CNF != DNF)

s1 = Solver()
s1.add(DNF != BICON)

s2 = Solver()
s2.add(CNF != BICON)

print s.check()
print s1.check()
print s2.check()
