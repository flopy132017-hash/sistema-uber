import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

# ----------------------------
# VARIABLES GLOBALES
# ----------------------------

conductores = ["Carlos", "Pedro", "Luis"]
indice_conductor = 0
conductor_actual = "Ninguno"

estado_viaje = "Sin viaje"

puntaje = 100
sanciones = 0

estado_conductor_actual = "Activo"
tiempo_suspension = 0


# ----------------------------
# FUNCIONES LÓGICAS (TESTEABLES)
# ----------------------------

def hora():
    return datetime.now().strftime("%H:%M:%S")


def reset_estado():
    global puntaje, sanciones, estado_conductor_actual, estado_viaje, indice_conductor, conductor_actual

    puntaje = 100
    sanciones = 0
    estado_conductor_actual = "Activo"
    estado_viaje = "Sin viaje"
    indice_conductor = 0
    conductor_actual = "Ninguno"


def solicitar_viaje_logica():
    global estado_viaje, conductor_actual

    if estado_conductor_actual == "SUSPENDIDO PERMANENTE":
        return "ERROR"

    estado_viaje = "Pendiente"
    conductor_actual = conductores[indice_conductor]

    return "OK"


def aceptar_viaje_logica():
    global estado_viaje

    if conductor_actual == "Ninguno":
        return "ERROR"

    estado_viaje = "Aceptado"
    return "OK"


def cancelar_usuario_logica():
    global estado_viaje

    estado_viaje = "Cancelado por usuario"
    return "OK"


def cancelar_conductor_logica():
    global puntaje, sanciones, estado_conductor_actual

    sanciones += 1
    puntaje -= 10

    if puntaje <= 0:
        puntaje = 0
        estado_conductor_actual = "SUSPENDIDO PERMANENTE"
        return "SUSPENDIDO"

    if puntaje <= 70:
        estado_conductor_actual = "SUSPENDIDO TEMPORAL"

    return "OK"