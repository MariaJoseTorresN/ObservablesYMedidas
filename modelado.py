import retos as reto
import calculadoraMatrices as cM
import complejos as compl

def simulacion4_1():
    vectorKet = [[(-3, -1)], [(0, -2)], [(0, 1)], [(2, 0)]]
    ket1=[[(1,0)],[(0,-1)]]
    ket2 = [[(0, 1)], [(1, 0)]]
    prob = reto.probabilidadPosicion(2,vectorKet)
    ampl = reto.amplitudTransicionKet(ket1,ket2)
    print("Probabilidad de encontrar la particula en la posicion 2: ",prob)
    print("Amplitud transitar de ket 1 a ket 2: ",compl.redondear(ampl,2))
    print("Probabilidad de transitar de ket 1 a ket 2: ",reto.probabilidad(ampl))

def ejercicio4_3_1():
    sx = [[0,1],[1,0]]
    Sx = [[(0,0),(1,0)],[(1,0),(0,0)]]
    inicial = [(1,0),(0,0)]
    valores,vectores = reto.valoresPropios(sx)
    final = cM.accionMatrixVector(Sx,inicial)
    for i in range(len(final)):
        final[i] = [final[i]]
    print("Valores Propios: ",valores)
    print("Vectores Propios Normalizados: ",vectores)
    print("Estado Final: ", final)
    
def ejercicio4_3_2():
    sx = [[0,1],[1,0]]
    inicial = [[(1,0)],[(0,0)]]
    valores,vectores = reto.valoresPropios(sx)
    probabilidad = reto.probabilidadPropios(inicial,vectores)
    mean = reto.meanValue(probabilidad,valores)
    print("Probabilidad: ",probabilidad)
    print("Valor medio: ", mean)
    reto.grafica(probabilidad)

def ejercicio4_4_1():
    u1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    u2 = [[((2**0.5)/2,0),((2**0.5)/2,0)],[((2**0.5)/2,0),(-(2**0.5)/2,0)]]
    if cM.matrixUnitaria(u1) and cM.matrixUnitaria(u2):
        productoU1U2 = cM.productMatrix(u1,u2)
        productoU2U1 = cM.productMatrix(u2,u1)
        if cM.matrixUnitaria(productoU1U2) and cM.matrixUnitaria(productoU2U1):
            print("U1, U2 y el producto entre ambos son matrices unitarias")
    else:
        print("No son unitarias")
        
def ejercicio4_4_2():
    mapaUnitario=[[(0,0),(1/(2**0.5),0),(1/(2**0.5),0),(0,0)],[(0,1/(2**0.5)),(0,0),(0,0),(1/(2**0.5),0)],[(1/(2**0.5),0),(0,0),(0,0),(0,1/(2**0.5))],[(0,0),(1/(2**0.5),0),(-1/(2**0.5),0),(0,0)]]
    inicial = [[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
    if cM.matrixUnitaria(mapaUnitario):
        dinamica = reto.dinamica(3,mapaUnitario,inicial)
        for i in range(len(dinamica)):
            dinamica[i] = [dinamica[i]]
        print("Estado final despues de 3 time steps: ",dinamica)
        print("Probabilidad de encontar la bola cuantica en la posicion 3: ", reto.probabilidadPosicion(3,dinamica))
    else:
        print("Mapa no unitario")

def main():
    simulacion4_1()
    ejercicio4_3_1()
    ejercicio4_3_2()
    ejercicio4_4_1()
    ejercicio4_4_2()
main()
