import tkinter as tk
from math import floor
from random import random
from tkinter import messagebox


class PvE:
    def jugar_piedra(self):
        self.value_jugada_player.set("Piedra")
        self.jugar_IA()
        self.añadir_puntos(self.elegir_ganador())

    def jugar_papel(self):
        self.value_jugada_player.set("Papel")
        self.jugar_IA()
        self.añadir_puntos(self.elegir_ganador())

    def jugar_tijeras(self):
        self.value_jugada_player.set("Tijeras")
        self.jugar_IA()
        self.añadir_puntos(self.elegir_ganador())

    def jugar_IA(self):
        jugada_IA = floor((random() * 100) % 3)  # Selecciona un número del 0 al 2 aleatorio
        if jugada_IA == 0:
            self.value_jugada_IA.set("Piedra")
        elif jugada_IA == 1:
            self.value_jugada_IA.set("Papel")
        elif jugada_IA == 2:
            self.value_jugada_IA.set("Tijeras")
        else:
            self.root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
            messagebox.showinfo("Número no encontrado", "Cerrando la partida...")
            self.root.destroy()

    def elegir_ganador(self):
        resultado = None  # Inicializamos la variable para guardar al ganador
        self.root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
        if self.value_jugada_player.get() == "Piedra":
            if self.value_jugada_IA.get() == "Piedra":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Es un empate.")
            elif self.value_jugada_IA.get() == "Papel":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Gana la IA.")
            elif self.value_jugada_IA.get() == "Tijeras":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Ganas tú.")
        elif self.value_jugada_player.get() == "Papel":
            if self.value_jugada_IA.get() == "Piedra":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Ganas tú.")
            elif self.value_jugada_IA.get() == "Papel":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Es un empate.")
            elif self.value_jugada_IA.get() == "Tijeras":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Gana la IA.")
        elif self.value_jugada_player.get() == "Tijeras":
            if self.value_jugada_IA.get() == "Piedra":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Gana la IA.")
            elif self.value_jugada_IA.get() == "Papel":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Ganas tú.")
            elif self.value_jugada_IA.get() == "Tijeras":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador saca " + self.value_jugada_player.get() + ". La IA saca " + self.value_jugada_IA.get() + ". Es un empate.")
        else:
            messagebox.showinfo("Error inesperado", "Cerrando la aplicación...")
            self.root.quit()

        self.root.attributes("-disabled",
                             False)  # Habilita de nuevo la ventana después de cerrar el messagebox correspondiente
        return resultado

    def añadir_puntos(self, res):
        if res > 0:  # Si gana el jugador, actualiza su marcador
            self.puntos_player.set(self.puntos_player.get() + 1)
            self.puntuacion_jugador1.config(text="PUNTUACIÓN JUGADOR: " + str(self.puntos_player.get()))
        elif res < 0:  # Si gana la máquina, actualiza su marcador
            self.puntos_IA.set(self.puntos_IA.get() + 1)
            self.puntuacion_jugador2.config(text="PUNTUACIÓN IA: " + str(self.puntos_IA.get()))

        if self.puntos_IA.get() == 3 or self.puntos_player.get() == 3:  # Si la partida se acaba, elige ganador
            self.root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
            if self.puntos_IA.get() == 3:
                messagebox.showinfo("Partida terminada", "GANADOR: IA")
            else:
                messagebox.showinfo("Partida terminada", "GANADOR: TÚ")

            self.root.destroy()  # Cierra la partida, pero no la aplicación

    def __init__(self):
        # Ventana para la partida contra la máquina
        self.root = tk.Toplevel()
        self.root.title("Jugador vs IA")
        self.root.geometry("800x600+300+50")

        # Jugadas
        self.value_jugada_player = tk.StringVar()
        self.value_jugada_player.set(str(None))
        self.value_jugada_IA = tk.StringVar()
        self.value_jugada_IA.set(str(None))

        # Puntuación
        self.puntos_player = tk.IntVar()
        self.puntos_player.set(0)
        self.puntos_IA = tk.IntVar()
        self.puntos_IA.set(0)

        # Grid
        tk.Label(self.root).grid(row=0, column=0)  # Label decorativa para centrar el grid

        self.puntuacion_jugador1 = tk.Label(self.root, text="PUNTUACIÓN JUGADOR: " + str(self.puntos_player.get()))
        self.puntuacion_jugador1.grid(row=1, column=1, columnspan=2, pady=20)
        self.puntuacion_jugador2 = tk.Label(self.root, text="PUNTUACIÓN IA: " + str(self.puntos_IA.get()))
        self.puntuacion_jugador2.grid(row=1, column=4, columnspan=2, pady=20)
        self.piedra = tk.Button(self.root, text="PIEDRA", command=self.jugar_piedra)
        self.piedra.grid(row=2, column=1, padx=15)
        self.papel = tk.Button(self.root, text="PAPEL", command=self.jugar_papel)
        self.papel.grid(row=2, column=3, padx=15)
        self.tijeras = tk.Button(self.root, text="TIJERAS", command=self.jugar_tijeras)
        self.tijeras.grid(row=2, column=5, padx=15)

        tk.Label(self.root).grid(row=10, column=10)  # Label decorativa para centrar el grid

        # Configuración grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(10, weight=1)
        self.root.grid_columnconfigure(10, weight=1)
