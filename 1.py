import numpy as np
from math import sqrt

def check_basis(*vectors):
  print('i j dot')
  for i in range(0, len(vectors)):
    for j in range(0, len(vectors)):
      a = np.array(vectors[i]);
      b = np.array(vectors[j]);
      print(i, j, a.dot(b))

check_basis([1,0,0],[0,0,1])
check_basis([1/sqrt(2),-1/sqrt(2), 0], [1/sqrt(2), 1/sqrt(2), 0], [0,0,1])
check_basis([1/2, -1/2, 0], [0, 1/2, 1/2], [0,0,1])
check_basis([1,0,0], [0,1,0], [0,0,1])