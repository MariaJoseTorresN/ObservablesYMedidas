import complejos as compl
import calculadoraMatrices as cM
import numpy as np
import math
from matplotlib import pyplot as plt

"""Funcion que calcula la probabilidad de encontrar una particula en una posicion"""
def probabilidadPosicion(posicion,vectorKet):
    return (compl.modulo(vectorKet[posicion][0])**2)/cM.normaVec(vectorKet)**2

"""Funcion que calcula la amplitud al transitar de un vector a otro"""
def amplitudTransicionKet(ket1,ket2):
    bra = cM.adjMatrix(ket2)
    amplitud = cM.productMatrix(bra,ket1)[0][0]
    norma1 = cM.normaVec(ket1)
    norma2 = cM.normaVec(ket2)
    ans = compl.division(amplitud,compl.producto((norma1,0),(norma2,0)))
    return ans
"""Funcion que calcula la probabilidad, se implementa para sacar la probabilidad
de la amplitud al transitar de un vector a otro pero se puede usar cuando sea prudente"""
def probabilidad(c):
    return compl.modulo(c)**2

"""Funcion que calcula el valor esperado (media) y la varianza"""
def valorEsperadoYVarianza(matriz, ket):
    if cM.matrixHermitiana(matriz):
        bra = cM.adjMatrix(cM.productMatrix(matriz,ket))[0]
        for i in range(len(bra)):
            bra[i]=[(bra[i])]
        mu = cM.productMatrix(cM.transMatrix(bra), ket)[0][0]
        x = cM.escalarMultMatrix(mu,cM.matrixIdentidad(len(matriz)))
        y = cM.adiMatrix(matriz,cM.inverMatrix(x))
        cuadrado = cM.productMatrix(y,y)
        var = cM.productMatrix(cM.productMatrix(cM.adjMatrix(ket), cuadrado),ket)[0][0]
        ans = mu,var
    else:
        ans = "Matriz no hermitiana"
    return ans

"""Funcion que calcula los vectores normalizados y valores propios de un observable.
El observable se escribe con de fila a fila y el numero imaginario debe ir con un multiplo y j"""
def valoresPropios(observable):
    matriz = np.array(observable)
    propios = np.linalg.eig(matriz)
    valores, vectores = [], []
    for i in range(len(propios[0])):
        valores += [(propios[0][i].real,propios[0][i].imag)]
    
    for j in range(len(propios[1])):
        vect = []
        for k in range(len(propios[1][j])):
            vect += [[(propios[1][j][k].real,propios[1][j][k].imag)]]
        vectores += [vect]
    vectNormalizado = []
    for h in range(len(vectores)):
        vectNormalizado += normalizarVector(vectores[h])
    return valores, vectNormalizado

"""Funcion que normaliza un vector"""
def normalizarVector(vector):
    vectorNormalizado, v = [], []
    norma = cM.normaVec(vector)
    for i in range(len(vector)):
        v+=[compl.producto((1/norma,0),vector[i][0])]
    vectorNormalizado += [v]
    return vectorNormalizado

"""Funcion que calcula la probabilidad de que el sistema transite a un vector propio"""
def probabilidadPropios(vectorEstado,vectorPropio):
    prob = []
    bra = cM.adjMatrix(vectorEstado)[0]
    for i in range(len(bra)):
        bra[i]=[(bra[i])]
    for j in range(len(vectorPropio)):
        prob += [((compl.modulo(cM.productMatrix(cM.transMatrix(bra), vectorPropio)[0][0]))**2,0)]
    return prob

"""Funcion que calcula el valor medio usando la probabilidad y los valores propios"""
def meanValue(probabilidad,valoresPropios):
    mean, ans = [], (0,0)
    for i in range(len(probabilidad)):
        mean += [compl.producto(probabilidad[i],valoresPropios[i])]
    for j in range(len(mean)):
        ans = compl.suma(mean[i],ans)
    return ans
"""Funcion para graficar las probabilidades"""
def grafica(v):
    prob = [i for i in range(len(v))]
    vector = [v[i][0] for i in range(len(v))]
    plt.bar(prob,vector,color="#FF0080")
    plt.show()

