# K-means clustering algorithm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance

k = 5  # --PARAMETER

# --- Training points ---
# Read
data = pd.read_csv('data.csv')
samples_num = len(data)
data_np = np.concatenate((data.to_numpy(dtype='float64'),
                          np.zeros((samples_num,1),dtype='float64')),
                          axis=1)

print('data:\n',data_np)

# Plot data
fig1 = plt.figure()
plt.scatter(data_np[:,0], data_np[:,1])
fig1.suptitle('Data', fontsize=20)
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=16)
plt.grid(True)
fig1.savefig('data_plot.png')
plt.show()

# --------------- K-means Algo ---------------
# Initialisation
x_limits = np.array([min(data_np[:,0]), max(data_np[:,0])])
y_limits = np.array([min(data_np[:,1]), max(data_np[:,1])])
print('datapoints range: \n',x_limits,y_limits)

# Initial random centroids
centroids = np.zeros((k,2), dtype='float64') # centroids (rows:clusters, col: x,y)
for i in range(k):
  centroids[i,:] = [np.random.uniform(x_limits[0],x_limits[1]),
                    np.random.uniform(y_limits[0],y_limits[1])]
print('Initial centroids:\n', centroids)

cluster_avg = np.array([row[:] for row in centroids])         # avg coordinates of each cluster. (dims= clusters x 2)
dist = np.zeros((samples_num,k), dtype='float64')     # distances (rows: dist of each point, col: dist from each centroid)
convergence_flag = 0
img_i = 0

while(convergence_flag==0):
  img_i += 1
  # --Cluster Assignment--
  # print(data_np)
  for i in range(samples_num):
    # print(i)
    for j in range(k):
      # print(j)
      dist[i,j] = distance.euclidean(data_np[i,0:2], centroids[j,:])
  # print(dist)
  for i in range(len(dist)):
    data_np[i,2] = np.argmin(dist[i,:])

  # update clusters in dataframe
  # data_np = data.to_numpy(dtype='float64')
  # print('data = ',data)
  print('data_np\n', data_np)

  # --- Plot data and centroids ---
  fig = plt.figure()
  for i in range(k):
    plt.scatter(data_np[data_np[:,2]==i,0], data_np[data_np[:,2]==i,1], label='cluster '+str(i))
  plt.scatter(centroids[:,0], centroids[:,1], label='centroids')
  fig.suptitle('Clusters and Centroids (iteration'+str(img_i)+')', fontsize=20)
  plt.xlabel('x', fontsize=18)
  plt.ylabel('y', fontsize=16)
  plt.xlim(right=x_limits[1]+2)
  plt.legend(loc='upper right')
  plt.grid(True)
  fig.savefig('output'+str(img_i)+'.png')
  plt.show()
  
  # Moving Centroid
  for i in range(k):
    print('i= ',i)
    cluster_members_num = np.sum(data_np[:,2]==i)
    print('memebers = ',cluster_members_num)
    if (cluster_members_num!=0):
      cluster_avg[i] = np.sum(data_np[data_np[:,2]==i,0:2], axis=0)/cluster_members_num
  print('old centroids:\n', centroids)
  print('cluster_avg:\n', cluster_avg)

  # Convergence
  if (np.array_equal(centroids, cluster_avg)):
    convergence_flag = 1
    print('Convergence! We stop here.')
    print('new centroids = \n', cluster_avg, flush='True')
  else:
    centroids = np.array([row[:] for row in cluster_avg])
    print('new centroids = \n', centroids, flush='True')
# --------------------------------------------

