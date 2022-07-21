import math
import numpy as np


def recta_simple(x0, y0, x1, y1):
    x = x0
    y = y0
    dx = x1 - x0
    dy = y1 - y0
    m = dy / dx
    b = y0 - 0 * x0
    print("Recta simple")
    a = round(y)
    print(f"({x},{y})\t{a}")
    for x in range(x0, x1 + 1, 1):
        y = m * x + b
        a = round(y)
        print(f"({x},{y})\t{a}")


def recta_dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    m = dy / dx
    y = y0
    x = x0
    print("Recta DDA")
    a = round(y)
    print(f"({x},{y})\t{a}")
    if (m < 1):
        for x in range(x0, x1 + 1, 1):
            y = y + m
            a = round(y)
            print(f"({x},{y})\t{a}")
    else:
        for y in range(y0, y1 + 1, 1):
            x = round(x + 1 / m)
            a = round(y)
            print(f"({x},{y})\t{a}")


def recta_punto_medio(x0, y0, x1, y1):
    print("Recta Punto Medio")
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x = x0
    y = y0
    print(f"({x},{y})\t{d}")
    while (x < x1):
        if (d <= 0):
            d = d + dE
            x = x + 1
        else:
            d = d + dNE
            x = x + 1
            y = y + 1
        print(f"({x},{y})\t{d}")


def circunferencia_fuerza_bruta(R):
    x = 0
    y = R
    print(f"({x},{y})")
    while (x < y):
        y = math.sqrt(R ** 2 - x ** 2)
        x = x + 1
        print(f"({x},{y})")


def circunferencia_parametrica(R):
    theta = math.pi / 4
    delta = 0.1
    while (theta < math.pi / 2):
        x = R * math.cos(theta)
        y = R * math.sin(theta)
        theta = theta + delta
        print(f"({x},{y})")


def circunferencia_punto_medio(R):
    x = 0
    y = R
    d = 5 / 4 - R
    print(f"({x},{y})")
    while (x < y):
        if (d < 0):  # Se escoge el Pixel E
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * (x - y) + 5
            x = x + 1
            y = y - 1
        print(f"({x},{y})")


def traslacion():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n)
    print("Vector de desplazamiento: ")
    d = []
    d.append(int(input("dx: ")))
    d.append(int(input("dy: ")))
    print(f"(dx,dy)=({d[0]},{d[1]})")
    for i in range(n):
        m[i][0] += d[0]
        m[i][1] += d[1]
    print("Resultado: ")
    imprimir_matriz(m)


def escalamiento():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n)
    print("Factor de escalamiento: ")
    e = []
    e.append(int(input("ex: ")))
    e.append(int(input("ey: ")))
    print(f"(ex,ey)=({e[0]},{e[1]})")
    for i in range(n):
        m[i][0] *= e[0]
        m[i][1] *= e[1]
    print("Resultado: ")
    imprimir_matriz(m)


def rotacion():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n)
    o = int(input("Angulo: "))
    o = math.radians(o)
    print(f"theta:{o}")
    cos = round(math.cos(o), 3)
    sin = round(math.sin(o), 3)
    print(f"cos={cos},sin={sin}")
    for i in range(n):
        x = m[i][0]
        y = m[i][1]
        m[i][0] = round(x * cos - y * sin, 3)
        m[i][1] = round(x * sin + y * cos, 3)
    print("Resultado: ")
    imprimir_matriz(m)


def hom_traslacion():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n)
    print("Vector de desplazamiento: ")
    d = []
    d.append(int(input("dx: ")))
    d.append(int(input("dy: ")))
    print(f"(dx,dy)=({d[0]},{d[1]})")
    t = np.array([[1, 0, d[0]], [0, 1, d[1]], [0, 0, 1]])
    print("tmatrix")
    print(t)
    for i in range(n):
        p = np.array([[m[i][0]], [m[i][1]], [1]])
        p1 = np.matmul(t, p)
        imprimir_producto_matrices(p1, t, p, i)


def hom_escalamento():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n)
    print("Factor de escalamiento: ")
    e = []
    e.append(int(input("ex: ")))
    e.append(int(input("ey: ")))
    print(f"(ex,ey)=({e[0]},{e[1]})")
    s = np.array([[e[0], 0, 0], [0, e[1], 0], [0, 0, 1]])
    print("tmatrix")
    print(s)
    for i in range(n):
        p = np.array([[m[i][0]], [m[i][1]], [1]])
        p1 = np.matmul(s, p)
        imprimir_producto_matrices(p1, s, p, i)


def hom_rotacion():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n)
    o = int(input("Angulo: "))
    o = math.radians(o)
    print(f"theta:{o}")
    cos = round(math.cos(o), 3)
    sin = round(math.sin(o), 3)
    print(f"cos={cos},sin={sin}")
    r = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    print("tmatrix")
    print(r)
    for i in range(n):
        p = np.array([[m[i][0]], [m[i][1]], [1]])
        p1 = np.matmul(r, p)
        imprimir_producto_matrices(p1, r, p, i)


