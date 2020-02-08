# Author: Pantelis Dimitroulis
# Title: Agglomerative Algorithm (Proximity Matrix) (Pattern Recognition Book p. 562)

# Implementation characteristics:
# - Matrix of dissimilarity

# Input:
# - data.csv file

######################################################################################
#----- LIBRARIES ----#
from numpy import *
from pandas import read_csv
from scipy.spatial import distance
from pprint import pprint
######################################################################################

######################################################################################
#----- INPUT ----#
norm_option = int(input('\nDistance calculation?\n 1.Manhattan distance\n 2.Euclidean distance\n Or any other number (Minkowski distance)\n Give a number: '))
complete_link = int(input('\nComplete link?\n 0. NO\n 1. YES\n Give a number: '))
df = read_csv('data.csv')
#####################################################################################

#####################################################################################
#---- INITIALIZATION ----#
P = [] #Proximity matrix
temp_vector = []
D = df.values.tolist()
Groups = df.values.tolist() # 2D list for groups

# Initialize P (Proximity Matrix)
for i in range(len(D)):
    for j in range(len(D)):
        temp_vector.append(distance.minkowski(D[i],D[j],norm_option))
    P.append(list(around(temp_vector,decimals=2))) # P[i] = temp_vector
    del temp_vector[:]

print(D,'\n')
pprint(P)
#####################################################################################


#####################################################################################
#--- MAIN CODE ----#
while(len(P)>1):

    # Find P's minimum
    p_list = []
    for j in range(len(P)):
        p_list = p_list + P[j] #create a sequence of all values
    P_array = array(p_list)
    index = p_list.index(min(P_array[nonzero(P_array)]))
    i = index // len(P)
    j = index % len(P)

    # Calculate 2 distance sums (of the two points i and j)
    sum_i = sum(P[i][:])
    sum_j = sum(P[:][j])

    print('')
    print(index,len(P))
    print(i,j)
    print(sum_i,sum_j)

    # Decrease Proximity Matrix - Single Link (Case 1)
    if (sum_i <= sum_j and not complete_link) or (sum_i >= sum_j and complete_link): # Swap i,j
        temp = i
        i = j
        j = temp

    # Remove i row and column
    P = P[:i] + P[i+1:]   #remove row
    for k in range(len(P)):
        del P[k][i]     #remove column

    # Merget i to j
    Groups[j] = Groups[j] + Groups[i]
    Groups = Groups[:i] + Groups[i+1:]

    print('step done!')
    print('Groups', Groups)
    pprint(P)

################################## END OF CODE ##################################
#####################################################################################
