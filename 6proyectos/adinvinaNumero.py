import random
def adivinaNumer(x):
    #m mostrar el mensaje
    print("""
    ============================
      ¡Bienvenido al JUego !
           ++++++++++++++
    Tu objetivo es adivinar el 
    numero
    ============================""")
    numeroAleatorio=random.randint(1,x)
    predicion=int(input(f'Dime el numero entre 1-{x}->'))
    while predicion != numeroAleatorio:
        predicion=int(input('Adivina otra ves -> \n'))
        if predicion <= numeroAleatorio:
            print('Intenta un numero mayor!\n')
        elif predicion >= numeroAleatorio:
            print('Intenta un numero menor!\n')
    print(f'Felicidades adivinaste el numero ->{numeroAleatorio}')

adivinaNumer(10)
