import socket
import re
#AF_INET se refiere a una familia IP
#SOCK_STREAM indica que es una conexión TCP
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Especificamos la dirección ip y el puerto en el cual
#escuchará nuestro servidor
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(5) #Máximo de conexiones

print(f"\n\nServer Listening on {ip}:{port}")

salir = False
while salir == False:
    conexion, address = socket_server.accept()
    print ("La conexión  ha sido establecida")


    while True:
        message = conexion.recv(1024)
        message = message.decode()
        print(message)
         
        #Expresiones Regulares
        #Cantidad de vocales recibidas
        regex1 = "[AEIOUaeiou]"              
        resultado1 = (len(re.findall(regex1, message)))

        #Cantidad de palabras recibidas 
        regex2 = "[A-Za-z\d]+"
        resultado2 = (len(re.findall(regex2, message)))

        #Cantidad de números contenidos en el mensaje enviado
        regex3 = "[\d]"
        resultado3 =(len(re.findall(regex3, message)))

        #Cantidad de palabras que inician con mayúscula
        regex4 = "[A-Z][a-z|A-Z]"
        resultado4 = (len(re.findall(regex4, message)))

        #Palabras que finalizan con letras que no son vocal
        regex5 = "[A-Za-z]+"
        regex6 = "[A-Za-z]+[^aeiou]$"
        lista_temp = []
        lista = re.findall(regex5, message)
        for elemento in lista:
            if re.findall(regex6, elemento):
                lista_temp.append(elemento)

        if message == '[Salir]':
            message = 'Hasta luego...'
            conexion.send(message.encode())
            print("\n")
            salir = True
            break
        
        else:
             message = "\n1.Cantidad de vocales recibidas:" +str(resultado1) + "\n"\
                       "2.Cantidad de palabra recibidas:" +str(resultado2) + "\n"\
                       "3.Cantidad de números contenidos en el mensaje enviado:" +str(resultado3) + "\n"\
                       "4.Cantidad de palabras que inician con mayúscula:" +str(resultado4) + "\n"\
                       "5.Palabras que finalizan con letras que no son vocal:" +str(lista_temp) + "\n"\
                       "\nIngrese la cadena a anlizar\n"
        
             conexion.send(message.encode())
 
print("Servidor Finalizado")
conexion.close()
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

print(sumalista([1,3,5,7,9]))

contador == suma 
contador != factorial
resta <= multiplicacion
suma > resta 
multiplicacion >= division

factorial = 100 * (5 + suma)
resultado = (multiplicacion - 10) / 5
