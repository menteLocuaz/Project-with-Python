import random
import string
from palabras import palabras
from vidasahorcado import vidasahorcado

def obtenerPalabras(palabras):
    frase= random.choice(palabras)
    while '-' in frase or ' ' in frase:
        frase = random.choice(palabras)
    return frase.upper()
    # print(frase).upper()
def ahorcado():
    print(f"""
    ==================================
           Bienvenido al juego
              de ahorcado
    ==================================""")
    frase=obtenerPalabras(palabras)
    letraporAdivinar=set(frase)
    letrasAdivinar= set()
    # funcion de abecedario
    abecedario=set(string.ascii_uppercase)
    # contador de vida 
    vidas=7
    # elemenot de vidas 
    while len(letraporAdivinar) > 0 and vidas > 0:
        print(f"""\n Te quedas {vidas} vidas y has usado esta letras : \n {" ".join(letrasAdivinar)}
        """)
        # mostra el estado de la palabra
        palabra_lista=[letra if letra in letrasAdivinar
        else '-' for letra in frase]
        # mostra la vida
        # print(vidasahorcado[vidas])
        print(f"""\n ----Tu estdo de vida ----\n
                      {vidasahorcado[vidas]}
        ----------------------------------------""")
        # mostrar la letra separada
        print(f'-->palbras : {" ".join(palabra_lista)} <--')
        letra_usuraio=input('--> Escoje una letra : <--').upper()
        # letras que añade a la adivinanza
        if letra_usuraio in abecedario-letrasAdivinar:
            letrasAdivinar.add(letra_usuraio)
            # si la letra esta en la palabra
            if letra_usuraio in letraporAdivinar:
                letraporAdivinar.remove(letra_usuraio)
                print(' ')
            else:
                vidas=vidas-1
                print(f'\n--> Tu Letra ,{letra_usuraio} no esta en la palabra. <--')
        # si la lera esta escogido  
        elif letra_usuraio in letraporAdivinar:
            print('\n ya escpgites esta letra Elegi otra letra')
        else:
            print('\n esta letra no es valida')
    # se adivina todas la letra
    # cunado se acaba la vida
    if vidas==0:
        print(vidasahorcado[0])
        print(f'¡ Ha Perdido !\n la palabra era {frase}.')
    else :
        print(f'Felicidades Ganaste \n La palabra era {frase}')
        
ahorcado()



    