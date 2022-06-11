import random
import time
mi_lista=[1,2,3,4,5,6,7,8,9,10,12,11]
def buqueda_inge(lista,objetivo):
    for i in range(len(lista)):
        if lista[i]==objetivo:
            return i
    return -1

def busquea_binaria(lista,objetivo,limiteInferio=None,limiteSuperior=None):
    if limiteInferio is None:
        # inicio de la lista
        limiteInferio=0
    if limiteSuperior is None:
        # Final dela lista
        limiteSuperior=len(lista)-1
    if limiteSuperior<limiteInferio:
        return -1
    punto_medio=(limiteInferio+limiteSuperior)//2

    if lista[punto_medio]==objetivo:
        return punto_medio
    elif objetivo<lista[punto_medio]:
        return busquea_binaria(lista,objetivo,limiteInferio,punto_medio-1)
    else:
        return busquea_binaria(lista,objetivo,punto_medio+1,limiteSuperior)

if __name__=='main':
    print(busquea_binaria(mi_lista,3))
    #crear una lista ordenada
    tamaño=10000
    conjunto_incial=set()

    while len(conjunto_incial)<tamaño:
        conjunto_incial.add(random.randint(-3*tamaño,3*tamaño))

    lista_ordenada=sorted(list(conjunto_incial))
    # medir el tiemo de la busqueinge
    inicio=time.time()
    for objetivo in lista_ordenada:
        buqueda_inge(lista_ordenada,objetivo)
    fin=time.time()
    print(f'Tiempo de busqueda ingenua: {fin-inicio} segundos')
     # medir el tiemo de la busqueda binaria
    inicio=time.time()
    for objetivo in lista_ordenada:
        buqueda_inge(lista_ordenada,objetivo)
    fin=time.time()
    print(f'Tiempo de busqueda binaria : {fin-inicio} segundos')






print(buqueda_inge(mi_lista,3))