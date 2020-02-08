# Algorithm of Nearest Neighbor Rule

# Implementation characteristics:
# 2 clusters
# k neighbors

from numpy import *
import pandas as pd
import matplotlib.pyplot as plt

k = 8  # --PARAMETER

# --- Training points ---
# Read
data = pd.read_csv('data.csv')
print (data)

# Split to clusters
cluster1 = data.loc[data['cluster'] == 1]
cluster2 = data.loc[data['cluster'] == 2]

# Plot
my_axis = cluster1.plot(kind='scatter', x='x', y='y', c='Green', label='Cluster 1')
cluster2.plot(kind='scatter', x='x',y='y',c='Red', label='Cluster 2', ax=my_axis)

# --- Test points ---
# Read
test_df = pd.read_csv('test.csv')
print (test_df)

# Plot
test_df.plot(kind='scatter', x='x', y='y', c='Blue', label='test points', ax=my_axis)
plt.grid(True)
plt.show()


# --------------- NN Algo ---------------
my_color = [] # this list wil contain the final clustering (output)

for i in range(len(test_df.iloc[:,0])):
  # --- Distances ---
  # initialize variables
  dist_list = []
  cluster_list = []
  index = 0

  # distance calculations with Manhattan distance
  print('--Points and their distances from the test point')
  for x,y in zip(data.iloc[:,0], data.iloc[:,1]):
      dist = abs(x - test_df.iloc[i,0]) + abs(y - test_df.iloc[i,1]) # Manhattan dist
      print(x, y)
      print(dist)
      dist_list.append(dist) # track distances
      cluster_list.append(data.iloc[index,2]) # track clusters
      index += 1
  dist_df = pd.DataFrame()
  dist_df['Distance'] = dist_list
  dist_df['Cluster'] = cluster_list
  print(dist_df)

  dist_df = dist_df.sort_values(by='Distance')
  print(dist_df)


  # --- Counters ---
  counter = []
  counter.append(0)
  counter.append(0)

  dist_df = dist_df.iloc[0:k,:] # keep the first k rows (i.e. only k nearest neighbors)
  for z in dist_df.iloc[:,1]:
      if z == 1 :
          counter[0] +=1 # cluster1
      elif z == 2:
          counter[1] +=1 # cluster2

  print('Counter1:',counter[0])
  print('Counter2:',counter[1])
  print('Test point goes to the cluster with the greatest counter.')

  if counter[0] >= counter[1]:
      my_color.append('Green')
  else:
      my_color.append('Red')


print('my_color = ', my_color)
# --------------- end of NN Algo ---------------

# --- Plot classified test points ---
test_df.plot(kind='scatter', x='x', y='y', c=my_color)
plt.grid(True)
plt.show()

# --- Plot all data ---
final_axis = cluster1.plot(kind='scatter', x='x', y='y', c='green', label='cluster 1')
cluster2.plot(kind='scatter', x='x',y='y',c='red', label='cluster 2', ax=final_axis)
test_df.plot(kind='scatter', x='x', y='y', c=my_color, ax=final_axis)
plt.grid(True)
plt.show()
