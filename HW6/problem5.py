from z3 import *

S = Solver()

in_a_0 = Int('in_a_0')
out_a_0 = Int('out_a_0')
out_a_1 = Int('out_a_1')
out_a_2 = Int('out_a_2')
in_b_0 = Int('in_b_0')
out_b_0 = Int('out_b_0')



phi_a = And((out_a_0 == in_a_0), out_a_1 == (out_a_0 * in_a_0), out_a_2 == (out_a_1 * in_a_0))
phi_b = out_b_0 == (in_b_0 * in_b_0) * in_b_0


S.add( Not(
          Implies(
              And(
                 (in_a_0 == in_b_0), phi_a, phi_b
               ),
              out_b_0 == out_a_2
          )
       )
)

print(S.check())

