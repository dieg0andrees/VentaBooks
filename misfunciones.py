#Funciones de color y titulo
from colorama import Fore, Style
import numpy
import msvcrt
import os
import random

#Funciones de diseño
def printRojo(texto):
    print(F"{Fore.RED}{texto}{Fore.RESET}")

def printERROR(texto):
    print(F"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printVerde(texto):
    print(F"{Fore.GREEN}{texto}{Fore.RESET}")

def printAmarillo(texto):
    print(F"{Fore.YELLOW}{texto}{Fore.RESET}")

def printAzul(texto):
    print(F"{Fore.BLUE}{texto}{Fore.RESET}")

def titulo(texto):
    printRojo("_________________________________")
    printAzul(f"**{texto}")
    printRojo("_________________________________")
    
#Funciones operacionales
libreria = numpy.empty([10,4],object)

def limpiarPantalla():
    printRojo("<<Press any key to continue>>")
    msvcrt.getch()
    os.system("cls")

def validarCodigo(codigo):
    for i in range (10):
        if libreria[i,0] == codigo:
            return i
    return -1

def guardarLibro(codigo,titulo,autor,precio):
    if validarCodigo(codigo) < 0:
        if len(titulo) >= 4:
            if precio >= 0:
                for i in range(10):
                    if libreria[i,0] == None:
                        libreria[i,0] = codigo
                        libreria[i,1] = titulo
                        libreria[i,2] = autor
                        libreria[i,3] = precio
                        printVerde("Libro registrado con exito!")
                        break
            else:
                printERROR("El precio debe ser mayor o igual a 0")
        else:
            printERROR("El titulo debe tener al menos 4 caracteres")
    else:
        printERROR("Codigo ya registrado, Intente con otro")

def listarLibro(codigo):
    posicion = validarCodigo(codigo)
    if validarCodigo(codigo) >= 0:
        printAmarillo(f"Codigo: {libreria[posicion,0]}")
        printAmarillo(f"Titulo: {libreria[posicion,1]}")
        printAmarillo(f"Autor: {libreria[posicion,2]}")
        printAmarillo(f"Precio: {libreria[posicion,3]}")
    else:
        printERROR("Codigo no encontrado")

criticas = []
criticas.append("Muy buen libro")
criticas.append("Pesimo libro")
criticas.append("Buena narrativa")
criticas.append("Es el mejor libro que he leido")
criticas.append("Este libro cambió mi vida")
criticas.append("Nunca volveré a leer este libro")
criticas.append("No lo recomiendo para nada")
criticas.append("Cambió mi perspectiva de la vida")
criticas.append("Lenguaje muy tecnico, indescifrable")
criticas.append("El autor nunca debio haber escrito este libro")
criticas.append("Hare que todos mis amigos lean este libro")
#11 criticas

def criticasLibro(codigo):
    posicion = validarCodigo(codigo)
    if validarCodigo(codigo) >= 0:
        titulo("Criticas de libro")
        printRojo(f"Codigo: {libreria[posicion,0]}")
        printRojo(f"Titulo: {libreria[posicion,1]}")
        printAmarillo(f"1. {criticas[random.randint(0,10)]}")
        printAmarillo(f"2. {criticas[random.randint(0,10)]}")
        printAmarillo(f"3. {criticas[random.randint(0,10)]}")
        printAmarillo(f"4. {criticas[random.randint(0,10)]}")
        printAmarillo(f"5. {criticas[random.randint(0,10)]}")
    else:
        printERROR("Libro no encontrado")

#Datos aleatorios de venta de libro
cant_ventas_libros = random.randint(1,50)
cant_traduc = random.randint(1,15)


def detalleVentas(codigo):
    posicion = validarCodigo(codigo)
    if validarCodigo(codigo) >= 0:
        titulo("Detalle de ventas")
        printRojo(f"Codigo: {libreria[posicion,0]}")
        printRojo(f"Titulo: {libreria[posicion,1]}")
        printAmarillo(f"Cantidad de ventas: {cant_ventas_libros}")
        printAmarillo(f"Total de ventas :${cant_ventas_libros*libreria[posicion,3]}")
        printAmarillo(f"Libro traducido a {cant_traduc} idiomas")
    else:
        printERROR("Libro no encontrado")