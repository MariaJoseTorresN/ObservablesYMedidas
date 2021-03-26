import complejos as comp

def adiVect(a,b):
    ans = []
    for i in range(len(a)):
        ans = ans + [comp.suma(a[i],b[i])]
    return ans

def inverVect(a):
    ans = []
    for i in range(len(a)):
        escalar = (-1,0)
        ans = ans + [comp.producto(escalar,a[i])]
    return ans

def escalarMultVect(escalar,a):
    ans = []
    for i in range(len(a)):
        ans = ans + [comp.producto(escalar,a[i])]
    return ans

def verificacionSuma(a,b):
    verificado = True
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        verificado = False
    return verificado

def adiMatrix(a,b):
    if verificacionSuma(a,b):
        ans = [[comp.suma(a[i][j],b[i][j]) for j in range (len(a[0])) ]for i in range (len(a))]
    else:
        ans = "Indefinido"
    return ans

def inverMatrix(a):
    escalar = (-1, 0)
    ans = [[comp.producto(escalar,a[i][j]) for j in range (len(a[0])) ]for i in range (len(a))]
    return ans

def escalarMultMatrix(escalar,a):
    return [[comp.producto(escalar,a[i][j]) for j in range (len(a[0])) ]for i in range (len(a))]

def transMatrix(a):
    return [[a[j][i] for j in range (len(a)) ]for i in range (len(a[0]))]

def conjuMatrix(a):
    return [[comp.conjugado(a[i][j]) for j in range (len(a[0])) ]for i in range (len(a))]

def adjMatrix(a):
    return conjuMatrix(transMatrix(a))

def verificacionMult(a,b):
    verificado = True
    if len(a[0]) != len(b):
        verificado = False
    return verificado

def productMatrix(a,b):
    if verificacionMult(a,b):
        ans = [[(0,0) for j in range (len(a[0])) ]for i in range (len(a)) ]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    ans[i][j] = comp.suma(comp.producto(a[i][k],b[k][j]),ans[i][j])
    else:
        ans = "Indefinido"
    return ans

def accionMatrixVector(a,v):
    if verificacionMult(a,v):
        ans, res = [], (0,0)
        for i in range(len(a)):
            for j in range(len(a[0])):
                res = comp.suma(comp.producto(a[i][j], v[j]), res)
            ans = ans + [res]
            res = (0,0)
    else:
        ans = "Indefinido"
    return ans

def prodIntVec(a,b):
    return productMatrix(adjMatrix(a),b)[0][0]

def normaVec(a):
    return (prodIntVec(a,a)[0])**(1/2)

def distVect(a,b):
    ans = [[(adiVect(a,inverVect(b))[i])] for i in range (len(a)) ]
    return normaVec(ans)

def matrixIdentidad(a):
    m = [[(0.0,0.0) for j in range(a)] for i in range(a)]
    for i in range(a):
        m[i][i] = (1.0,0.0)
    return m

def redondearMatriz(a,decimal):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = comp.redondear(a[i][j],decimal)
    return a

def matrixUnitaria(a):
    if redondearMatriz(productMatrix(a,adjMatrix(a)),2) == matrixIdentidad(len(a)):
        ans = True
    else:
        ans = False
    return ans

def matrixHermitiana(a):
    if adjMatrix(a) == a:
        ans = True
    else:
        ans = False
    return ans

def producTensorVector(a,b):
    ans = []
    for i in range (len(a)):
        ans = ans + escalarMultVect(a[i],b)
    return ans

def productTensorMatrix(a,b):
    ans = [[[[]]for j in range(len(a[0])*len(b[0]))]for i in range(len(a)*len(b))]
    for i in range(len(a)*len(b)):
        for j in range(len(a[0])*len(b[0])):
            x, y = i//len(b), j//len(b[0])
            res = escalarMultMatrix(a[x][y],b)
            x1, y1 = i%len(b), j%len(b[0])
            ans[i][j] = res[x1][y1]
    return ans

