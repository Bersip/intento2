import modulos.modulo_intro as intro
import modulos.modulo_reto1 as reto1
import modulos.modulo_reto2 as reto2
import modulos.modulo_reto3 as reto3
import modulos.modulo_conclu as conclu

def ciclo_principal():
    pasalir=False
    pasalir = intro.introduccion()
    if pasalir:
        return 0
    #pasalir = reto1.puerta1()
    if pasalir:
        return 0
    pasalir = reto2.puerta2()
    if pasalir:
        return 0
    #pasalir = reto3.puerta3()
    if pasalir:
         return 0
    #pasalir = conclu.final()
    if pasalir:
         return 0
print("♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥")
print("         Bienvenido Moisés      ")
print("♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥")
   
ciclo_principal()
