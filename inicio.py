# declaramos una variable "name" y gusrdamos lo que el user ingrese
#name = input("ingrese nombre: ").strip().title()

# borramos los espacion en blanco y poner en mayuscula las primeras letras
#name = name.strip().title()

#pone en mayuscula la primer letra
#name = name.capitalize()
#name = name.title()

#imprimimos la variable en pantalla la F es para decirle al programa the {name} es una variable 
#print(f"Hola, {name}")
#print("Hola, "+name)

import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

# Pedir al usuario que ingrese el primer numero
num1 = simpledialog.askinteger(title="Ingresar numero 1", prompt="Por favor ingrese el primer numero:")

# Pedir al usuario que ingrese el segundo numero
num2 = simpledialog.askinteger(title="Ingresar numero 2", prompt="Por favor ingrese el segundo numero:")

"""# Calcular la suma de los dos numeros ingresados
suma = num1 + num2

# Mostrar el resultado de la suma en una ventana emergente
messagebox.showinfo(title="Resultado", message="La suma de los dos numeros es: " + str(suma))
     """

# Verificar si ambos números se han ingresado
if num1 is not None and num2 is not None:
    # Calcular la suma de los dos números ingresados
    suma = num1 + num2

    # Mostrar el resultado de la suma en una ventana emergente
    messagebox.showinfo(title="Resultado", message="La suma de los dos números es: " + str(suma))
else:
    # Si el usuario cancela alguno de los cuadros de diálogo, mostrar un mensaje de advertencia
    messagebox.showwarning(title="Advertencia", message="Se canceló la operación. No se ingresaron ambos números.")