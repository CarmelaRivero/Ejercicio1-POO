from mail import mail
import re
import csv
# -- coding: utf-8 --
if __name__ == "__main__":
    """email = Email("AlanPerez","hotmail","com","123")
    email2 = Email()
    print(email.retornaEmail())"""
    nombre=str(input("ingresar su nombre: "))
    correo=str(input("ingesar correo: "))
    
    while((correo.count("@")!=1) or (correo.count(".")==0)):
       print("Correo Mal Ingresado: ")
       correo=str(input("ingesar correo nuevamente: "))
    password=str(input("ingresar password: "))
    separador = correo.split('@')
    idcuenta = separador[0]
    separador2 = separador[1].split('.')
    dom = separador2[0]
    tipo =separador2[1]
    
    Mail = mail(idcuenta,dom,tipo,password)
    print("Estimado {} te enviaremos tus mensajes a la dirección {}".format(nombre,Mail.retornaEmail()))
    #else:
    password2=str(input("ingresar password actual: "))
    while (str(password2)!=str(Mail.getcontra())):
        password2=str(input("ingresar password nuevamete por que ha fallado : "))
    print("contraseña valida: ")
    nueva=str(input("ingresar nueva contraseña: "))
    Mail.NUEVOc(nueva)
    print("contrseña actualizda",Mail.getcontra())
    parabuscar=input("ingresar dominio para realizar  una buaqueda: ")
    archivo=open("archivo.csv")
    reader=csv.reader(archivo,delimiter=";")
    cont=0
    for i in reader:
        if (i[1] == parabuscar):
            cont += 1
    print("cantidad de correos para el domineo ",parabuscar,"es de",cont)        
    print(">>>crear objetos de correos<<<")
    Mail = mail(idcuenta,dom,tipo,password)
    n=str(input("ingresar correo para crear objeto: "))
      

    while(n != 'fin'):
        m1=Mail.crearcuenta(n)
        print(m1)
        n=str(input("ingresar correo para crear objeto , finalizar con fin: "))
    print("FIN")
    print("funcion de test: ")
    Mail = mail(idcuenta,dom,tipo,password)
    Mail.testEmail()