import random
def adivinaCompu(x):
    #m ostrar el mensaje
    print(f"""
    ============================
      ¡Bienvenido al JUego !
           ++++++++++++++
    Tu objetivo es que la computadora\n
    adivina el numeero entre 
       1 y {x}
    =============================""")
    limiteInferior=1
    limiteSuperior=x
    respuesta=''
    while respuesta !='c':
        if limiteInferior!=limiteSuperior:
         predicicon=random.randint(limiteInferior,limiteSuperior)
        else:
         predicicon==limiteInferior
          # obtener la respuesta
        respuesta=input(f'La predicion es {predicicon} si es muy alta, ingrese (A).\nSi es muy baja ,ingrerse (B).\nsi es correcta ,ingresa (C)->').lower()
        if respuesta=='a':
            limiteSuperior=predicicon-1
        elif respuesta=='b':
            limiteInferior=predicicon+1
    print(f'Ha adivinado el numro {predicicon}')
adivinaCompu(10)