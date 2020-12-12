from z3 import *

t = Int('t')
x = Bool('x')
y = Bool('y')
z = Bool('z')

phi = Or (And(x,y), And(x,z), And(y,z))
psi = And (Or(x,y), Or(x,z), Or(y,z))

s = Solver()
s.add(phi != psi)

print s.check()