def homogeneizacion():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n)
    op = int(input("1. Traslacion\n2. Escalamiento\n3. Rotacion\nDigite la opcion: "))
    if (op == 1):
        print("Vector de desplazamiento: ")
        d = []
        d.append(int(input("dx: ")))
        d.append(int(input("dy: ")))
        print(f"(dx,dy)=({d[0]},{d[1]})")
        mop = np.array([[1, 0, d[0]], [0, 1, d[1]], [0, 0, 1]])
    elif (op == 2):
        print("Factor de escalamiento: ")
        e = []
        e.append(int(input("ex: ")))
        e.append(int(input("ey: ")))
        print(f"(ex,ey)=({e[0]},{e[1]})")
        mop = np.array([[e[0], 0, 0], [0, e[1], 0], [0, 0, 1]])
    else:
        o = int(input("Angulo: "))
        o = math.radians(o)
        print(f"theta:{o}")
        cos = round(math.cos(o), 3)
        sin = round(math.sin(o), 3)
        print(f"cos={cos},sin={sin}")
        mop = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    for i in range(n):
        p = np.array([[m[i][0]], [m[i][1]], [1]])
        p1 = np.matmul(mop, p)
        imprimir_producto_matrices(p1, mop, p, i)


def transformaciones3d():
    n = int(input("Numero de puntos: "))
    m = llenar_matriz(n, 3)
    op = int(input("1. Traslacion\n2. Escalamiento\n3. Rotacion\nDigite la opcion: "))
    if (op == 1):
        print("Vector de desplazamiento: ")
        d = []
        d.append(int(input("dx: ")))
        d.append(int(input("dy: ")))
        d.append(int(input("dz: ")))
        print(f"(dx,dy)=({d[0]},{d[1]},{d[2]})")
        mop = np.array([[1, 0, 0, d[0]],
                        [0, 1, 0, d[1]],
                        [0, 1, 1, d[2]],
                        [0, 0, 0, 1]])
    elif (op == 2):
        print("Factor de escalamiento: ")
        e = []
        e.append(int(input("ex: ")))
        e.append(int(input("ey: ")))
        e.append(int(input("ez: ")))
        print(f"(ex,ey)=({e[0]},{e[1]},{e[2]})")
        mop = np.array([[e[0], 0, 0, 0],
                        [0, e[1], 0, 0],
                        [0, 0, e[2], 0]
                        [0, 0, 0, 1]])
    else:
        o = int(input("Angulo: "))
        o = math.radians(o)
        print(f"theta:{o}")
        cos = round(math.cos(o), 3)
        sin = round(math.sin(o), 3)
        print(f"cos={cos},sin={sin}")
        axis = int(input("Digite el eje\n1. x\n2. y\n3. z:"))
        if (axis == 1):
            mop = np.array([[1, 0, 0, 0],
                            [0, cos, -sin, 0],
                            [0, sin, cos, 0]
                            [0, 0, 0, 1]])
        elif (axis == 2):
            mop = np.array([[cos, 0, sin, 0],
                            [0, 1, 0, 0],
                            [-sin, 0, cos, 0]
                            [0, 0, 0, 1]])
        else:
            mop = np.array([[cos, -sin, 0, 0],
                            [sin, cos, 0, 0],
                            [0, 0, 1, 0]
                            [0, 0, 0, 1]])
    for i in range(n):
        p = np.array([[m[i][0]], [m[i][1]], [m[i][2]], [1]])
        p1 = np.matmul(mop, p)
        imprimir_producto_matrices(p1, mop, p, i)


def llenar_matriz(n, dim=2):
    m = []
    for i in range(n):
        m.append([0] * n)
    for i in range(n):
        m[i][0] = int(input(f"x{i + 1}: "))
        m[i][1] = int(input(f"y{i + 1}: "))
        if dim == 3:
            m[i][1] = int(input(f"z{i + 1}: "))
    if dim == 2:
        for i in range(n):
            print(f"(x{i + 1},y{i + 1})=({m[i][0]},{m[i][1]})", end="")
    elif (dim == 3):
        for i in range(n):
            print(f"(x{i + 1},y{i + 1},z{i + 1})=({m[i][0]},{m[i][1]},{m[i][2]})", end="")
    print("")
    return m


def imprimir_producto_matrices(p1, mop, p, i=-1):
    if i != -1:
        print(f"{i + 1}:({p[0][0]},{p[1][0]})->({p1[0][0]},{p1[1][0]})-----------------")
    print(mop)
    print("x")
    print(p)
    print("=")
    print(p1)


def imprimir_matriz(m):
    for i in range(len(m)):
        print(f"(x{i + 1}',y{i + 1}')=({m[i][0]},{m[i][1]})", end="\t")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # recta_simple(6, 9, 11, 12)
    # recta_dda(6, 9, 11, 12)
    # recta_punto_medio(8,10,15,15)
    # circunferencia_fuerza_bruta(10)
    # circunferencia_parametrica(10)
    # circunferencia_punto_medio(8)
    # traslacion()
    # escalamiento()
    rotacion()
# hom_traslacion()
# hom_escalamento()
# hom_rotacion()
# homogeneizacion()
# transformaciones3d()
