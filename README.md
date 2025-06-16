# Documentación del Código de Digiturno NuevaEPS

## Introducción

El proyecto **Digiturno NuevaEPS** es una aplicación que simula un sistema de turnos para usuarios, desarrollada con interfaz gráfica usando `tkinter`. Este sistema incluye conceptos de programación orientada a objetos, tales como herencia, polimorfismo, encapsulamiento y uso de clases abstractas.

---

## Características Principales

1. **Gestión de Turnos:**

   * Usuarios de tercera edad tienen atención prioritaria.
   * Los demás usuarios pueden seleccionar entre varias opciones de servicio.

2. **Interfaz Gráfica:**

   * Uso de tkinter para la creación de ventanas y botones interactivos.
   * Sistema de ventanas para capturar datos y seleccionar servicios.

3. **Estructura Modular:**

   * Clases separadas para cada tipo de usuario.
   * Gestor de turnos centralizado.

---

## Estructura del Código

### 1. Clases Principales

#### **Clase `Usuario` (Abstracta)**

Define la base para diferentes tipos de usuarios.

**Métodos:**

* `__init__(self, cedula, edad)`: Inicializa los atributos encapsulados.
* `obtener_turno()`: Método abstracto que las subclases deben implementar.

---

#### **Clase `UsuarioTerceraEdad` (Hereda de `Usuario`)**

Usuarios con atención prioritaria.

**Métodos:**

* `obtener_turno()`: Devuelve un turno con prefijo `X`.

---

#### **Clase `UsuarioGeneral` (Hereda de `Usuario`)**

Usuarios que seleccionan un tipo de servicio.

**Métodos:**

* `obtener_turno(tipo_servicio)`: Genera un turno basado en el servicio seleccionado.

---

#### **Clase `TurnoManager`**

Clase estática que gestiona la numeración de los turnos.

**Atributos:**

* `_contador_turnos`: Variable encapsulada que lleva el conteo.

**Métodos:**

* `siguiente_turno()`: Incrementa y devuelve el número del siguiente turno.

---

#### **Clase `DigiturnoApp`**

Controla toda la interfaz gráfica y la interacción con los usuarios.

**Métodos:**

* `_crear_interfaz_principal()`: Crea la ventana principal.
* `_mostrar_ventana_datos()`: Muestra una ventana para capturar cédula y edad.
* `_capturar_datos()`: Valida los datos ingresados por el usuario.
* `_mostrar_menu_o_turno(usuario)`: Decide si el usuario va directo al turno o selecciona un servicio.
* `_mostrar_ventana_menu(usuario)`: Presenta las opciones de servicios.
* `_mostrar_turno(usuario, opcion, prefix)`: Muestra el turno generado.

---

### 2. Flujo de la Aplicación

1. **Inicio:**

   * El usuario ve la ventana principal con un botón para obtener turno.

2. **Captura de Datos:**

   * Se solicita el número de cédula y la edad.
   * Validaciones aseguran que los datos sean correctos.

3. **Asignación de Turno:**

   * Si el usuario es mayor de 65 años, se le da un turno prioritario.
   * Otros usuarios eligen entre servicios disponibles y obtienen un turno con prefijo específico.

4. **Retorno al Inicio:**

   * Una vez asignado el turno, el sistema regresa a la ventana principal.

---

## Requerimientos del Sistema

1. **Software:**

   * Python 3.x
   * Módulo `tkinter` (instalado por defecto en la mayoría de las distribuciones de Python).

2. **Entorno de Ejecución:**

   * Sistema operativo con soporte gráfico (Windows, macOS o Linux).

---

## Posibles Mejoras

1. **Persistencia de Datos:**

   * Agregar una base de datos para guardar los turnos generados.

2. **Soporte Multilenguaje:**

   * Implementar traducciones para diferentes idiomas.

3. **Diseño Mejorado:**

   * Modernizar la interfaz gráfica con librerías como `ttk` o `customtkinter`.

---

## Créditos

**Desarrollador:**
Mai Col
Técnico en mantenimiento de equipos de cómputo
Estudiante de Ingeniería de Sistemas
