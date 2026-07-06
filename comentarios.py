"""
=========================================================
            SISTEMA DE GESTIÓN DE VIAJES TIPO UBER
=========================================================

Autor      : Tu nombre
Versión    : 1.0
Fecha      : Julio 2026

Descripción:
-------------
Sistema desarrollado como prototipo para simular el
proceso de solicitud de viajes, aceptación,
cancelación, reasignación automática de conductores
y aplicación de sanciones.

Características:
- Solicitud de viaje.
- Asignación automática de conductor.
- Cancelación por pasajero.
- Cancelación por conductor.
- Reasignación automática.
- Sistema de sanciones.
- Suspensión temporal.
- Suspensión permanente.
- Registro de historial.
- Interfaz gráfica con CustomTkinter.

Librerías utilizadas:
- customtkinter
- tkinter
- datetime

=========================================================
"""

# ----------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ----------------------------

import customtkinter as ctk  # Librería para interfaz gráfica moderna
from tkinter import messagebox  # Ventanas emergentes de alerta
from datetime import datetime  # Manejo de fecha y hora

# ----------------------------
# CONFIGURACIÓN DE LA INTERFAZ
# ----------------------------

ctk.set_appearance_mode("dark")  # Tema oscuro
ctk.set_default_color_theme("blue")  # Color azul por defecto

# ----------------------------
# VARIABLES GLOBALES DEL SISTEMA
# ----------------------------

# Lista de conductores disponibles
conductores = ["Carlos", "Pedro", "Luis"]

# Índice del conductor actual asignado
indice_conductor = 0

# Conductor actualmente asignado al viaje
conductor_actual = "Ninguno"

# Estado del viaje (Sin viaje, Pendiente, Aceptado, etc.)
estado_viaje = "Sin viaje"

# Puntaje del conductor (sistema de reputación)
puntaje = 100

# Número de sanciones acumuladas
sanciones = 0

# Estado del conductor (Activo, Suspendido temporal, etc.)
estado_conductor_actual = "Activo"

# Tiempo restante de suspensión temporal (segundos)
tiempo_suspension = 0

# ----------------------------
# FUNCIONES DEL SISTEMA
# ----------------------------

def hora():
    """
    Retorna la hora actual del sistema.

    Returns:
        str: Hora en formato HH:MM:SS
    """
    return datetime.now().strftime("%H:%M:%S")


def agregar_historial(texto):
    """
    Agrega un mensaje al historial del usuario y del conductor.

    Args:
        texto (str): Mensaje a registrar en el historial.
    """

    # Construcción del mensaje con hora
    mensaje = f"[{hora()}] {texto}\n"

    # Agregar al historial del usuario
    historial_usuario.insert("end", mensaje)
    historial_usuario.see("end")

def actualizar():
    """
    Actualiza todos los elementos de la interfaz gráfica
    con los valores actuales del sistema.

    Esta función sincroniza la información del estado del viaje,
    conductor, sanciones, puntaje y estado del conductor en la UI.

    También controla el estado de los botones según si el conductor
    está activo o suspendido.
    """

    # ----------------------------
    # ACTUALIZACIÓN DE ETIQUETAS DEL USUARIO
    # ----------------------------

    estado_usuario_label.configure(
        text=f"Estado: {estado_viaje}"
    )  # Muestra el estado actual del viaje

    conductor_usuario_label.configure(
        text=f"Conductor: {conductor_actual}"
    )  # Muestra el conductor asignado

    # ----------------------------
    # ACTUALIZACIÓN DEL PANEL DEL CONDUCTOR
    # ----------------------------

    estado_conductor_label.configure(
        text=f"Estado Viaje: {estado_viaje}"
    )  # Estado del viaje en el panel conductor

    sanciones_label.configure(
        text=f"Sanciones: {sanciones}"
    )  # Número de sanciones acumuladas

    puntaje_label.configure(
        text=f"Puntaje: {puntaje}"
    )  # Puntaje actual del conductor

    estado_driver_label.configure(
        text=f"Estado Conductor: {estado_conductor_actual}"
    )  # Estado general del conductor

    suspension_label.configure(
        text=f"Tiempo suspensión: {tiempo_suspension}s"
    )  # Tiempo restante de suspensión

    # ----------------------------
    # CONTROL DE BOTONES SEGÚN ESTADO DEL CONDUCTOR
    # ----------------------------

    if estado_conductor_actual == "SUSPENDIDO PERMANENTE":
        aceptar_btn.configure(state="disabled")
        cancelar_conductor_btn.configure(state="disabled")

    elif estado_conductor_actual == "SUSPENDIDO TEMPORAL":
        aceptar_btn.configure(state="disabled")
        cancelar_conductor_btn.configure(state="disabled")

    else:
        aceptar_btn.configure(state="normal")
        cancelar_conductor_btn.configure(state="normal")

    # =========================================================
