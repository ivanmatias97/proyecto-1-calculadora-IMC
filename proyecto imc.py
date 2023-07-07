#Crear un programa que pida al usuario nombre, apellidos, edad, peso y estatura,
#Mandar a pantalla los datos del usuario y su indice de masa corporal (IMC).
#El programa no puede permitir que ningún dato quede vacío, además de asegurarse de que en los campos de edad, peso y estatura 
#el usuario introduzca una cifra. Todo esto antes de proceder con el cálculo del IMC siguiendo la formula:
#Peso / estatura2   -> Peso sobre estatura al cuadrado

print("""
              ¡Hola!
                                                                    
Te mostrare tu indice de masa corporal.
Solo necesito algunos datos tuyos.""")                                              #mensaje de bienvenida

nombre=input('¿Cual es su nombre(s)? ')                                 #pide el nombre(s) y si no se ingreso dato, un ciclo   
if len(nombre) == 0:                                                    #hara que el usuario ingrese el dato que se pide.
    while len(nombre) == 0:
        print('No ingresaste tu nombre(s)\nIngresalo de nuevo')
        nombre=input('¿Cual es su nombre(s)? ')

apat=input('\n¿Cual es su apellido paterno? ')                      #pide el apellido paterno al usuario y si no se ingresa ningun 
if len(apat) == 0:                                                  #dato, un ciclo hara que el usuario ingrese lo que se le pide.
    while len(apat) == 0:
        print('No ingresaste tu apellido paterno\nIngresalo de nuevo')
        apat=input('¿Cual es su apellido paterno? ')

amat=input('\n¿Cual es su apellido materno? ')                      #pide el apellido materno al usuario y si no se ingresa ningun
if len(amat) == 0:                                                  #dato, un ciclo hara que el usuario ingrese lo que se le pide.
    while len(amat) == 0:
        print('No ingresaste el dato que se te pidio\nIngresalo de nuevo')
        amat=input('¿Cual es su apellido materno? ')

gnr=int(input('\n¿Eres Hombre o Mujer? \nPresione \n0 == Hombre\t1 == Mujer\n'))                #pide que se ingrese un numero
if(gnr==0):                                                                                     #y le asigna un valor booleano.
    band=True
elif(gnr==1):
    band=False

bband=int(input('\n¿El IMC es para un recien nacido?\nPresione\n0 == NO \t1 == SI\n'))      #pide que se ingrese un numero, le
if(bband==0):                                                                               #asigna un valor booleano,con un ciclo
    bebe=False                                                                              #verifica que la edad no sea negativa 
    edad=int(input('¿Que edad tiene? '))                                                    #o que el mes sea igual o mayor a 0 y 
    while edad<=0 :                                                                         #que no sea mayor a 11.
        print("Dato Erroneo Ingresalo de Nuevo")
        edad=int(input('¿Que edad tiene? '))
elif(bband==1):
    bebe=True
    edad=0
    mes=int(input("¿Cuantos meses tiene de 0 hasta 11? "))
    while mes<0 and mes>=12:
        print("Dato Erroneo Ingresalo de Nuevo")
        mes=int(input('¿Cuantos meses tiene de 0 hasta 11? '))

altura=float(input('\n¿Que altura tiene en metros? '))                              #pide que se ingrese un numero, con un ciclo
while altura<=0 or altura>2.40:                                                     #hara una comparacion para que la altura no
    print("Dato Erroneo Ingresalo de Nuevo")                                        #sea menor o igual a 0 y que no pase de 2.40.
    altura=float(input('¿Que altura tiene en metros? '))

peso=float(input('\n¿Cuantos kilogramos pesa? '))                                   #pide que se ingrese un dato, con un ciclo
while peso<=0:                                                                      #comparara que el peso no sea igual o menor
    print("Dato Erroneo Ingresalo de Nuevo")                                        #que 0.
    peso=float(input('¿Cuantos kilogramos pesa? '))

imc=peso/altura**2                                                                           #hace el calculo del IMC.

