import re
class mail ():
    __idcuenta =None 
    __dominio=None 
    __tipodedominio=None
    __password=None
    

    def __init__ (self,idcuenta=None,dominio=None, tipodedominio=None, password=None):
        self.__idcuenta=idcuenta#str te convierte todo a cadena y el if te verifica las entradas
        self.__dominio=dominio
        self.__tipodedominio=tipodedominio
        self.__password=password
    def retornaEmail(self):
        return self.__idcuenta + "@" + self.__dominio + "." + self.__tipodedominio
    def getcontra(self):
        return self.__password
        
    def NUEVOc(self,password):
        self.__password=password
    def crearcuenta(self,Correo):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',Correo.lower()):
            print("DATO VALIDO",Correo)
            password=str(input("ingresar password: "))
            separador = Correo.split('@')
            idcuenta = separador[0]
            separador2 = separador[1].split('.')
            dom = separador2[0]
            tipo =separador2[1]
            return mail(idcuenta,dom,tipo,password)
    def testEmail(self):
        prueba1=mail("pedro",234,5,"sesss")
        prueba2=mail(11,"gmail","com",1234321)
        prueba3=mail("pablo","edu","ar","pablo123")
        prueba4=mail()
        print(prueba4.retornamail)
        print("dominio prueba2",prueba2.getdom())
        print("prueba3 password",prueba3.getdom())
    def getdom(self):
        return self.__dominio