# FUNCIÓN: SOLICITAR VIAJE
# =========================================================

def solicitar_viaje():
    """
    Permite al usuario solicitar un viaje.

    Verifica si el conductor está disponible.
    Si no está suspendido permanentemente, asigna un conductor
    automáticamente y actualiza el estado del viaje a "Pendiente".

    También registra el evento en el historial del sistema.
    """

    global estado_viaje
    global conductor_actual

    # Verifica si el conductor está suspendido permanentemente
    if estado_conductor_actual == "SUSPENDIDO PERMANENTE":
        messagebox.showerror(
            "Error",
            "No hay conductores disponibles."
        )
        return

    # Cambia el estado del viaje
    estado_viaje = "Pendiente"

    # Asigna el conductor actual de la lista
    conductor_actual = conductores[indice_conductor]

    # Registra eventos en el historial
    agregar_historial("Usuario solicitó un viaje.")
    agregar_historial(f"Conductor asignado: {conductor_actual}")

    # Actualiza la interfaz gráfica
    actualizar()


# =========================================================
# FUNCIÓN: ACEPTAR VIAJE
# =========================================================

def aceptar_viaje():
    """
    Permite al conductor aceptar un viaje solicitado.

    Cambia el estado del viaje a "Aceptado" y registra el evento
    en el historial del sistema.
    """

    global estado_viaje

    # Verifica si existe un conductor válido
    if conductor_actual == "Ninguno":
        return

    # Actualiza estado del viaje
    estado_viaje = "Aceptado"

    # Registra acción en historial
    agregar_historial(f"{conductor_actual} aceptó el viaje.")

    # Actualiza interfaz
    actualizar()


# =========================================================
# FUNCIÓN: CANCELAR VIAJE (USUARIO)
# =========================================================

def cancelar_usuario():
    """
    Permite al usuario cancelar un viaje en curso.

    Cambia el estado del viaje a "Cancelado por usuario"
    y registra la acción en el historial.
    """

    global estado_viaje

    # Actualiza estado del viaje
    estado_viaje = "Cancelado por usuario"

    # Registro en historial
    agregar_historial("Usuario canceló el viaje.")

    # Actualiza interfaz
    actualizar()


# =========================================================
# FUNCIÓN: REPORTAR INCIDENCIA
# =========================================================

def reportar_incidencia():
    """
    Permite al usuario reportar una incidencia.

    Registra el evento en el historial y muestra una alerta
    de confirmación.
    """

    # Registro en historial
    agregar_historial("Usuario reportó una incidencia.")

    # Mensaje de confirmación
    messagebox.showinfo(
        "Incidencia",
        "Incidencia registrada correctamente."
    )


# =========================================================
# FUNCIÓN: CANCELAR VIAJE (CONDUCTOR)
# =========================================================

