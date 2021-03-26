import math
#a=a[0]+a[1]i
#b=b[0]+b[1]i

def complexToStr(c):
    return str(c[0]) + "+" + str(c[1]) + "i"

def suma(a,b):
    return a[0] + b[0], a[1] + b[1]

def resta (a,b):
    return a[0] - b[0], a[1] - b[1]

def producto(a,b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]

def division(a,b):
    x = (a[0]*b[0] + a[1]*b[1]) / (b[0]**2 + b[1]**2)
    y = (b[0] * a[1] - a[0] * b[1]) / (b[0]**2 + b[1]**2)
    return x, y

def conjugado(c):
    return c[0], -c[1]

def redondear(c,decimales):
    return round(c[0],decimales), round(c[1],decimales)

def modulo(c):
    return round((c[0]**2 + c[1]**2)**(1/2),2)

def polarCartesiano(c):
    return round(c[0]*math.cos(math.radians(c[1])),2),round(c[0]*math.sin(math.radians(c[1])),2)

def fase(c):
    return round(math.degrees(math.atan(c[1] / c[0])),2)

def cartesianoPolar(c):
    return round(modulo(c),2),round(fase(c),2)
