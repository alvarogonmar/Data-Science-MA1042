print("***Bienvendo a la calculadora de intereses***")

# asignamos valores a las variables necesarias
tasa_interes = 0.08
interes_acumulado = 0
nombre = input("Ingresa tu nombre: ")
saldo = int(input("Ingresa tu saldo inicial: "))
deposito = int(input("Ingresa la cantidad a depositar en octubre: "))
retiro = int(input("Ingresa la cantidad a retirar en diciembre: "))

# usamos el ciclo for para calcular mes con mes los intereses y el saldo
for mes in range(1, 12 + 1):
 
  #calculamos el interés mensual y lo sumamos a los acumuladores de interés y saldo
  interes_mensual = saldo * tasa_interes / 12
  interes_acumulado = interes_acumulado + interes_mensual
