import tkinter as tk
from tkinter import messagebox

# Lista para almacenar los estudiantes
estudiantes = []

def mostrar_menu():
    # Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Crear un Frame para centrar los botones
    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    # Botón para agregar estudiantes
    boton_agregar = tk.Button(frame, text="Agregar Estudiantes", command=muestra_agregar, bg="#7F00B2", fg="white", width=20)
    boton_agregar.pack(pady=10)

    # Botón para mostrar estudiantes
    boton_mostrar = tk.Button(frame, text="Mostrar Estudiantes", command=mostrar_estudiantes, bg="#7F00B2", fg="white", width=20)
    boton_mostrar.pack(pady=10)

def muestra_agregar():
    # Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Campos de entrada para nombre, edad y programa
    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)

    label_edad = tk.Label(ventana, text="Edad:")
    label_edad.pack(pady=5)
    entry_edad = tk.Entry(ventana)
    entry_edad.pack(pady=5)

    label_programa = tk.Label(ventana, text="Programa:")
    label_programa.pack(pady=5)
    entry_programa = tk.Entry(ventana)
    entry_programa.pack(pady=5)

    # Botón para agregar estudiantes
    boton_agregar = tk.Button(ventana, text="Agregar Estudiante", command=lambda: agregar_estudiante(entry_nombre, entry_edad, entry_programa), bg="#7F00B2", fg="white", width=20)
    boton_agregar.pack(pady=10)

    # Botón para volver al menú
    boton_volver = tk.Button(ventana, text="Volver al Menú", command=mostrar_menu, bg="#7F00B2", fg="white", width=20)
    boton_volver.pack(pady=10)

def agregar_estudiante(entry_nombre, entry_edad, entry_programa):
    # Obtener datos de los campos de entrada
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    programa = entry_programa.get()

    # Validar que los campos no estén vacíos
    if not nombre or not edad or not programa:
        messagebox.showerror("Error", "Los campos no pueden enviarse vacíos.")
        return

    # Agregar el estudiante a la lista
    estudiantes.append((nombre, edad, programa))
    
    # Limpiar los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_programa.delete(0, tk.END)
    
    # Mostrar mensaje de confirmación
    messagebox.showinfo("Registro Exitoso", f"El estudiante: {nombre} ha sido correctamente registrado.")

def mostrar_estudiantes():
    # Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Crear un widget Text para mostrar los estudiantes
    resultado = tk.Text(ventana, height=10, width=40)
    resultado.pack(pady=10)

    # Hacer el Text solo lectura
    resultado.config(state=tk.NORMAL)

    # Recorrer la lista e imprimir cada estudiante en el Text
    for nombre, edad, programa in estudiantes:
        resultado.insert(tk.END, f"Nombre: {nombre}, Edad: {edad}, Programa: {programa}\n")

    # Hacer el Text solo lectura nuevamente
    resultado.config(state=tk.DISABLED)

    # Botón para volver al menú
    boton_volver = tk.Button(ventana, text="Volver al Menú", command=mostrar_menu, bg="#7F00B2", fg="white", width=20)
    boton_volver.pack(pady=10)

def cerrar_aplicacion():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Estudiantes")
ventana.geometry("300x300")  # Establecer tamaño de la ventana
ventana.resizable(False, False)  # Deshabilitar maximizar

# Crear un Frame para el botón de cierre
frame_cierre = tk.Frame(ventana)
frame_cierre.place(relx=0.95, rely=0.05, anchor='ne')


# Mostrar el menú inicial
mostrar_menu()

# Ejecutar el bucle principal
ventana.mainloop()
