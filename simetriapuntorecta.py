def simetria_punto_recta():
    print("Digite la recta: Ax+By+C=0")
    a = float(input("A="))
    b = float(input("B="))
    c = float(input("C="))
    print("Digite el punto: (x,y)")
    p = float(input("x="))
    q = float(input("y="))
    if (a == 0):
        r = p
        s = q + 2 * (-c - q)
    else:
        m = b / a
        print(f"m'={m}")
        x = -1 * (-b * m * p + b * q + c) / (a + b * m)
        y = (-c - a * x) / b
        r = 2 * x - p
        s = 2 * y - q
        print(f"Punto P({p},{q})")
        print(f"Punto de corte M({x},{y})")

    print(f"Punto P'({r},{s})")

simetria_punto_recta()
