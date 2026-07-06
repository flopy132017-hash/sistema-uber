import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

# ----------------------------
# CONFIGURACIÓN
# ----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

conductores = ["Carlos", "Pedro", "Luis"]

indice_conductor = 0
conductor_actual = "Ninguno"

estado_viaje = "Sin viaje"

puntaje = 100
sanciones = 0

estado_conductor_actual = "Activo"
tiempo_suspension = 0

# ----------------------------
# FUNCIONES
# ----------------------------

def hora():
    return datetime.now().strftime("%H:%M:%S")


def agregar_historial(texto):
    mensaje = f"[{hora()}] {texto}\n"

    historial_usuario.insert("end", mensaje)
    historial_usuario.see("end")

    historial_conductor.insert("end", mensaje)
    historial_conductor.see("end")


def actualizar():
    estado_usuario_label.configure(
        text=f"Estado: {estado_viaje}"
    )

    conductor_usuario_label.configure(
        text=f"Conductor: {conductor_actual}"
    )

    estado_conductor_label.configure(
        text=f"Estado Viaje: {estado_viaje}"
    )

    sanciones_label.configure(
        text=f"Sanciones: {sanciones}"
    )

    puntaje_label.configure(
        text=f"Puntaje: {puntaje}"
    )

    estado_driver_label.configure(
        text=f"Estado Conductor: {estado_conductor_actual}"
    )

    suspension_label.configure(
        text=f"Tiempo suspensión: {tiempo_suspension}s"
    )

    if estado_conductor_actual == "SUSPENDIDO PERMANENTE":
        aceptar_btn.configure(state="disabled")
        cancelar_conductor_btn.configure(state="disabled")

    elif estado_conductor_actual == "SUSPENDIDO TEMPORAL":
        aceptar_btn.configure(state="disabled")
        cancelar_conductor_btn.configure(state="disabled")

    else:
        aceptar_btn.configure(state="normal")
        cancelar_conductor_btn.configure(state="normal")


def contar_suspension():
    global tiempo_suspension
    global estado_conductor_actual

    if tiempo_suspension > 0:

        suspension_label.configure(
            text=f"Tiempo suspensión: {tiempo_suspension}s"
        )

        tiempo_suspension -= 1

        conductor_window.after(
            1000,
            contar_suspension
        )

    else:

        estado_conductor_actual = "Activo"

        agregar_historial(
            "Suspensión temporal finalizada."
        )

        actualizar()


def solicitar_viaje():
    global estado_viaje
    global conductor_actual

    if estado_conductor_actual == "SUSPENDIDO PERMANENTE":
        messagebox.showerror(
            "Error",
            "No hay conductores disponibles."
        )
        return

    estado_viaje = "Pendiente"

    conductor_actual = conductores[indice_conductor]

    agregar_historial(
        f"Usuario solicitó un viaje."
    )

    agregar_historial(
        f"Conductor asignado: {conductor_actual}"
    )

    actualizar()


def aceptar_viaje():
    global estado_viaje

    if conductor_actual == "Ninguno":
        return

    estado_viaje = "Aceptado"

    agregar_historial(
        f"{conductor_actual} aceptó el viaje."
    )

    actualizar()


def cancelar_usuario():
    global estado_viaje

    estado_viaje = "Cancelado por usuario"

    agregar_historial(
        "Usuario canceló el viaje."
    )

    actualizar()


def reportar_incidencia():

    agregar_historial(
        "Usuario reportó una incidencia."
    )

    messagebox.showinfo(
        "Incidencia",
        "Incidencia registrada correctamente."
    )


