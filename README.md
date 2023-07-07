# proyecto-1-calculadora-IMC

El programa comienza con comentarios de lo que tratara.

La fuente para sacar el IMC fue proporcionada por el ISSSTE, pero también utilice la del IMSS para complementar algunas cosas ya que me pregunte si el IMC de igual manera se aplicaba a las diferentes etapas de un ser humano, el link que me proveyó de esa información es el siguiente
https://www.imss.gob.mx/salud-en-linea/calculaimc

Mandara a pantalla un mensaje de bienvenida, después le pedirá al usuario que ingrese su nombre y apellidos, si el usuario no ingresa nombre o apellidos el programa entrara en bucle hasta que ingrese el dato que se solicito y para verificar que se esta ingresando algo utiliza "len" para comparar que el string de nombre o apellidos no este vacío.

Le pide al usuario que confirme su sexo, posteriormente le asigna un valor booleano a la variable 'gnr'.
Solicita si el IMC será para un recién nacido y si lo es preguntara por los meses que este tiene, si se ingresa algún dato menor a 0 o mayor a 11 entrara un bucle hasta que se cumpla la condición antes mencionada. Si el IMC no es para un recién nacido solicitara la edad, esta no tiene que ser igual o menor a 0 ya que entrar en un bucle hasta que la condición sea cumplida. Dependiendo la elección del usuario asigna un valor BOOLEANO a la variable 'bebe'.

Solicita al usuario que ingrese su altura en metros, si el usuario ingresa valores menores o iguales a 0 y mayores a 2.40 (por poner una altura máxima), se iniciara un ciclo hasta que se cumpla la condición antes mencionada.

Le pregunta al usuario su peso en kilogramos, se iniciara un bucle si se ingreso algún número menor o igual a 0 y saldrá de este hasta que el peso sea mayor a 0.

El programa hace el calculo del IMC sin mostrarlo a pantalla, para tenerlo ya guardado en la variable "imc".

Muestra en pantalla los datos que solicito al usuario y revela los pasos para calcular el IMC de una persona.

El programa corrobora los datos con los if anidados.
Primero verifica el sexo de la persona, después si es un recién nacido, si su edad es de 1 año a 9 años, si su edad es de 10 a 19 años, de 20 a 59 años y si es mayor a 60 años.
En el caso de que sea un recién nacido o que llegue a ser una persona de 1 a 4 años, el peso del sujeto es lo que se toma en cuenta para decir si tiene o no desnutrición, sobrepeso u obesidad.
En el caso de que el sujeto tenga una edad de 5 a 9 años o de 10 a 19 años, si se utilizara el IMC, en estos casos se tiene un resultado diferente del IMC debido a la etapa del sujeto ya que no alcanza aun la adultez.
En el caso de que el sujeto tenga entre 20 a 59 años el calculo del IMC si es el correcto como lo muestra el ISSSTE y el IMSS, mostrara si la persona tiene el peso normal, sobrepeso o algún grado de obesidad.
En el ultimo de los casos es lo mismo que el anterior solo que lo que cambia es la edad, que esta va de 60 años en adelante.

Se utilizo la palabra 'Exit' para que el programa saliera de los if anidados de la categoría "bebe".

Por ultimo muestra un mensaje de despedida a pantalla .

Finaliza el programa.
