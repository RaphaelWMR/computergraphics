def simetria_punto_recta():
    print("Digite la recta: Ax+By+C=0")
    a = float(input("A="))
    b = float(input("B="))
    c = float(input("C="))
    print("Digite el punto: (x,y)")
    p = float(input("x="))
    q = float(input("y="))
    m = -a / b
    print(f"m: {m}")
    m = -1 / m
    print(f"m'={m}")
    x = -1 * (-b * m * p + b * q + c) / (a + b * m)
    y = (-c - a * x) / b
    print(f"Punto P({p},{q})")
    print(f"Punto de corte M({x},{y})")
    r = 2 * x - p
    s = 2 * y - q
    print(f"Punto P'({r},{s})")


simetria_punto_recta()
