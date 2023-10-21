# crear nuestra funcion
def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
# Crear una lista vacia letras_verificadas para las letras de la palabra luego de ser verificadas
    letras_verificadas = []
# Recorrer la plabra
    for posicion in range(cantidad_de_letras):
        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]

        las_letras_existen = palabra_ingresada[posicion] in palabra_a_encontrar

# si las letras existen en la palabra y sus posiciones coinciden: encerrar entre corchetes [] y agregar a nuestra lista principal
        if las_letras_son_iguales:
            letras_verificadas.append("["+palabra_ingresada[posicion]+"]")
# si las letras existen en la palabra pero sus posiciones no coinciden: encerrar la letra entre parentesis () y agregar a la lista principal
        elif las_letras_existen:
            letras_verificadas.append("("+palabra_ingresada[posicion]+")")
# si las letras no existen: agregar a la lista principal sin modificar 
        else:
            letras_verificadas.append(palabra_ingresada[posicion])
# Retornar el resultado
    return letras_verificadas

def imprimir_grilla(lista):
    cantidad_de_filas = len(lista)

    for fila in range(cantidad_de_filas):
        print(lista[fila])


# Iniciamos el wordle

print("Bienvenido a Wordle!!")

palabra_a_encontrar = "virus"
cantidad_de_letras = 5
intentos = 6 

grilla = []

while intentos > 0:
    print(f"te quedan {intentos} intentos")
    palabra_ingresada = input("Ingrese una palabra: ")
    intentos = intentos - 1 

    if (len(palabra_ingresada) != cantidad_de_letras):
        print("la palabra no tiene la cantidad de letras correctas")
        print(f"ingresa una palabra con {cantidad_de_letras} letras")
        continue 
    else: 
        linea_verificada = obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada)
        grilla.append(linea_verificada)

    imprimir_grilla(grilla)

    if palabra_ingresada == palabra_a_encontrar:
        print("felicidades, ganaste!!")
        break

