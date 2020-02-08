# Author: Pantelis Dimitroulis
# Title: Algorithm of Nearest Neighbor Rule

# Implementation characteristics:
# 2 clusters
# k neighbors

from numpy import *
import pandas as pd
import matplotlib.pyplot as plt

k = 3
# k = input('How many neighbors to consider? (K parameter)')

# --- Training points ---
data = pd.read_csv('data.csv')
print (data)

cluster1 = data.loc[data['cluster'] == 1]
cluster2 = data.loc[data['cluster'] == 2]

my_axis = cluster1.plot(kind='scatter', x='x', y='y', c='Green', label='Cluster 1')
cluster2.plot(kind='scatter', x='x',y='y',c='Red', label='Cluster 2', ax=my_axis)

# --- Test points ---
test_df = pd.read_csv('test.csv')
print (test_df)

test_df.plot(kind='scatter', x='x', y='y', c='Blue', label='test points', ax=my_axis)
plt.grid(True)
plt.show()

dist_list = []
cluster_list = []
index = 0

# Distance calculation
for x,y in zip(data.iloc[:,0], data.iloc[:,1]):
    dist = abs(x - test_df.iloc[0,0]) + abs(y - test_df.iloc[0,1])
    print(x, y)
    print('Distance=',dist)
    dist_list.append(dist)
    cluster_list.append(data.iloc[index,2])
    index += 1
dist_df = pd.DataFrame()
dist_df['Distance'] = dist_list
dist_df['Cluster'] = cluster_list
print(dist_df)

dist_df = dist_df.sort_values(by='Distance')
print(dist_df)

counter = []
counter.append(0)
counter.append(0)

dist_df = dist_df.iloc[0:k,:] # keep the first k rows
for z in dist_df.iloc[:,1]:
    if z == 1 :
        counter[0] +=1 # cluster1
    elif z == 2:
        counter[1] +=1 # cluster2

print('counter1:',counter[0])
print('counter2:',counter[1])

if counter[0] >= counter[1]:
    my_color = 'Green'
else:
    my_color = 'Red'
# --- Results - Plot ---
final_axis = cluster1.plot(kind='scatter', x='x', y='y', c='Green', label='Cluster 1')
cluster2.plot(kind='scatter', x='x',y='y',c='Red', label='Cluster 2', ax=final_axis)

test_df.plot(kind='scatter', x='x', y='y', c=my_color, ax=final_axis)
plt.grid(True)
plt.show()
