print("Manejo de funciones v1")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")


def Mensa(msg):
    print(msg)


def EscribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"Tu nombre completo es: {Nombre} {Apellido}")

def suma2numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} + {n2} es: {s}"

#llamando a la funcion
hola_mundo()
Mensa("hola whatsApp")#llama a mensa como un parametro
Mensa("El profe me sorprendio enviando mensajes")#llama a mensa como un parametro
EscribeNC("Octavio", "Ozaeta")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))