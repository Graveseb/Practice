
print('\n\n\n\t\t\tCalculadora de Masa Corporal \n')
print('\nIngrese la cantidad de personas en la calculadora \n\n')

# Pedir al usuario sus datos su información personal
nombre = input("Por favor, ingresa tu nombre: ")
while not nombre.isalpha() or not nombre: 
    nombre = input("El nombre es un campo obligatorio y solo debe contener letras. Por favor, ingresa tu nombre: ")

apellido_paterno = input("Por favor, ingresa tu apellido paterno: ")
while not apellido_paterno.isalpha() or not nombre: 
    apellido_paterno = input("El Apellido Paterno es un campo obligatorio y solo debe contener letras. Por favor, ingresa tu nombre: ")

apellido_materno = input("Por favor, ingresa tu apellido materno: ")
while not apellido_materno.isalpha() or not nombre: 
    apellido_materno = input("El Apellido Materno es un campo obligatorio y solo debe contener letras. Por favor, ingresa tu nombre: ")

edad = input("Por favor, ingresa tu edad: ")
while not edad.isdigit(): 
    edad = input("La edad es un campo obligatorio. Por favor, ingresa tu edad: ")
edad = int(edad)

peso = input("Por favor, ingresa tu peso en kilogramos: ")
while not peso.replace('.', '', 1).isdigit(): 
    peso = input("El peso es un campo obligatorio. Por favor, ingresa tu peso en kilogramos: ")
peso = float(peso)

estatura = input("Por favor, ingresa tu estatura en metros: ")
while not estatura.replace('.', '', 1).isdigit(): 
    estatura = input("La estatura es un campo obligatorio. Por favor, ingresa tu estatura en metros: ")
estatura = float(estatura)

# Calcular el IMC
imc = peso / (estatura ** 2)

print('\n\n')
# Mostrar la información personal y el IMC en pantalla
print("\t\t Resultados en base a la informacion presentado")
print("Nombre completo: " + nombre + " " + apellido_paterno + " " + apellido_materno)
print("Edad: " + str(edad) + " años")
print("Peso: " + str(peso) + " kg")
print("Estatura: " + str(estatura) + " m")
print("Tu índice de masa corporal (IMC) es: " + str(imc))