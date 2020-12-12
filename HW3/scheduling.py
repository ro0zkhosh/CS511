from z3 import *

S = Solver()

A = Int('A')
S.add(A >= 0)

At = Int('At')
S.add(At == 2)

B = Int('B')
S.add(B >= 0)

Bt = Int('Bt')
S.add(Bt == 1)

C = Int('C')
S.add(C >= 0)


Ct = Int('Ct')
S.add(Ct == 2)

D = Int('D')
S.add(D >= 0)

Dt = Int('Dt')
S.add(Dt == 2)

E = Int('E')
S.add(E >= 0)

Et = Int('Et')
S.add(Et == 7)

F = Int('F')
S.add(F >= 0)

Ft = Int('Ft')
S.add(Ft == 5)

End = Int('End')
S.add(End == 14)

S.add( Or( (A+At <= C), (C+Ct <= A) ) )
S.add( Or( (B+Bt <= D), (D+Dt <= B) ) )
S.add( Or( (B+Bt <= E), (E+Et <= B) ) )
S.add( Or( (D+Dt <= E), (E+Et <= D) ) )
S.add( And( (D+Dt <= F), (E+Et <= F) ) )
S.add( A+At <= B ) 
S.add( A <= End - At )
S.add( B <= End - Bt )
S.add( C <= End - Ct )
S.add( D <= End - Dt )
S.add( E <= End - Et )
S.add( F <= End - Ft )

print S.check()
print(S.model())