def cancelar_conductor():
    """
    Permite al conductor cancelar un viaje.

    Aplica sanciones al conductor, reduce su puntaje y evalúa
    si debe ser suspendido temporal o permanentemente.
    También reasigna automáticamente un nuevo conductor.
    """

    global puntaje
    global sanciones
    global conductor_actual
    global indice_conductor
    global estado_viaje
    global estado_conductor_actual
    global tiempo_suspension

    # Si no hay conductor asignado, no hace nada
    if conductor_actual == "Ninguno":
        return

    # Incrementa sanciones y reduce puntaje
    sanciones += 1
    puntaje -= 10

    # Registros en historial
    agregar_historial(f"{conductor_actual} canceló el viaje.")
    agregar_historial("-10 puntos aplicados.")
    agregar_historial(f"Puntaje actual: {puntaje}")

    # -----------------------------------------------------
    # SUSPENSIÓN PERMANENTE
    # -----------------------------------------------------

    if puntaje <= 0:

        puntaje = 0
        estado_conductor_actual = "SUSPENDIDO PERMANENTE"

        agregar_historial(
            f"{conductor_actual} fue suspendido PERMANENTEMENTE."
        )

        actualizar()

        messagebox.showerror(
            "Suspensión Permanente",
            "El conductor ha sido suspendido permanentemente."
        )

        return

    # -----------------------------------------------------
    # SUSPENSIÓN TEMPORAL
    # -----------------------------------------------------

    if puntaje <= 70 and estado_conductor_actual != "SUSPENDIDO TEMPORAL":

        estado_conductor_actual = "SUSPENDIDO TEMPORAL"
        tiempo_suspension = 30

        agregar_historial(
            f"{conductor_actual} suspendido temporalmente por 30 segundos."
        )

        contar_suspension()
        # ----------------------------
# REASIGNACIÓN AUTOMÁTICA DE CONDUCTOR
# ----------------------------

# Se guarda el conductor actual antes de ser reemplazado
conductor_anterior = conductor_actual

# Se incrementa el índice para pasar al siguiente conductor
indice_conductor += 1

# Si el índice supera la cantidad de conductores, se reinicia (ciclo circular)
if indice_conductor >= len(conductores):
    indice_conductor = 0

# Se asigna el nuevo conductor según el índice actualizado
conductor_actual = conductores[indice_conductor]

# Se actualiza el estado del viaje a "Reasignado"
estado_viaje = "Reasignado"

# Registro en el historial del sistema para el usuario
agregar_historial(
    f"Usuario notificado: {conductor_anterior} canceló el viaje."
)

# Registro de evento de reasignación automática
agregar_historial(
    "Se ha reasignado automáticamente un nuevo conductor."
)

# Registro del nuevo conductor asignado
agregar_historial(
    f"Nuevo conductor: {conductor_actual}"
)

# Se actualiza toda la interfaz gráfica con los nuevos valores
actualizar()


# =========================================================
# INTERFAZ GRÁFICA - VENTANA DE USUARIO
# =========================================================

# Creación de la ventana principal del usuario
usuario = ctk.CTk()
usuario.title("Usuario")              # Título de la ventana
usuario.geometry("550x650")           # Tamaño de la ventana

# Título visual del panel de usuario
titulo_usuario = ctk.CTkLabel(
    usuario,
    text="👤 PANEL USUARIO",
    font=("Arial", 24, "bold")
)
titulo_usuario.pack(pady=15)

# Etiqueta que muestra el estado actual del usuario (viaje)
estado_usuario_label = ctk.CTkLabel(
    usuario,
    text="Estado: Sin viaje"
)
estado_usuario_label.pack(pady=5)

# Etiqueta que muestra el conductor asignado
conductor_usuario_label = ctk.CTkLabel(
    usuario,
    text="Conductor: Ninguno"
)
conductor_usuario_label.pack(pady=5)

# Botón para solicitar un viaje
ctk.CTkButton(
    usuario,
    text="Solicitar Viaje",
    command=solicitar_viaje
).pack(pady=5)

# Botón para cancelar el viaje desde el usuario
ctk.CTkButton(
    usuario,
    text="Cancelar Viaje",
    command=cancelar_usuario
).pack(pady=5)

