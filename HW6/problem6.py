from z3 import *

S = Solver()
def check_equal():
 f = open("demofile.txt", "r")
 #print(f.read())
 lines = f.readlines()
 #print(lines[0])
 in_a = lines[0]
 m = lines[1]
 in_b = lines[2]
 n = lines[3]

# z3_in_a = Int("in_a")
 z3_out_a = Int("out_a")
# z3_in_b = Int("in_b")
 z3_out_b = Int("out_b")

 # power
 out_a = 1
 for i in range(int(m)+1):
    out_a = out_a * int(in_a)
    
 z3_out_a = out_a

 
 # power_new
 out_b = int (in_b)
 for i in range(int(n)):
     out_b = out_b * out_b

 z3_out_b = out_b
     

 S.add(out_a == out_b)

# print(S.check())
 if (str(S.check()) == "sat"):
  return True
 else:
  if (str(S.check()) == "unsat"):
   return False

print(bool(check_equal()))
