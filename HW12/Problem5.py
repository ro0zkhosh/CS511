from __future__ import division
from random import randrange
from z3 import *
import math

S = Solver()

n = input("Enter your value: ")


#n=4
#n=6
#n=8


#Defining Queen variables

# Q = [[]]
# for i in range(n):
#     tmp = []
#     for j in range(n):
#          tmp.append(Bool("Q"+str(i+1)+","+str(j+1)))
#     Q.append(tmp)     
# #Defining Rook variables


# R = [[]]
# for i in range(n):
#     tmp = []
#     for j in range(n):
#          tmp.append(Bool("R"+str(i+1)+","+str(j+1)))
#     R.append(tmp)

# Variables
Q = [[Bool("Q" + str(i+1) + "," + str(j+1)) for j in range(n)] for i in range(n)]
R = [[Bool("R" + str(i+1) + "," + str(j+1)) for j in range(n)] for i in range(n)]



#Getting a random 
def getDistinctRandomNumbers(inclusiveMin, exclusiveMax, amount):
    result = set()
    while len(result) != amount:
        result.add(randrange(inclusiveMin, exclusiveMax))
    return result

#defining a dummy set
total = set()
for i in range(n):
    total.add(i+1)
#print(math.ceil(n/3))
rows = getDistinctRandomNumbers(1, n, math.ceil(n/3))



print(total)
print(rows)
#print(R)
print(total.difference(rows))



#Defining constraints

#phi_n_1
for i in rows:
     S.add(Or(Q[i-1]))
    
#phi_n_2
for i in total.difference(rows):
    S.add(Or(R[i-1]))

    
#phi_n_3
for i in total:
    for j in total:
        S.add(Implies(Q[i-1][j-1], Not(R[i-1][j-1])))

#phi_n_4
for i in total:
    for j in total:
                S.add(Implies(Q[i-1][j-1], And([And(Not(Q[i-1][k-1]), Not(R[i-1][k-1])) for k in total if (k != j)])))

#phi_n_5
for i in total:
    for j in total:
                S.add(Implies(Q[j-1][i-1], And([And(Not(Q[k-1][i-1]), Not(R[k-1][i-1])) for k in total if k != j])))


#phi_n_6
for i in total:
    for j in total:
                S.add(Implies(R[i-1][j-1], And([And(Not(R[i-1][k-1]), Not(R[i-1][k-1])) for k in total if k != j])))

#phi_n_7
for i in total:
    for j in total:
        S.add(Implies(R[j-1][i-1], And([And(Not(R[k-1][i-1]), Not(R[k-1][i-1])) for k in total if k != j])))

#phi_n_8
for i in total:
    for j in total:
        S.add(Implies(Q[i-1][j-1], And([And(Not(Q[l-1][k-1]), Not(R[l-1][k-1])) for l in total for k in total if ( (l != i) and (k != j) and (l + k == i + j)) ])))

#phi_n_9
for i in total:
    for j in total:
        S.add(Implies(Q[i-1][j-1], And([And(Not(Q[l-1][k-1]), Not(R[l-1][k-1])) for l in total for k in total if ( (l != i) and (k != j) and (l - k == i - j)) ])))



if S.check() == unsat:
    print("Unsat")
else:
    model = S.model()
    #model.sort()
    #print(type(model))
    print(model)