"""Funcion que calcula el estado final de una matriz unitaria (dinamica)"""
def dinamica(steps,matriz,estadoInicial):
    if cM.matrixUnitaria(matriz):
        if steps == 1:
            ans = cM.productMatrix(matriz,estadoInicial)[0]
        else:
            for i in range(steps):
                matriz = cM.productMatrix(matriz,matriz)
            ans = cM.productMatrix(matriz,estadoInicial)[0]
    return ans
            
    
def main1():
    """vectorKet = [[(-3, -1)], [(0, -2)], [(0, 1)], [(2, 0)]]
    ans = probabilidadPosicion(2,vectorKet)
    ket1=[[(1,0)],[(0,-1)]]
    ket2 = [[(0, 1)], [(1, 0)]]
    res = amplitudTransicionKet(ket1,ket2)
    print(ans)
    print(compl.redondear(res))
    print(probabilidad(res))
    matriz=[[(1,0),(0,-1)],[(0,1),(2,0)]]
    ket=[[((2 ** 0.5) / 2, 0)], [(0, (2 ** 0.5) / 2)]]
    print(valorEsperadoYVarianza(matriz,ket))
    x=[[(0,0),(0,-1)],[(0,1),(0,0)]]
    y=[[(1 / 2 ** 0.5, 0)], [(0, 1 / 2 ** 0.5)]]
    z=valorEsperadoYVarianza(x, y)
    print(compl.redondear(z[0]))
    print(compl.redondear(z[1]))
    print(z)"""
    observable = [[-1,-1j],[1j,1]]
    x = valoresPropios(observable) 
    print(x)
    #v=[[(0.9238795325112867, 0.0)],[(-0.0, -0.3826834323650897)]]
    #norma= cM.normaVec(v)
    #h=normalizarVector(v)
    #print(h)
    vectorEstado = [[(1/2,0)],[(1/2,0)]]
    print(x[1][0])
    aja=cM.productMatrix(cM.transMatrix(vectorEstado), x[1])[0][0]
    ajaa=(compl.modulo(aja))**2
    print(ajaa)
    mu=[[(0.9238795325112867, 0.0)], [(0.0, -0.3826834323650897)]]
    jaja=cM.prodIntVec(vectorEstado,mu)
    jajas=(compl.modulo(jaja))**2
    print(jajas)
    t=[[(0.0, -0.3826834323650898)], [(0.9238795325112867, 0.0)]]
    tt=cM.prodIntVec(vectorEstado,t)
    ttt=(compl.modulo(tt))**2
    print(ttt)
    print(probabilidadPropios(vectorEstado,x[1]))
    #bra = cM.adjMatrix(vectorEstado)[0]
    #print(bra)
    #sep=probabilidadPropios(vectorEstado,x[1])
    #print(sep)
    """ex=[[(2,-3)],[(1,2)]]
    qu=cM.normaVec(ex)
    print(qu)
    ptr=compl.producto((1/qu,0),(1,2))
    print(ptr)
    print(ex[0][0])
    po,pos = [],[]
    for i in range(len(ex)):
        po += [[compl.producto((1/qu,0),ex[i][0])]]
    pos += po
    print(pos)
    print(normalizarVector(ex))"""

def main2():
    m=[[(0,0),(1/(2**0.5),0),(1/(2**0.5),0),(0,0)],[(1/(2**0.5),0),(0,0),(0,0),(-1/(2**0.5),0)],[(1/(2**0.5),0),(0,0),(0,0),(1/(2**0.5),0)],[(0,0),(-1/(2**0.5),0),(1/(2**0.5),0),(0,0)]]
    ma=[[(0,0),(1,0)],[(1,0),(0,0)]]
    mat=[[((2**0.5)/2,0),((2**0.5)/2,0)],[((2**0.5)/2,0),(-(2**0.5)/2,0)]]
    uni = cM.matrixUnitaria(mat)
    um=[[(0,0),(1/(2**0.5),0),(1/(2**0.5),0),(0,0)],[(0,1/(2**0.5)),(0,0),(0,0),(1/(2**0.5),0)],[(1/(2**0.5),0),(0,0),(0,0),(0,1/(2**0.5))],[(0,0),(1/(2**0.5),0),(-1/(2**0.5),0),(0,0)]]
    uninew = cM.matrixUnitaria(um)
    print(uninew)
    e = [[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
    print(dinamica(3,um,e))






