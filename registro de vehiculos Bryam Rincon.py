import tkinter as tk
from tkinter import messagebox

class RegistroVehiculos:
    def __init__(self, Ventana):
        self.Ventana = Ventana
        self.Ventana.title("Registro de Vehículos")
        self.vehiculos_registrados = []
        
        self.placa_label = tk.Label(Ventana, text="Placa:")
        self.placa_label.grid(row=0, column=0)
        self.placa_entry = tk.Entry(Ventana)
        self.placa_entry.grid(row=0, column=1)
        
        self.marca_label = tk.Label(Ventana, text="Marca:")
        self.marca_label.grid(row=1, column=0)
        self.marca_entry = tk.Entry(Ventana)
        self.marca_entry.grid(row=1, column=1)
        
        self.color_label = tk.Label(Ventana, text="Color:")
        self.color_label.grid(row=2, column=0)
        self.color_entry = tk.Entry(Ventana)
        self.color_entry.grid(row=2, column=1)
        
        self.tipo_label = tk.Label(Ventana, text="Tipo:")
        self.tipo_label.grid(row=3, column=0)
        self.tipo_entry = tk.Entry(Ventana)
        self.tipo_entry.grid(row=3, column=1)
        
        self.hora_label = tk.Label(Ventana, text="Hora de Ingreso:")
        self.hora_label.grid(row=4, column=0)
        self.hora_entry = tk.Entry(Ventana)
        self.hora_entry.grid(row=4, column=1)
        
        self.boton_guardar = tk.Button(Ventana, text="Guardar", command=self.guardar_vehiculo)
        self.boton_guardar.grid(row=5, column=0)
        
        self.boton_mostrar = tk.Button(Ventana, text="Mostrar Registros", command=self.mostrar_registros)
        self.boton_mostrar.grid(row=5, column=1)
        
        self.boton_limpiar = tk.Button(Ventana, text="Limpiar", command=self.limpiar_campos)
        self.boton_limpiar.grid(row=5, column=2)
        
        self.resultado_label = tk.Label(Ventana, text="")
        self.resultado_label.grid(row=6, column=0, columnspan=3)
    
    def guardar_vehiculo(self):
        placa = self.placa_entry.get()
        marca = self.marca_entry.get()
        color = self.color_entry.get()
        tipo = self.tipo_entry.get()
        hora = self.hora_entry.get()
        
        if placa == "" or marca == "" or color == "" or tipo == "" or hora == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
        else:
            vehiculo = {"placa": placa, "marca": marca, "color": color, "tipo": tipo, "hora": hora}
            self.vehiculos_registrados.append(vehiculo)
            messagebox.showinfo("Éxito", "Vehículo registrado correctamente")
            self.limpiar_campos()
    
    def mostrar_registros(self):
        if len(self.vehiculos_registrados) == 0:
            self.resultado_label.config(text="No hay registros")
        else:
            texto = ""
            for v in self.vehiculos_registrados:
                texto += f"Placa: {v['placa']}, Marca: {v['marca']}, Color: {v['color']}, Tipo: {v['tipo']}, Hora: {v['hora']}\n"
            self.resultado_label.config(text=texto)
    
    def limpiar_campos(self):
        self.placa_entry.delete(0, tk.END)
        self.marca_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)

Ventana = tk.Tk()
app = RegistroVehiculos(Ventana)
Ventana.mainloop()
