import unittest
import retos as reto
import complejos as compl

class TestRetos(unittest.TestCase):
    def test_reto1(self):
        vectorKet = [[(-3, -1)], [(0, -2)], [(0, 1)], [(2, 0)]]
        ket1=[[(1,0)],[(0,-1)]]
        ket2 = [[(0, 1)], [(1, 0)]]
        self.assertEqual(reto.probabilidadPosicion(2,vectorKet),0.05263157894736841)
        self.assertEqual(compl.redondear(reto.amplitudTransicionKet(ket1,ket2),2),(0.0, -1.0))
        self.assertEqual(reto.probabilidad(compl.redondear(reto.amplitudTransicionKet(ket1,ket2),2)),1.0)

    def test_reto2(self):
        observable = [[(1,0),(0,-1)],[(0,1),(2,0)]]
        ket = [[((2 ** 0.5) / 2, 0)], [(0, (2 ** 0.5) / 2)]]
        observable2 = [[(0,0),(0,-1)],[(0,1),(0,0)]]
        ket2 = [[(1 / 2 ** 0.5, 0)], [(0, 1 / 2 ** 0.5)]]
        self.assertEqual(reto.valorEsperadoYVarianza(observable,ket),((2.5000000000000004, 0.0), (0.25, 0.0)))
        self.assertEqual(compl.redondear(reto.valorEsperadoYVarianza(observable2,ket2)[0],2),(1.0, 0.0))
        self.assertEqual(compl.redondear(reto.valorEsperadoYVarianza(observable2,ket2)[1],2),(0.0, 0.0))

    def test_reto3(self):
        observable = [[-1,-1j],[1j,1]]
        vectorEstado = [[(1/2,0)],[(1/2,0)]]
        self.assertEqual(reto.valoresPropios(observable),([(-1.414213562373095, 0.0), (1.4142135623730951, 0.0)], [[(0.9238795325112867, 0.0), (0.0, -0.3826834323650897)], [(0.0, -0.3826834323650898), (0.9238795325112867, 0.0)]]))
        self.assertEqual(reto.probabilidadPropios(vectorEstado,reto.valoresPropios(observable)[1]),[(0.25, 0), (0.25, 0)])

    def test_reto4(self):
        Un=[[(0,0),(1/(2**0.5),0),(1/(2**0.5),0),(0,0)],[(0,1/(2**0.5)),(0,0),(0,0),(1/(2**0.5),0)],[(1/(2**0.5),0),(0,0),(0,0),(0,1/(2**0.5))],[(0,0),(1/(2**0.5),0),(-1/(2**0.5),0),(0,0)]]
        estadoInicial = [[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
        self.assertEqual(reto.dinamica(3,Un,estadoInicial),[(-0.49999999999999956, -0.49999999999999956), (0, 0), (0, 0), (0, 0)])

if __name__=='__main__':
    unittest.main()
