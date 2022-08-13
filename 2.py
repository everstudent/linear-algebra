import numpy as np


# 1.2 
a = np.array([[1, -2], [3, 0]])
b = np.array([[4, -1], [0, 5]])

print('A+B =')
print(a + b)

print('AB =')
print(a @ b)


# 1.3
a = np.array([[1,  7], [3, -6]])
b = np.array([[0,  5], [2, -1]])
c = np.array([[2, -4], [1,  1]])

print('3A-2B+4C =')
print(3*a - 2*b + 4*c)


# 1.4
a = np.array([[4, 1], [5, -2], [2, 3]])
print('AT =')
print(a.T)

print('A * AT =')
print(a @ a.T)

print('AT * A =')
print(a.T @ a)


# 1.5

def dot(a,b):
  if a.shape[0] == b.shape[1]:
    res = np.zeros((a.shape[0],b.shape[1]))
    for i in range(0, a.shape[0]):
      for j in range(0, b.shape[1]):
        v = 0
        for k in range(0, a.shape[1]):
          v += a[i][k]*b[k][j]
        res[i][j] = v
    return res;


a = np.array([[1,  7, 3], [3, -6, 4]])
b = np.array([[0,  5], [2, -1], [2, 5]])

print(a @ b)
print(dot(a, b))


# 2.2
a = np.array([[4, 2, 3], [0, 5, 1], [0, 0, 9]])
print('det(a) = ')
print(np.linalg.det(a))

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('det(a) = ')
print(np.linalg.det(a))

# 2.3
a = np.array([[-2, 7, -3], [4, -14, 6], [-3, 7, 13]])
print('det(a) = ')
print(np.linalg.det(a))

# 2.4
a = np.array([[-2, 7, -3], [4, -14, 6], [-3, 7, 13]])
print('rank(a) = ')
print(np.linalg.matrix_rank(a))

a = np.array([[0, 0, 2, 1], [0, 0, 2, 2], [0, 0, 4, 3], [2, 3, 5, 6]])
print('rank(a) = ')
print(np.linalg.matrix_rank(a))