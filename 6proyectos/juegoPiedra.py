import random
def jugarPiedra():
    usuario=input('Escoje una opcion piedra(Pi) o papel(Pa) o tigeras(Ti)\n').upper()
    computador=random.choice(['PI','PA','TI'])
    if usuario==computador:
        return'-----¡ EMPATE !----------'

    if ganoUsuario(usuario,computador):
        return'--------Ganaste----------'

    return '¡----------Perdiste!-----------'

def ganoUsuario(usuario,computador):
    # poner la logica del ganador
    if((usuario=='PI' and computador=='TI')
    or (usuario=='TI'and computador=='PA')
    or (usuario=='PA'and computador=='PI')   
    ):
     print(f'ganaste | el opnete eligio {computador}')
    else:
     print(f'perdiste | el opnete eligio {computador}')



print(jugarPiedra())