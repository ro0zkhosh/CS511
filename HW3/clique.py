from z3 import *

# Define Graph config

#N = int(input()) #Number of nodes
#Graph = []

Graph = [
    (1, 2, [2, 3, 4, 5]),
    (2, 4, [1, 4]),
    (3, 4, [1, 5]),
    (4, 7, [1, 2, 5]),
    (5, 7, [1, 3, 4])
]

Graph.sort()

#print(Graph)
adjMatrix = []
weightArray = []


for i in range(len(Graph)):
    adjMatrix.append([0 for i in range(len(Graph))])
    weightArray.append(0)
#print(adjMatrix)

 # Add edges
def add_edge(v1, v2):
    if v1 == v2:
        print("Same vertex %d and %d" % (v1, v2))
    adjMatrix[v1][v2] = 1
    adjMatrix[v2][v1] = 1

#print(Graph)
   
    
for i in range (len(Graph)):
    for j in Graph[i][2]:
        #print([i+1,j])
        add_edge(i, j-1)
    weightArray[i] = Graph[i][1]

#print(adjMatrix)
print (weightArray)

def is_connected(v1,v2):
    if (adjMatrix[v1][v2] == 1):
        return 1
    else:
        return 0

S = Solver()
    
# Bitmap correspond to nodes.
# If some node i exists in the clique, it's bit will be 1
# Initially it's empty
clique = []

char_list = [] 
alpha = 'a'
# for i in range(0, len(Graph)):
#     char_list.append(alpha)
#     alpha = chr(ord(alpha) + 1) 


for i in range(len(Graph)):
    char_list.append(alpha)
    alpha = chr(ord(alpha) + 1) 
    clique.append(Int(char_list[i]))

#print(char_list)
#print(clique)

#clique makes sence for 3 or more nodes.
#Counting number of nodes in clique        
numNodes = Int('numNodes');
counter = 0;
for i in range (len(Graph)):
        counter = sum(clique)

S.add(numNodes == counter)
S.add(numNodes > 2)



# Each node is either in the clique or not.
for i in range(len(Graph)):
    S.add(Or(clique[i] == 1, clique[i] == 0))

# Each node in the clique should be connected to others.
for i in range (len(Graph)):
    for j in range(i+1, len(Graph)):
        #Two nodes, i and j are in the clique if:
        #Both have their bits set then they are connected
        # clique[i] & clique[j] => edge(i,j)
        #print(is_connected(i,j))
        S.add(Or( clique[i] == 0, clique[j] == 0, And(clique[i] == 1, clique[j] == 1, is_connected(i,j) == 1 )))

sum =0
for i in range (len(Graph)):
    sum = weightArray[i] * clique[i] + sum
#print(sum)


cliqueWeight = Int('cliqueWeight')
S.add(cliqueWeight > 0)
S.add(cliqueWeight == sum)


S.check()
#print(S.model())

curMax = 0
#going through all potential models:
while S.check() == sat:
    #print S.model()
    model = S.model()
    #print(model[cliqueWeight])
    curMax = model[cliqueWeight]
    #print (curMax)
    S.add(cliqueWeight > curMax)

print(model)