print(f"\nExcelente","gracias por los datos\n\n")                                            #muestra a pantalla los datos que 
print(f'Sujeto :  ' + nombre +' ' + apat +' '+ amat)                                         #se ingresaron y tambien revela
if(band==True):                                                                              #la manera en que se calcula 
    print('Sexo :  Masculino')                                                               #el IMC de una persona.
elif(band==False):
    print("Sexo :  Femenino")
print(f'Altura :  ' + str(altura) + ' mts' )
print(f'Peso :  '+ str(peso) +' kg')
if(bebe==True):
    print(f'Mes(es) de nacido :  ' + mes)
elif(bebe==False):
    print(f'Edad :  ' + str(edad) + ' años')
print(f'Tu indice de masa corporal es: \nIMC = '+ str(peso)+' Kgs / '+ str(altura)+' ^ 2 Mts\nIMC = %0.2f '%(imc))

if(band==True):                          #hombre, verifica si el valor de 'band' sea TRUE y procede con las siguientes condiciones 
    
    if(bebe==True):                      #bebe, verifica si 'bebe' es 'TRUE',compara, el mes y despues el peso para arrojar a pantalla un mensaje
        if(mes==0):
            if(peso<=2.8):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=2.9 and peso<=3.8):
               print("Tu peso es NORMAL")
            elif(peso>=3.9 and peso<=4.3):
                print("Tienes SOBREPESO")
            elif(peso>=4.4):
                print("Tienes OBESIDAD")
        if(mes==1):
            if(peso<=3.9):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=4.0 and peso<=5.0):
                print("Tu peso es NORMAL")
            elif(peso>=5.1 and peso<=5.7):
                print("Tienes SOBREPESO")
            elif(peso>=5.8):
                print("Tienes OBESIDAD")
        if(mes==2):
            if(peso<=4.9):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=5.0 and peso<=6.2):
                print("Tu peso es NORMAL")
            elif(peso>=6.3 and peso<=7.0):
                print("Tienes SOBREPESO")
            elif(peso>=7.1):
                print("Tienes OBESIDAD")
        if(mes==3):
            if(peso<=5.7):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=5.8 and peso<=7.1):
                print("Tu peso es NORMAL")
            elif(peso>=7.2 and peso<=7.9):
                print("Tienes SOBREPESO")
            elif(peso>=8.0):
                print("Tienes OBESIDAD")
        if(mes==4):
            if(peso<=6.2):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=6.3 and peso<=7.7):
                print("Tu peso es NORMAL")
            elif(peso>=7.8 and peso<=8.6):
                print("Tienes SOBREPESO")
            elif(peso>=8.7):
                print("Tienes OBESIDAD")
        if(mes==5):
            if(peso<=6.7):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=6.8 and peso<=8.3):
                print("Tu peso es NORMAL")
            elif(peso>=8.4 and peso<=9.2):
                print("Tienes SOBREPESO")
            elif(peso>=9.3):
                print("Tienes OBESIDAD")
        if(mes==6):
            if(peso<=7.1):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=7.2 and peso<=8.7):
                print("Tu peso es NORMAL")
            elif(peso>=8.8 and peso<=9.7):
                print("Tienes SOBREPESO")
            elif(peso>=9.7):
                print("Tienes OBESIDAD")
        if(mes==7):
            if(peso<=7.4):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=7.5 and peso<=9.1):
                print("Tu peso es NORMAL")
            elif(peso>=9.2 and peso<=10.2):
                print("Tienes SOBREPESO")
            elif(peso>=10.3):
                print("Tienes OBESIDAD")
        if(mes==8):
            if(peso<=7.7):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=7.8 and peso<=9.5):
                print("Tu peso es NORMAL")
            elif(peso>=9.6 and peso<=10.6):
                print("Tienes SOBREPESO")
            elif(peso>=10.7):
                print("Tienes OBESIDAD")
        if(mes==9):
            if(peso<=8.0):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=8.1 and peso<=9.8):
                print("Tu peso es NORMAL")
            elif(peso>=9.9 and peso<=10.9):
                print("Tienes SOBREPESO")
            elif(peso>=11.0):
                print("Tienes OBESIDAD")
        if(mes==10):
            if(peso<=8.2):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=8.3 and peso<=10.1):
                print("Tu peso es NORMAL")
            elif(peso>=10.2 and peso<=11.6):
                print("Tienes SOBREPESO")
            elif(peso>=11.7):
                print("Tienes OBESIDAD")
        if(mes==11):
            if(peso<=8.4):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=8.5 and peso<=10.4):
                print("Tu peso es NORMAL")
            elif(peso>=10.5 and peso<=11.6):
                print("Tienes SOBREPESO")
            elif(peso>=11.7):
                print("Tienes OBESIDAD")
        exit                                    #se escribio 'exit' para que el programa salga de los if anidados
    
    if(edad>=1 and edad<=9):             #niño, compara, la edad, el imc o el peso 'solo si la edad es de 1 a 4 años' y arroja mensaje a pantalla
        if(edad==1):
            if(peso<=8.6):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=8.7 and peso<=10.7):
                print("Tu peso es NORMAL")
            elif(peso>=10.8 and peso<=11.9):
                print("Tienes SOBREPESO")
            elif(peso>=12.0):
                print("Tienes OBESIDAD")       
        if(edad==2):
            if(peso<=10.8):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=10.9 and peso<=13.5):
                print("Tu peso es NORMAL")
            elif(peso>=13.6 and peso<=15.2):
                print("Tienes SOBREPESO")
            elif(peso>=15.3):
                print("Tienes OBESIDAD")
        if(edad==3):
            if(peso<=12.7):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=12.8 and peso<=16.1):
                print("Tu peso es NORMAL")
            elif(peso>=16.2 and peso<=18.2):
                print("Tienes SOBREPESO")
            elif(peso>=18.3):
                print("Tienes OBESIDAD")
        if(edad==4):
            if(peso<=14.4):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=14.5 and peso<=18.5):
                print("Tu peso es NORMAL")
            elif(peso>=18.6 and peso<=21.1):
                print("Tienes SOBREPESO")
            elif(peso>=21.2):
                print("Tienes OBESIDAD")
        if(edad==5):
            if(imc<=16.0):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=16.1 and imc<=20.9):
                print("Tu peso es NORMAL")
            elif(imc>=21.0 and imc<=24.1):
                print("Tienes SOBREPESO")
            elif(imc>=24.2):
                print("Tienes OBESIDAD")
        if(edad==6):
            if(imc<=13.0):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=13.1 and imc<=16.7):
                print("Tu peso es NORMAL")
            elif(imc>=16.8 and imc<=18.4):
                print("Tienes SOBREPESO")
            elif(imc>=18.5):
                print("Tienes OBESIDAD") 
        if(edad==7):
            if(imc<=13.1):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=13.2 and imc<=16.9):
                print("Tu peso es NORMAL")
            elif(imc>=17.0 and imc<=18.9):
                print("Tienes SOBREPESO")
            elif(imc>=19.0):
                print("Tienes OBESIDAD")
        if(edad==8):
            if(imc<=13.3):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=13.4 and imc<=17.3):
                print("Tu peso es NORMAL")
            elif(imc>=17.4 and imc<=19.6):
                print("Tienes SOBREPESO")
            elif(imc>=19.7):
                print("Tienes OBESIDAD")
        if(edad==9):
            if(imc<=13.5):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=13.6 and imc<=17.8):
                print("Tu peso es NORMAL")
            elif(imc>=17.9 and imc<=20.4):
                print("Tienes SOBREPESO")
            elif(imc>=20.5):
                print("Tienes OBESIDAD")
    
    if(edad>=10 and edad<=19):           #adolescente, compara, la edad, el imc y arroja mensaje a pantalla
        if(edad==10):
            if(imc<=13.7):
                print("Tienes BAJO PESO")
            elif(imc>=13.8 and imc<=18.4):
                print("Tu peso es NORMAL")
            elif(imc>=18.5 and imc<=21.3):
                print("Tienes SOBREPESO")
            elif(imc>=21.4):
                print("Tienes OBESIDAD")
        elif(edad==11):
            if(imc<=14.1):
                print("Tienes BAJO PESO")
            elif(imc>=14.2 and imc<=19.1):
                print("Tu peso es NORMAL")
            elif(imc>=19.2 and imc<=22.4):
                print("Tienes SOBREPESO")
            elif(imc>=22.5):
                print("Tienes OBESIDAD")
        elif(edad==12):
            if(imc<=14.5):
                print("Tienes BAJO PESO")
            elif(imc>=14.6 and imc<=19.8):
                print("Tu peso es NORMAL")
            elif(imc>=19.9 and imc<=23.5):
                print("Tienes SOBREPESO")
            elif(imc>=23.6):
                print("Tienes OBESIDAD")
        elif(edad==13):
            if(imc<=14.9):
                print("Tienes BAJO PESO")
            elif(imc>=15.0 and imc<=20.7):
                print("Tu peso es NORMAL")
            elif(imc>=20.8 and imc<=24.7):
                print("Tienes SOBREPESO")
            elif(imc>=24.8):
                print("Tienes OBESIDAD")
        elif(edad==14):
            if(imc<=15.5):
                print("Tienes BAJO PESO")
            elif(imc>=15.6 and imc<=21.7):
                print("Tu peso es NORMAL")
            elif(imc>=21.8 and imc<=25.8):
                print("Tienes SOBREPESO")
            elif(imc>=25.9):
                print("Tienes OBESIDAD")
        elif(edad==15):
            if(imc<=16.0):
                print("Tienes BAJO PESO")
            elif(imc>=16.1 and imc<=22.6):
                print("Tu peso es NORMAL")
            elif(imc>=22.7 and imc<=26.9):
                print("Tienes SOBREPESO")
            elif(imc>=27.0):
                print("Tienes OBESIDAD")
        elif(edad==16):
            if(imc<=16.5):
                print("Tienes BAJO PESO")
            elif(imc>=16.6 and imc<=23.4):
                print("Tu peso es NORMAL")
            elif(imc>=23.5 and imc<=27.8):
                print("Tienes SOBREPESO")
            elif(imc>=27.9):
                print("Tienes OBESIDAD")
        elif(edad==17):
            if(imc<=16.9):
                print("Tienes BAJO PESO")
            elif(imc>=17.0 and imc<=24.2):
                print("Tu peso es NORMAL")
            elif(imc>=24.3 and imc<=28.5):
                print("Tienes SOBREPESO")
            elif(imc>=28.6):
                print("Tienes OBESIDAD")
        elif(edad==18):
            if(imc<=17.3):
                print("Tienes BAJO PESO")
            elif(imc>=17.4 and imc<=24.8):
                print("Tu peso es NORMAL")
            elif(imc>=24.9 and imc<=29.1):
                print("Tienes SOBREPESO")
            elif(imc>=29.2):
                print("Tienes OBESIDAD")
        elif(edad==19):
            if(imc<=17.6):
                print("Tienes BAJO PESO")
            elif(imc>=17.7 and imc<=25.3):
                print("Tu peso es NORMAL")
            elif(imc>=25.4 and imc<=29.6):
                print("Tienes SOBREPESO")
            elif(imc>=29.7):
                print("Tienes OBESIDAD")
    
    if(edad>=20 and edad<=59):           #adulto, compara, la edad, el imc y arroja mensaje a pantalla
        if(imc>=18.5 and imc<=24.9):
            print("Tu IMC es NORMAL")
        elif(imc>=25 and imc<=29.9):
            print("Tu IMC indica que tienes SOBREPESO")
        elif(imc>=30 and imc<=34.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 1")
        elif(imc>=35 and imc<=39.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 2")
        elif(imc>=40):
            print("Tu IMC indica que tienes OBESIDAD GRADO 3")
    
    if(edad>=60):                        #adulto mayor, compara, la edad, el imc y arroja mensaje a pantalla
        if(imc>=18.5 and imc<=24.9):
            print("Tu IMC es NORMAL")
        elif(imc>=25 and imc<=29.9):
            print("Tu IMC indica que tienes SOBREPESO")
        elif(imc>=30 and imc<=34.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 1")
        elif(imc>=35 and imc<=39.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 2")
        elif(imc>=40):
            print("Tu IMC indica que tienes OBESIDAD GRADO 3")

elif(band==False):                       #mujer, verifica si el valor de 'band' sea FALSE y procede con las siguientes condiciones
   
    if(bebe==True):                      #bebe, verifica si 'bebe' es 'TRUE',compara, el mes y despues el peso para arrojar a pantalla un mensaje
        if(mes==0):
            if(peso<=2.8):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=2.9 and peso<=3.6):
                print("Tu peso es NORMAL")
            elif(peso>=3.7 and peso<=4.1):
                print("Tienes SOBREPESO")
            elif(peso>=4.2):
                print("Tienes OBESIDAD")
        if(mes==1):
            if(peso<=3.6):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=3.7 and peso<=4.7):
                print("Tu peso es NORMAL")
            elif(peso>=4.8 and peso<=5.4):
                print("Tienes SOBREPESO")
            elif(peso>=5.5):
                print("Tienes OBESIDAD")
        if(mes==2):
            if(peso<=4.5):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=4.6 and peso<=5.7):
                print("Tu peso es NORMAL")
            elif(peso>=5.8 and peso<=6.5):
                print("Tienes SOBREPESO")
            elif(peso>=6.6):
                print("Tienes OBESIDAD")
        if(mes==3):
            if(peso<=5.2):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=5.3 and peso<=6.5):
                print("Tu peso es NORMAL")
            elif(peso>=6.6 and peso<=7.4):
                print("Tienes SOBREPESO")
            elif(peso>=7.5):
                print("Tienes OBESIDAD")
        if(mes==4):
            if(peso<=6.1):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=6.2 and peso<=7.2):
                print("Tu peso es NORMAL")
            elif(peso>=7.3 and peso<=8.1):
                print("Tienes SOBREPESO")
            elif(peso>=8.2):
                print("Tienes OBESIDAD")
        if(mes==5):
            if(peso<=6.1):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=6.2 and peso<=7.7):
                print("Tu peso es NORMAL")
            elif(peso>=7.8 and peso<=8.7):
                print("Tienes SOBREPESO")
            elif(peso>=8.8):
                print("Tienes OBESIDAD")
        if(mes==6):
            if(peso<=6.5):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=6.6 and peso<=8.1):
                print("Tu peso es NORMAL")
            elif(peso>=8.2 and peso<=9.2):
                print("Tienes SOBREPESO")
            elif(peso>=9.3):
                print("Tienes OBESIDAD")
        if(mes==7):
            if(peso<=6.8):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=6.9 and peso<=8.5):
                print("Tu peso es NORMAL")
            elif(peso>=8.6 and peso<=9.7):
                print("Tienes SOBREPESO")
            elif(peso>=9.8):
                print("Tienes OBESIDAD")
        if(mes==8):
            if(peso<=7.0):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=7.1 and peso<=8.9):
                print("Tu peso es NORMAL")
            elif(peso>=9.0 and peso<=10.1):
                print("Tienes SOBREPESO")
            elif(peso>=10.2):
                print("Tienes OBESIDAD")
        if(mes==9):
            if(peso<=7.3):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=7.4 and peso<=9.2):
                print("Tu peso es NORMAL")
            elif(peso>=9.3 and peso<=10.4):
                print("Tienes SOBREPESO")
            elif(peso>=10.5):
                print("Tienes OBESIDAD")
        if(mes==10):
            if(peso<=7.5):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=7.6 and peso<=9.5):
                print("Tu peso es NORMAL")
            elif(peso>=9.6 and peso<=10.8):
                print("Tienes SOBREPESO")
            elif(peso>=10.9):
                print("Tienes OBESIDAD")
        if(mes==11):
            if(peso<=7.7):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=7.8 and peso<=9.8):
                print("Tu peso es NORMAL")
            elif(peso>=9.9 and peso<=11.1):
                print("Tienes SOBREPESO")
            elif(peso>=11.2):
                print("Tienes OBESIDAD")
        exit                                    #se escribio 'exit' para que el programa salga de los if anidados.
   
    if(edad>=1 and edad<=9):             #niña, compara, la edad, el imc o el peso 'solo si la edad es de 1 a 4 años' y arroja mensaje a pantalla 
        if(edad==1):
            if(peso<=7.9):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=8.0 and peso<=10.0):
                print("Tu peso es NORMAL")
            elif(peso>=10.1 and peso<=11.4):
                print("Tienes SOBREPESO")
            elif(peso>=11.5):
                print("Tienes OBESIDAD")
        if(edad==2):
            if(peso<=10.2):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=10.3 and peso<=12.9):
                print("Tu peso es NORMAL")
            elif(peso>=13.0 and peso<=14.7):
                print("Tienes SOBREPESO")
            elif(peso>=14.8):
                print("Tienes OBESIDAD")
        if(edad==3):
            if(peso<=12.1):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=12.2 and peso<=15.7):
                print("Tu peso es NORMAL")
            elif(peso>=15.8 and peso<=18.0):
                print("Tienes SOBREPESO")
            elif(peso>=18.1):
                print("Tienes OBESIDAD")
        if(edad==4):
            if(peso<=14.0):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(peso>=14.1 and peso<=18.4):
                print("Tu peso es NORMAL")
            elif(peso>=18.5 and peso<=21.4):
                print("Tienes SOBREPESO")
            elif(peso>=21.5):
                print("Tienes OBESIDAD")
        if(edad==5):
            if(imc<=15.8):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=15.9 and imc<=21.1):
                print("Tu peso es NORMAL")
            elif(imc>=21.2 and imc<=24.8):
                print("Tienes SOBREPESO")
            elif(imc>=24.9):
                print("Tienes OBESIDAD")
        if(edad==6):
            if(imc<=12.7):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=12.8 and imc<=16.9):
                print("Tu peso es NORMAL")
            elif(imc>=17.0 and imc<=19.1):
                print("Tienes SOBREPESO")
            elif(imc>=19.2):
                print("Tienes OBESIDAD")
        if(edad==7):
            if(imc<=12.7):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=12.8 and imc<=17.2):
                print("Tu peso es NORMAL")
            elif(imc>=17.3 and imc<=19.7):
                print("Tienes SOBREPESO")
            elif(imc>=19.8):
                print("Tienes OBESIDAD")
        if(edad==8):
            if(imc<=12.9):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=13.0 and imc<=17.6):
                print("Tu peso es NORMAL")
            elif(imc>=17.7 and imc<=20.5):
                print("Tienes SOBREPESO")
            elif(imc>=20.6):
                print("Tienes OBESIDAD")      
        if(edad==9):
            if(imc<=13.1):
                print("Estas en RIESGO DE DESNUTRICION")
            elif(imc>=13.2 and imc<=18.2):
                print("Tu peso es NORMAL")
            elif(imc>=18.3 and imc<=21.4):
                print("Tienes SOBREPESO")
            elif(imc>=21.5):
                print("Tienes OBESIDAD")
   
    if(edad>=10 and edad<=19):           #adolescente, compara, la edad, el imc y arroja mensaje a pantalla
        if(edad==10):
            if(imc<=13.5):
                print("Tienes BAJO PESO")
            elif(imc>=13.6 and imc<=18.9):
                print("Tu peso es NORMAL")
            elif(imc>=19.0 and imc<=22.5):
                print("Tienes SOBREPESO")
            elif(imc>=22.6):
                print("Tienes OBESIDAD")
        elif(edad==11):
            if(imc<=13.9):
                print("Tienes BAJO PESO")
            elif(imc>=14.0 and imc<=19.8):
                print("Tu peso es NORMAL")
            elif(imc>=19.9 and imc<=23.6):
                print("Tienes SOBREPESO")
            elif(imc>=23.7):
                print("Tienes OBESIDAD")
        elif(edad==12):
            if(imc<=14.4):
                print("Tienes BAJO PESO")
            elif(imc>=14.5 and imc<=20.7):
                print("Tu peso es NORMAL")
            elif(imc>=20.8 and imc<=24.9):
                print("Tienes SOBREPESO")
            elif(imc>=25.0):
                print("Tienes OBESIDAD")
        elif(edad==13):
            if(imc<=14.9):
                print("Tienes BAJO PESO")
            elif(imc>=15.0 and imc<=21.7):
                print("Tu peso es NORMAL")
            elif(imc>=21.8 and imc<=26.1):
                print("Tienes SOBREPESO")
            elif(imc>=26.2):
                print("Tienes OBESIDAD")
        elif(edad==14):
            if(imc<=15.4):
                print("Tienes BAJO PESO")
            elif(imc>=15.5 and imc<=22.6):
                print("Tu peso es NORMAL")
            elif(imc>=22.7 and imc<=27.2):
                print("Tienes SOBREPESO")
            elif(imc>=27.3):
                print("Tienes OBESIDAD")
        elif(edad==15):
            if(imc<=15.9):
                print("Tienes BAJO PESO")
            elif(imc>=16.0 and imc<=23.4):
                print("Tu peso es NORMAL")
            elif(imc>=23.5 and imc<=28.1):
                print("Tienes SOBREPESO")
            elif(imc>=28.2):
                print("Tienes OBESIDAD")
        elif(edad==16):
            if(imc<=16.2):
                print("Tienes BAJO PESO")
            elif(imc>=16.3 and imc<=24.0):
                print("Tu peso es NORMAL")
            elif(imc>=24.1 and imc<=28.8):
                print("Tienes SOBREPESO")
            elif(imc>=28.9):
                print("Tienes OBESIDAD")
        elif(edad==17):
            if(imc<=16.4):
                print("Tienes BAJO PESO")
            elif(imc>=16.5 and imc<=24.4):
                print("Tu peso es NORMAL")
            elif(imc>=24.5 and imc<=29.2):
                print("Tienes SOBREPESO")
            elif(imc>=29.3):
                print("Tienes OBESIDAD")
        elif(edad==18):
            if(imc<=16.4):
                print("Tienes BAJO PESO")
            elif(imc>=16.5 and imc<=24.7):
                print("Tu peso es NORMAL")
            elif(imc>=24.8 and imc<=29.4):
                print("Tienes SOBREPESO")
            elif(imc>=29.5):
                print("Tienes OBESIDAD")
        elif(edad==19):
            if(imc<=16.5):
                print("Tienes BAJO PESO")
            elif(imc>=16.6 and imc<=24.9):
                print("Tu peso es NORMAL")
            elif(imc>=25.0 and imc<=29.6):
                print("Tienes SOBREPESO")
            elif(imc>=29.7):
                print("Tienes OBESIDAD")
   
    if(edad>=20 and edad<=59):           #adulto, compara, la edad, el imc y arroja mensaje a pantalla
        if(imc>=18.5 and imc<=24.9):
            print("Tu IMC es NORMAL")
        elif(imc>=25 and imc<=29.9):
            print("Tu IMC indica que tienes SOBREPESO")
        elif(imc>=30 and imc<=34.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 1")
        elif(imc>=35 and imc<=39.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 2")
        elif(imc>=40):
            print("Tu IMC indica que tienes OBESIDAD GRADO 3")
   
    if(edad>=60):                        #adulto mayor, compara, la edad, el imc y arroja mensaje a pantalla
        if(imc>=18.5 and imc<=24.9):
            print("Tu IMC es NORMAL")
        elif(imc>=25 and imc<=29.9):
            print("Tu IMC indica que tienes SOBREPESO")
        elif(imc>=30 and imc<=34.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 1")
        elif(imc>=35 and imc<=39.9):
            print("Tu IMC indica que tienes OBESIDAD GRADO 2")
        elif(imc>=40):
            print("Tu IMC indica que tienes OBESIDAD GRADO 3")

print("\n !!HASTA LUEGO¡¡ ")             #mensaje de desedida