# Author: Pantelis Dimitroulis
# Title: Decision Tree (Pattern Recognition Book p. 237)

# Implementation characteristics:
# -

# Input:
# - data.csv file

#####################################################################################
#----- LIBRARIES ----#
from numpy import *
import pandas as pd
from scipy.spatial import distance
from pprint import pprint
import matplotlib.pyplot as plt
#####################################################################################
#####################################################################################
#----- INPUT & INITIALIZATION ----#
data = pd.read_csv('data.csv')

# Devide Clusters
cluster1 = data.loc[data['cluster'] == 1]
cluster2 = data.loc[data['cluster'] == 2]

# Plot cluster points
my_axis = cluster1.plot(kind='scatter', x='x', y='y', c='Green', label='Cluster1')
cluster2.plot(kind='scatter', x='x', y='y', c='Red', label='Cluster2', ax=my_axis)

plt.grid(True)
# plt.show()

print('\n--- Isolate points of ONE cluster at a time ---')

#####################################################################################

##########################################################################################
#----- FUNCTIONS -----#
def decision(data, my_axis):
    division_str = input('\nPlease give division (Only \'>\', e.g. \'x>0.5\', \'y>3\'): ')

    #--- Input Parsing --
    div_coord = division_str[0]
    div_op = division_str[1]
    div_coeff = float(division_str[2:])

    print(division_str,div_coord,div_op,div_coeff)
    #--- End: Input Parsing ---

    #--- Make Decision ---
    max_abs_x = abs(data['x']).max()*1.2
    max_abs_y = abs(data['y']).max()*1.2

    if div_coord == 'x':
        my_axis.vlines(div_coeff, -max_abs_y, max_abs_y, color='Black')
    else:
        my_axis.hlines(div_coeff, -max_abs_x, max_abs_x, color='Black')
    #------- Divide data ------
    data_1 = data.loc[data[div_coord] > div_coeff]
    data_2 = data.loc[data[div_coord] <= div_coeff]


    if (data_1.loc[data_1['cluster'] != 1].shape[0] == 0) or (data_1.loc[data_1['cluster'] != 2].shape[0] == 0): # Points of ONLY one cluster (LEAF)
        if (data_1.iloc[0,2] == 1): # Which cluster?
            color = '#abebc6' # Light Green
        else:
            color = '#f5b7b1' # Light Red
        data_1.plot(x='x', y='y', kind='scatter', c=color, ax=my_axis)
    else:
        decision(data_1, my_axis)

    if(data_2.loc[data_2['cluster'] != 1].shape[0] == 0) or (data_2.loc[data_2['cluster'] != 2].shape[0] == 0): # Points of ONLY one cluster (LEAF)
        if (data_2.iloc[0,2] == 1): # Which cluster?
            color = '#abebc6' # Light Green
        else:
            color = '#f5b7b1' # Light Red
        data_2.plot(x='x', y='y', kind='scatter', c=color, ax=my_axis)
        return()
    else:
        decision(data_2, my_axis)

##########################################################################################

#####################################################################################
#--- MAIN CODE ----#
# Parse division input

decision(data, my_axis)

plt.grid(True)
plt.show()

#################################### END OF MAIN CODE ####################################

##########################################################################################
#===================================== END OF FILE =====================================#
##########################################################################################
