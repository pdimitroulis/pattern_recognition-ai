# Author: Pantelis Dimitroulis
# Title: Algorithm of BSAS

# Implementation characteristics:
# - theta: threshold

# Input:
# - norm_option: Type of distance (Norm1, Norm2 etc.)
# - theta
# - data.csv file: includes data points (x,y)

from numpy import *
import pandas as pd
from scipy.spatial import distance

######################################################################################
#----- INPUT ----#
theta = float(input('Threshold (theta): '))
norm_option = int(input('Distance calculation.\n 1.Manhattan distance\n 2.Euclidean distance\n Or any other number (Minkowski distance)\n Give a number:'))

df = pd.read_csv('data.csv')
#####################################################################################

#####################################################################################
#---- INITIALIZATION ----#
groups = {}
means = []
dist = []

data = df.values.tolist()
means.append(data[0])
groups.update({'1':[data[0]] })

print('\n', data, groups, means, dist,'\n')
#####################################################################################

#####################################################################################
#--- MAIN CODE ----#

# Iterate data points
for xtest in data[1:]:
    print('\n##### xtest: ', xtest)
    i = 0 # iterator of means
    # Iterate means
    for mean in means:
        print('--means: ', means)
        # Calculate distance
        curr_dist = distance.minkowski(mean, xtest, norm_option)
        dist.append(curr_dist)
        print('  distances: ', dist)
        if curr_dist < theta:
            # Find cluster
            cluster = i + 1
            print('  cluster: ', cluster)
            # Assign xtest to group
            groups[str(cluster)].append(xtest)
            break
        elif i == len(means) - 1:
            # Far from all means. Create new group
            cluster = int(list(groups.keys())[-1]) + 1
            groups.update({str(cluster) : [xtest]}) # Assign xtest to a new group
            means.append(xtest) # Set xtest as mean
            break
            print('  NEW group: ', cluster)
        i += 1
    print('Groups: ', groups)
    # Update corresponding mean
    means[cluster-1] = list(( array(means[cluster-1]) + array(xtest) ) / 2)
    del dist[:] # empty list in order to append

################################## END OF CODE ##################################
