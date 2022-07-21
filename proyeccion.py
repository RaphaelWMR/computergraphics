import math
from sympy.solvers import solve
from sympy import Symbol


def proyeccion():
    print("Proyeccion de punto")
    print("Digite la ecuacion del plano:\nAx+By+Cz+D=0")
    ap = float(input("A= "))
    bp = float(input("B= "))
    cp = float(input("C= "))
    dp = float(input("D= "))
    vdirector = [ap, bp, cp]
    print("Digite las coordenadas del punto (x,y,z)")
    x = float(input("x= "))
    y = float(input("y= "))
    z = float(input("z= "))
    xyz = [x, y, z]
    # interseccion
    xi = x + ap * vdirector[0]
    yi = y + bp * vdirector[1]
    zi = z + cp * vdirector[2]
    lam = Symbol("lam")
    lam = solve(
        ap * (xyz[0] + vdirector[0] * lam) + bp * (xyz[1] + vdirector[1] * lam) + cp * (
                    xyz[2] + vdirector[2] * lam) + dp)
    lam = lam[0]
    print(f"lam: {lam}")
    xyzpro = [xyz[0] + lam * vdirector[0], xyz[1] + lam * vdirector[1], xyz[2] + lam * vdirector[2]]
    print(f"P({xyz[0]},{xyz[1]},{xyz[2]}) => P'({xyzpro[0]},{xyzpro[1]},{xyzpro[2]})")


def distancia():
    print("Distancia entre dos puntos")
    p1 = []
    p2 = []
    print("P1(x1,y1,z3)")
    p1.append(float(input("x1= ")))
    p1.append(float(input("y1= ")))
    p1.append(float(input("z1= ")))
    print("P2(x2,y2,z2)")
    p2.append(float(input("x2= ")))
    p2.append(float(input("y2= ")))
    p2.append(float(input("z2= ")))
    d = math.sqrt(abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2 + abs(p1[2] - p2[2]) ** 2)
    print(f"Puntos: P1({p1[0]},{p1[1]},{p1[2]}),P2({p2[0]},{p2[1]},{p2[2]})")
    print(f"Distancia: {d}")


#proyeccion()
distancia()
