import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# Clase abstracta que define los metodos basicos
class Usuario(ABC):
    def __init__(self, cedula, edad):
        self._cedula = cedula  # Variable encapsulada
        self._edad = edad

    @abstractmethod
    def obtener_turno(self):
        pass

# Subclase para usuarios de la tercera edad
class UsuarioTerceraEdad(Usuario):
    def obtener_turno(self):
        return f"X{TurnoManager.siguiente_turno()}"

# Subclase para usuarios generales
class UsuarioGeneral(Usuario):
    def obtener_turno(self, tipo_servicio):
        return f"{tipo_servicio}{TurnoManager.siguiente_turno()}"

# Clase gestora de turnos
class TurnoManager:
    _contador_turnos = 0  # Variable encapsulada

    @classmethod
    def siguiente_turno(cls):
        cls._contador_turnos += 1
        return cls._contador_turnos

# Clase principal de la aplicacion
class DigiturnoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digiturno NuevaEPS")
        self.root.geometry("500x400")
        self.root.configure(bg="white")
        self._crear_interfaz_principal()

    def _crear_interfaz_principal(self):
        tk.Label(
            self.root,
            text="Bienvenido a NuevaEPS",
            font=("Arial", 16),
            pady=20,
            bg="white",
            fg="blue"
        ).pack()

        tk.Button(
            self.root,
            text="Obtener Turno",
            font=("Arial", 12),
            bg="blue",
            fg="white",
            command=self._mostrar_ventana_datos
        ).pack(pady=20)

    def _mostrar_ventana_datos(self):
        self.root.withdraw()  # Ocultar ventana principal

        self.ventana_datos = tk.Toplevel()
        self.ventana_datos.title("Digiturno NuevaEPS - Datos")
        self.ventana_datos.geometry("500x400")
        self.ventana_datos.configure(bg="white")

        tk.Label(
            self.ventana_datos,
            text="Por favor ingrese su numero de cedula y su edad",
            font=("Arial", 14),
            bg="white",
            fg="blue"
        ).pack(pady=10)

        self.entrada_cedula = tk.Entry(self.ventana_datos, font=("Arial", 12), justify="center")
        self.entrada_cedula.pack(pady=5)
        self.entrada_cedula.focus_set()

        self.entrada_edad = tk.Entry(self.ventana_datos, font=("Arial", 12), justify="center")
        self.entrada_edad.pack(pady=5)

        tk.Button(
            self.ventana_datos,
            text="Continuar",
            font=("Arial", 12),
            bg="blue",
            fg="white",
            command=self._capturar_datos
        ).pack(pady=10)

        tk.Button(
            self.ventana_datos,
            text="Volver al Inicio",
            font=("Arial", 12),
            bg="gray",
            fg="white",
            command=self._volver_a_inicio_desde_datos
        ).pack(pady=10)

    def _capturar_datos(self):
        cedula = self.entrada_cedula.get()
        edad = self.entrada_edad.get()

        if not cedula.isdigit() or len(cedula) != 10:
            messagebox.showerror("Error", "Por favor ingrese una cedula valida de 10 numeros")
        elif not edad.isdigit():
            messagebox.showerror("Error", "Por favor ingrese solo numeros en la edad")
        else:
            edad = int(edad)
            if edad < 0 or edad > 100:
                messagebox.showerror("Error", "Por favor ingrese una edad valida entre 0 y 100 años")
            else:
                usuario = UsuarioTerceraEdad(cedula, edad) if edad >= 65 else UsuarioGeneral(cedula, edad)
                self._mostrar_menu_o_turno(usuario)

    def _mostrar_menu_o_turno(self, usuario):
        if isinstance(usuario, UsuarioTerceraEdad):
            turno = usuario.obtener_turno()
            messagebox.showinfo("Turno Directo", f"Usted sera atendido inmediatamente.\nSu numero de turno es: {turno}")
            self._volver_a_inicio_desde_datos()
        else:
            self.ventana_datos.destroy()
            self._mostrar_ventana_menu(usuario)

    def _mostrar_ventana_menu(self, usuario):
        self.ventana_menu = tk.Toplevel()
        self.ventana_menu.title("Digiturno NuevaEPS - Menu")
        self.ventana_menu.geometry("500x400")
        self.ventana_menu.configure(bg="white")

        tk.Label(
            self.ventana_menu,
            text="Seleccione una opcion:",
            font=("Arial", 14),
            bg="white",
            fg="blue"
        ).pack(pady=20)

        opciones = {
            "Autorizaciones": "A",
            "Certificados": "C",
            "Portabilidad": "P"
        }

        for opcion, prefix in opciones.items():
            tk.Button(
                self.ventana_menu,
                text=opcion,
                font=("Arial", 12),
                bg="blue",
                fg="white",
                command=lambda opt_name=opcion, pref=prefix: self._mostrar_turno(usuario, opt_name, pref)
            ).pack(pady=5)

        tk.Button(
            self.ventana_menu,
            text="Volver al Inicio",
            font=("Arial", 12),
            bg="gray",
            fg="white",
            command=self._volver_a_inicio_desde_menu
        ).pack(pady=20)

    def _mostrar_turno(self, usuario, opcion, prefix):
        turno = usuario.obtener_turno(prefix)
        messagebox.showinfo("Turno Generado", f"Ha seleccionado: {opcion}\nSu numero de turno es: {turno}")
        self.ventana_menu.destroy()
        self.root.deiconify()

    def _volver_a_inicio_desde_datos(self):
        self.ventana_datos.destroy()
        self.root.deiconify()

    def _volver_a_inicio_desde_menu(self):
        self.ventana_menu.destroy()
        self.root.deiconify()

# Iniciar aplicacion
if __name__ == "__main__":
    root = tk.Tk()
    app = DigiturnoApp(root)
    root.mainloop()
