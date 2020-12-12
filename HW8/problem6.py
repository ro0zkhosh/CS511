from z3 import *
Z = Solver()


# w = [100, 100, 100, 1, 100]
# c = [[0, 7, 1, 0, 8],
#      [7, 0, 5, 4, 3],
#      [1, 5, 0, 2, 6],
#      [0, 4, 2, 0, 1],
#      [8, 3, 6, 1, 0]]



f = open ( 'input.txt' , 'r')
w = []
c = []
l = [line.rstrip() for line in f]
w = eval("".join(l[0]))
c = eval("".join(l[1:]))

#w = f.readline().strip().split(",")
# print l
# print w
# print len(w)
# print c



Vars = []
Weight = Int("weight")
for i in range(len(w)):
     Vars.append(Int('x'+str(i)))
     Z.add(Or(Vars[i] == 1, Vars[i] == 0))

#print Vars

sum = 0
totWeight = 0
# for i in range(len(w)):
#         for j in range(i, len(w)):
#             sum = sum + c[i][j]*(Vars[i]*(1-Vars[j]) + (1 - Vars[i])*Vars[j])


for i in range(len(w)):
        for j in range(i, len(w)):
            sum = sum + c[i][j]*Vars[i]*Vars[j]
        totWeight = totWeight + (w[i] * Vars[i]) - ((1 + max(w)) * sum )







Z.add(Weight == totWeight)


if Z.check() == unsat:
    print("Unsat!")
else:
    
    while Z.check() == sat:
        sample = Z.model()
        Z.add(sample[Weight] < Weight )
        #print(sample)
    print sample



# if Z.check() == sat:
#         model = s.model()
#         s.add(total > model[total])
#         print(model)
