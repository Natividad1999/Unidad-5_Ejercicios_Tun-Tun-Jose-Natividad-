import re

filename = "socket-server.py"
textFile = open(filename, "r")
exp1 = "[a-z]+\d*[-|_]*[a-zA-Z]*\s=\s\d*\w*$"
lista_1 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(exp1, linea)
    if len(x) > 0:
        lista_1.append(x)

filename = "socket-server.py"
textFile = open(filename, "r")
exp2 = "[a-z]+\d*[-|_]*[a-zA-Z]*\s=\s[a-zA-Z|\d|\d.]*\s[+|\-|*|/]\s[a-zA-z|\d|\d.]*$"
lista_2 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(exp2, linea)
    if len(x) > 0:
        lista_2.append(x)

filename = "socket-server.py"
textFile = open(filename, "r")
exp3 = "([A-za-z|\d|\d.]*\s([>=]{2}|[<=]{2}|[!=]{2}|[>]|[<])\s[A-za-z|\d|\d.]*)"
lista_3 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(exp3, linea)
    if len(x) > 0:
        lista_3.append(x)

filename = "socket-server.py"
textFile = open(filename, "r")
exp4 = "[\w]*\s=\s[\w|\d|\d.]*\s[+|\-|*|/]\s[()|\d|\d.|\w]*\s[+|\-|*|]\s[()|\d|\d.|\w]*|[A-Za-z]*\s=\s[()|\d|\d.|\w]*\s[+|\-|*|/]*\s[()|\d|\d.|\w]*\s[+|\-|*|/]*\s[()|\d|\d.|\w]"
lista_4 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(exp4, linea)
    if len(x) > 0:
        lista_4.append(x)

filename = "socket-server.py"
textFile = open(filename, "r")
exp5 = "(if\s[\w]*\s([>=]{2}|[<=]{2}|[!=]{2}|[>]|[<])\s[\w]*:|while\s[\w]*\s([>=]{2}|[<=]{2}|[!=]{2}|[>]|[<])\s[\w]*:|for\s[\w]*\sin\s[\w]*:|for\s[\w]*\sin\s[\w]*[()|\d|,\s]*:)"
lista_5 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(exp5, linea)
    if len(x) > 0:
        lista_5.append(x)

opcion = True
while opcion == True:
    print("\n"+"Analizador de Gramatica")
    print("Archivo analizado: "+str(filename)+"\n")
    print("1.Sentencias de asignación:")
    print(str(lista_1)+"\n")
    print("2.Operaciones aritméticas:")
    print(str(lista_2)+"\n")
    print("3.Expresiones booleanas básicas:")
    print(str(lista_3)+"\n")
    print("4.Formulas complejas del tipo c = a op ( b op d):")
    print(str(lista_4)+"\n")
    print("5.Encabezados de estructuras de control:")
    print(str(lista_5)+"\n")
    
    print("Alumno:Jose Natividad Tun Tun")
    print("Quinto Semestre |A|")
    print("Matricula: 18070059")
    res = input("Ingrese el comando [Salir] para finalizar el programa: ")
    if res == "[Salir]":
        opcion = False
    print("Analisis Finalizado.....")
