"""League of Legends Calculator"""""
import tkinter as tk
import re

# Define los colores
DARK_BLUE = '#005A82'
GOLD = '#C89B3C'
GRAY = '#A09B8C'
BLACK = '#010A13'

# Funciones para la calculadora
def mostrar(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def calculate_expression():
    operacion = display.get()
    if son_numeros(operacion):
        try:
            result = eval(operacion)
            clear_display()
            display.insert(0, result)
        except (SyntaxError, NameError):
            clear_display()
            display.insert(0, "Error")
    else:
        clear_display()
        display.insert(0, "No valido")

def son_numeros(expression):
    """verificar que es una operacion matemática"""
    texto = re.compile(r'^[-+*/0-9).(\s]+$')
    return bool(re.fullmatch(texto, expression))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.resizable(width=False, height=False)
root.geometry("400x600")  # Tamaño fijo de ventana

# Creación del display
display = tk.Entry(root, font=('Arial', 24), bg=GRAY, fg=BLACK, borderwidth=2, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Creación del frame para botones
button_frame = tk.Frame(root, bg=DARK_BLUE)
button_frame.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

# Configuración de pesos de filas y columnas
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
button_frame.grid_rowconfigure(0, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Definición de botones
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 2), ('+', 4, 3), ('.', 5, 2),
]

# Función para crear botones
def create_button(text, row, column, colspan=1):
    button = tk.Button(button_frame, text=text, 
                       command=lambda: mostrar(text) if text not in ['C', '='] else None,
                       font=('Arial', 18), bg=GOLD, fg=BLACK)
    button.grid(row=row, column=column, columnspan=colspan, sticky='nsew', padx=5, pady=5)
    if text == 'C':
        button.config(command=clear_display)
    elif text == '=':
        button.config(command=calculate_expression)

# Creación y colocación de botones
for text, row, column in buttons:
    colspan = 2 if text == '0' else 1
    create_button(text, row, column, colspan)

root.mainloop()
