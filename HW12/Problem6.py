from __future__ import division
from random import randrange
from z3 import *
import math

S = Solver()

n = input("Enter your value: ")


#n=4
#n=6



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


def switcher(solver,num):
    if num == 1:

#Defining constraints

		#phi_n_1
		for i in rows:
		     solver.add(Or(Q[i-1]))
	        #print("Adding constraint # 1")
    elif num == 2:	    
		#phi_n_2
		#print("Adding constraint # 2")
		for i in total.difference(rows):
		    solver.add(Or(R[i-1]))
    elif num == 3:
		#print("Adding constraint # 3")    
		#phi_n_3
		for i in total:
		    for j in total:
		        solver.add(Implies(Q[i-1][j-1], Not(R[i-1][j-1])))
    elif num == 4:
                #print("Adding constraint # 4")
		#phi_n_4
		for i in total:
		    for j in total:
		        solver.add(Implies(Q[i-1][j-1], And([And(Not(Q[i-1][k-1]), Not(R[i-1][k-1])) for k in total if (k != j)])))
    elif num == 5:
    	        #print("Adding constraint # 5")
		#phi_n_5
		for i in total:
		    for j in total:
		        solver.add(Implies(Q[j-1][i-1], And([And(Not(Q[k-1][i-1]), Not(R[k-1][i-1])) for k in total if k != j])))

    elif num == 6:
    	        #print("Adding constraint # 6")
		#phi_n_6
		for i in total:
		    for j in total:
		        solver.add(Implies(R[i-1][j-1], And([And(Not(R[i-1][k-1]), Not(R[i-1][k-1])) for k in total if k != j])))
    elif num == 7:
    	        #print("Adding constraint # 7")
		#phi_n_7
		for i in total:
		    for j in total:
		        solver.add(Implies(R[j-1][i-1], And([And(Not(R[k-1][i-1]), Not(R[k-1][i-1])) for k in total if k != j])))
    elif num == 8:
                #print("Adding constraint # 8")
                #phi_n_8
		for i in total:
		    for j in total:
		        solver.add(Implies(Q[i-1][j-1], And([And(Not(Q[l-1][k-1]), Not(R[l-1][k-1])) for l in total for k in total if ( (l != i) and (k != j) and (l + k == i + j)) ])))
    else:
                #print("Adding constraint # 9") 
		for i in total:
		    for j in total:
		        solver.add(Implies(Q[i-1][j-1], And([And(Not(Q[l-1][k-1]), Not(R[l-1][k-1])) for l in total for k in total if ( (l != i) and (k != j) and (l - k == i - j)) ])))


#define an experimental solver
all = [1,2,3,4,5,6,7,8,9]
# tmp = 0

# #Our honesty goodness :D


    
Z = []
Z1 = Solver()
Z.append(Z1)
Z2 = Solver()
Z.append(Z2)
Z3 = Solver()
Z.append(Z3)
Z4 = Solver()
Z.append(Z4)
Z5 = Solver()
Z.append(Z5)
Z6 = Solver()
Z.append(Z6)
Z7 = Solver()
Z.append(Z7)
Z8 = Solver()
Z.append(Z8)
Z9 = Solver()
Z.append(Z9)




for i in range(9):
    tmp=i+1
    for j in range(9):
        if(j+1 != tmp):
            #print()
            switcher(Z[i],j+1)
    first = Z[i].check()
    #print(first)
    if(first == sat):    
        model = Z[i].model()
        for k in range(n):
            for l in range(n):
                Z[i].add(Q[k][l] == model[Q[k][l]])
                Z[i].add(R[k][l] == model[R[k][l]])


        switcher(Z[i],tmp)
        second = Z[i].check()
        #print(second)
        if(second != first):
            print(i+1,"  is essential")
        else:
            print(i+1,"  is not essential")
            #         if(Z[i].check() != S.check()):
    # #     print(i+" essential")
    # print(Z[i].check())
    
    


# if Z.check() == unsat:
#     print("Unsat")
# else:
#     model = Z.model()
#     #model.sort()
#     #print(type(model))
#     print(model)
