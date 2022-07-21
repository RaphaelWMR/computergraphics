import math
import numpy as np


def imprimir_producto_matrices(m1, m2, p):
    print(m1)
    print("x")
    print(m2)
    print("=")
    print(p)


#  np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
# np.array([[1], [1], [1]])

o = math.radians(45)
cos = round(math.cos(o), 3)
sin = round(math.sin(o), 3)

#  m1 = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
'''
p = np.array([[-2], [0], [1]])

m1 = np.array([[cos, -sin, 0],
               [sin, cos, 0],
               [0, 0, 1]])
m2 = np.array([[1, 0, 2*math.sqrt(2)],
               [0, 1, 0],
               [0, 0, 1]])
m3 = np.array([[1, 0, 0],
               [0, 1, 2],
               [0, 0, 0]])'''

p = np.array([[1], [1], [1]])
m1 = np.array([[1, 0, 8],
               [0, 1, 5],
               [0, 0, 1]])
m2 = np.array([[-2, 0, 0],
               [0, -3 / 2, 0],
               [0, 0, 1]])
m3 = np.array([[1, 0, -1],
               [0, 1, -1],
               [0, 0, 1]])
# multiplicar
m = np.matmul(m1, m2)
m = np.matmul(m, m3)
print(m)
m = np.matmul(m, p)
print(m)
# sumar
# p = np.add(m1, m2)
# restar
# p = np.subtract(m1, m2)

# imprimir_producto_matrices(m1, m2, p)