# Botón para reportar una incidencia
ctk.CTkButton(
    usuario,
    text="Reportar Incidencia",
    command=reportar_incidencia
).pack(pady=5)

# Título del historial de eventos del usuario
ctk.CTkLabel(
    usuario,
    text="Historial"
).pack(pady=10)

# Área de texto donde se muestra el historial de acciones del usuario
historial_usuario = ctk.CTkTextbox(
    usuario,
    width=480,
    height=300
)
historial_usuario.pack(pady=10)
# -------------------------------------------------
# VENTANA PRINCIPAL DEL CONDUCTOR (INTERFAZ GRÁFICA)
# -------------------------------------------------

# Se crea una ventana secundaria (Toplevel) dependiente del usuario
# Esta ventana representa el panel del conductor
conductor_window = ctk.CTkToplevel(usuario)

# Título de la ventana del conductor
conductor_window.title("Conductor")

# Tamaño de la ventana (ancho x alto)
conductor_window.geometry("550x650")


# -------------------------------------------------
# TÍTULO DEL PANEL
# -------------------------------------------------

# Etiqueta principal del panel del conductor
titulo_conductor = ctk.CTkLabel(
    conductor_window,
    text="🚗 PANEL CONDUCTOR",
    font=("Arial", 24, "bold")
)

# Se posiciona en la ventana con espacio vertical
titulo_conductor.pack(pady=15)


# -------------------------------------------------
# INDICADORES DE ESTADO DEL CONDUCTOR
# -------------------------------------------------

# Muestra el estado del viaje del conductor
estado_conductor_label = ctk.CTkLabel(
    conductor_window,
    text="Estado Viaje: Sin viaje"
)
estado_conductor_label.pack(pady=5)


# Muestra la cantidad de sanciones acumuladas
sanciones_label = ctk.CTkLabel(
    conductor_window,
    text="Sanciones: 0"
)
sanciones_label.pack(pady=5)


# Muestra el puntaje de reputación del conductor
puntaje_label = ctk.CTkLabel(
    conductor_window,
    text="Puntaje: 100"
)
puntaje_label.pack(pady=5)


# Muestra el estado general del conductor (Activo / Suspendido)
estado_driver_label = ctk.CTkLabel(
    conductor_window,
    text="Estado Conductor: Activo"
)
estado_driver_label.pack(pady=5)


# Muestra el tiempo restante de suspensión (si aplica)
suspension_label = ctk.CTkLabel(
    conductor_window,
    text="Tiempo suspensión: 0s"
)
suspension_label.pack(pady=5)


# -------------------------------------------------
# BOTONES DE ACCIÓN DEL CONDUCTOR
# -------------------------------------------------

# Botón para aceptar el viaje asignado
aceptar_btn = ctk.CTkButton(
    conductor_window,
    text="Aceptar Viaje",
    command=aceptar_viaje
)
aceptar_btn.pack(pady=5)


# Botón para cancelar el viaje (genera sanciones)
cancelar_conductor_btn = ctk.CTkButton(
    conductor_window,
    text="Cancelar Viaje",
    command=cancelar_conductor
)
cancelar_conductor_btn.pack(pady=5)


# -------------------------------------------------
# HISTORIAL DE EVENTOS DEL CONDUCTOR
# -------------------------------------------------

# Título del historial
ctk.CTkLabel(
    conductor_window,
    text="Historial"
).pack(pady=10)


# Área de texto donde se registran eventos del conductor
historial_conductor = ctk.CTkTextbox(
    conductor_window,
    width=480,
    height=300
)

historial_conductor.pack(pady=10)


# -------------------------------------------------
# INICIALIZACIÓN DEL SISTEMA
# -------------------------------------------------

# Actualiza todos los valores de la interfaz al iniciar
actualizar()

# Inicia el loop principal de la interfaz gráfica (ventana usuario)
usuario.mainloop()