def cancelar_conductor():

    global puntaje
    global sanciones
    global conductor_actual
    global indice_conductor
    global estado_viaje
    global estado_conductor_actual
    global tiempo_suspension

    if conductor_actual == "Ninguno":
        return

    sanciones += 1
    puntaje -= 10

    agregar_historial(
        f"{conductor_actual} canceló el viaje."
    )

    agregar_historial(
        f"-10 puntos aplicados."
    )

    agregar_historial(
        f"Puntaje actual: {puntaje}"
    )

    # ----------------------------
    # SUSPENSIÓN PERMANENTE
    # ----------------------------

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

    # ----------------------------
    # SUSPENSIÓN TEMPORAL
    # ----------------------------

    if puntaje <= 70 and estado_conductor_actual != "SUSPENDIDO TEMPORAL":

        estado_conductor_actual = "SUSPENDIDO TEMPORAL"

        tiempo_suspension = 30

        agregar_historial(
            f"{conductor_actual} suspendido temporalmente por 30 segundos."
        )

        contar_suspension()

    # ----------------------------
    # REASIGNACIÓN
    # ----------------------------

    conductor_anterior = conductor_actual

    indice_conductor += 1

    if indice_conductor >= len(conductores):
        indice_conductor = 0

    conductor_actual = conductores[indice_conductor]

    estado_viaje = "Reasignado"

    agregar_historial(
        f"Usuario notificado: {conductor_anterior} canceló el viaje."
    )

    agregar_historial(
        f"Se ha reasignado automáticamente un nuevo conductor."
    )

    agregar_historial(
        f"Nuevo conductor: {conductor_actual}"
    )

    actualizar()


# -------------------------------------------------
# VENTANA USUARIO
# -------------------------------------------------

usuario = ctk.CTk()
usuario.title("Usuario")
usuario.geometry("550x650")

titulo_usuario = ctk.CTkLabel(
    usuario,
    text="👤 PANEL USUARIO",
    font=("Arial", 24, "bold")
)

titulo_usuario.pack(pady=15)

estado_usuario_label = ctk.CTkLabel(
    usuario,
    text="Estado: Sin viaje"
)

estado_usuario_label.pack(pady=5)

conductor_usuario_label = ctk.CTkLabel(
    usuario,
    text="Conductor: Ninguno"
)

conductor_usuario_label.pack(pady=5)

ctk.CTkButton(
    usuario,
    text="Solicitar Viaje",
    command=solicitar_viaje
).pack(pady=5)

ctk.CTkButton(
    usuario,
    text="Cancelar Viaje",
    command=cancelar_usuario
).pack(pady=5)

ctk.CTkButton(
    usuario,
    text="Reportar Incidencia",
    command=reportar_incidencia
).pack(pady=5)

ctk.CTkLabel(
    usuario,
    text="Historial"
).pack(pady=10)

historial_usuario = ctk.CTkTextbox(
    usuario,
    width=480,
    height=300
)

historial_usuario.pack(pady=10)

# -------------------------------------------------
# VENTANA CONDUCTOR
# -------------------------------------------------

conductor_window = ctk.CTkToplevel(usuario)
conductor_window.title("Conductor")
conductor_window.geometry("550x650")

titulo_conductor = ctk.CTkLabel(
    conductor_window,
    text="🚗 PANEL CONDUCTOR",
    font=("Arial", 24, "bold")
)

titulo_conductor.pack(pady=15)

estado_conductor_label = ctk.CTkLabel(
    conductor_window,
    text="Estado Viaje: Sin viaje"
)

estado_conductor_label.pack(pady=5)

sanciones_label = ctk.CTkLabel(
    conductor_window,
    text="Sanciones: 0"
)

sanciones_label.pack(pady=5)

puntaje_label = ctk.CTkLabel(
    conductor_window,
    text="Puntaje: 100"
)

puntaje_label.pack(pady=5)

estado_driver_label = ctk.CTkLabel(
    conductor_window,
    text="Estado Conductor: Activo"
)

estado_driver_label.pack(pady=5)

suspension_label = ctk.CTkLabel(
    conductor_window,
    text="Tiempo suspensión: 0s"
)

suspension_label.pack(pady=5)

aceptar_btn = ctk.CTkButton(
    conductor_window,
    text="Aceptar Viaje",
    command=aceptar_viaje
)

aceptar_btn.pack(pady=5)

cancelar_conductor_btn = ctk.CTkButton(
    conductor_window,
    text="Cancelar Viaje",
    command=cancelar_conductor
)

cancelar_conductor_btn.pack(pady=5)

ctk.CTkLabel(
    conductor_window,
    text="Historial"
).pack(pady=10)

historial_conductor = ctk.CTkTextbox(
    conductor_window,
    width=480,
    height=300
)

historial_conductor.pack(pady=10)

actualizar()

usuario.mainloop()