import numpy as np

m = np.array([
  [1, 2,  0],
  [0, 0,  5],
  [3, -4, 2],
  [1, 6,  5],
  [0, 1,  0]
])

U, s, W = np.linalg.svd(m)
D = np.zeros_like(m, dtype=float)
D[np.diag_indices(min(m.shape))] = s

print('U:', U)
print('W:', W)
print('D:', D)

print('Euclidean norm: ', np.linalg.norm(s))
print('Frobenius norm: ', np.linalg.norm(m, ord='fro'))