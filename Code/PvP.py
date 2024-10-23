import tkinter as tk
from tkinter import messagebox


class PvP:
    def jugar_piedra(self):
        self.value_jugada_player[self.turno.get() - 1] = "Piedra"
        if self.turno.get() == 1:
            self.turno.set(2)
            self.marcador_turno.config(text="TURNO: JUGADOR " + str(self.turno.get()))
        else:
            self.turno.set(1)
            self.marcador_turno.config(text="TURNO: JUGADOR " + str(self.turno.get()))
            self.añadir_puntos(self.elegir_ganador())

    def jugar_papel(self):
        self.value_jugada_player[self.turno.get() - 1] = "Papel"
        if self.turno.get() == 1:
            self.turno.set(2)
            self.marcador_turno.config(text="TURNO: JUGADOR " + str(self.turno.get()))
        else:
            self.turno.set(1)
            self.marcador_turno.config(text="TURNO: JUGADOR " + str(self.turno.get()))
            self.añadir_puntos(self.elegir_ganador())

    def jugar_tijeras(self):
        self.value_jugada_player[self.turno.get() - 1] = "Tijeras"
        if self.turno.get() == 1:
            self.turno.set(2)
            self.marcador_turno.config(text="TURNO: JUGADOR " + str(self.turno.get()))
        else:
            self.turno.set(1)
            self.marcador_turno.config(text="TURNO: JUGADOR " + str(self.turno.get()))
            self.añadir_puntos(self.elegir_ganador())

    def elegir_ganador(self):
        resultado = None  # Inicializamos la variable para guardar al ganador
        self.root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
        if self.value_jugada_player[0] == "Piedra":
            if self.value_jugada_player[1] == "Piedra":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Es un empate.")
            elif self.value_jugada_player[1] == "Papel":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Gana el jugador 2.")
            elif self.value_jugada_player[1] == "Tijeras":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Gana el jugador 1.")
        elif self.value_jugada_player[0] == "Papel":
            if self.value_jugada_player[1] == "Piedra":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Gana el jugador 1.")
            elif self.value_jugada_player[1] == "Papel":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Es un empate.")
            elif self.value_jugada_player[1] == "Tijeras":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Gana el jugador 2.")
        elif self.value_jugada_player[0] == "Tijeras":
            if self.value_jugada_player[1] == "Piedra":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Gana el jugador 2.")
            elif self.value_jugada_player[1] == "Papel":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Gana el jugador 1.")
            elif self.value_jugada_player[1] == "Tijeras":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador 1 saca " + self.value_jugada_player[0] + ". El jugador 2 " +
                                    self.value_jugada_player[1] + ". Es un empate.")
        else:
            messagebox.showinfo("Error inesperado", "Cerrando la aplicación...")
            self.root.quit()

        self.root.attributes("-disabled",
                             False)  # Habilita de nuevo la ventana después de cerrar el messagebox correspondiente
        return resultado

    def añadir_puntos(self, res):
        if res > 0:  # Si gana el jugador 1
            self.puntos_player1.set(self.puntos_player1.get() + 1)
            self.puntuacion_jugador1.config(text="PUNTUACIÓN JUGADOR 1: " + str(self.puntos_player1.get()))
        elif res < 0:  # Si gana el jugador 2
            self.puntos_player2.set(self.puntos_player2.get() + 1)
            self.puntuacion_jugador2.config(text="PUNTUACIÓN JUGADOR 2: " + str(self.puntos_player2.get()))

        if self.puntos_player2.get() == 3 or self.puntos_player1.get() == 3:  # Si la partida se acaba, elige ganador
            if self.puntos_player2.get() == 3:
                self.root.attributes("-disabled", True)  # Deshabilita la ventana del juego para impedir bugs
                messagebox.showinfo("Partida terminada", "GANADOR: Jugador 2")
            else:
                messagebox.showinfo("Partida terminada", "GANADOR: Jugador 1")

            self.root.destroy()  # Cierra la partida, pero no la aplicación

    def __init__(self):
        # Ventana para la partida contra otro jugador
        self.root = tk.Toplevel()
        self.root.title("Jugador vs Jugador")
        self.root.geometry("800x600+300+50")

        # Jugadas
        self.value_jugada_player = ["", ""]

        # Turno
        self.turno = tk.IntVar()
        self.turno.set(1)

        # Puntuación
        self.puntos_player1 = tk.IntVar()
        self.puntos_player1.set(0)
        self.puntos_player2 = tk.IntVar()
        self.puntos_player2.set(0)

        # Grid
        tk.Label(self.root).grid(row=0, column=0)  # Label decorativa para centrar el grid

        self.marcador_turno = tk.Label(self.root, text="TURNO: JUGADOR " + str(self.turno.get()))
        self.marcador_turno.grid(row=1, column=2, columnspan=3)
        self.puntuacion_jugador1 = tk.Label(self.root, text="PUNTUACIÓN JUGADOR 1: " + str(self.puntos_player1.get()))
        self.puntuacion_jugador1.grid(row=2, column=1, columnspan=2, pady=20)
        self.puntuacion_jugador2 = tk.Label(self.root, text="PUNTUACIÓN JUGADOR 2: " + str(self.puntos_player2.get()))
        self.puntuacion_jugador2.grid(row=2, column=4, columnspan=2, pady=20)
        self.piedra = tk.Button(self.root, text="PIEDRA", command=self.jugar_piedra)
        self.piedra.grid(row=3, column=1, padx=15)
        self.papel = tk.Button(self.root, text="PAPEL", command=self.jugar_papel)
        self.papel.grid(row=3, column=3, padx=15)
        self.tijeras = tk.Button(self.root, text="TIJERAS", command=self.jugar_tijeras)
        self.tijeras.grid(row=3, column=5, padx=15)

        tk.Label(self.root).grid(row=10, column=10)  # Label decorativa para centrar el grid

        # Configuración grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(10, weight=1)
        self.root.grid_columnconfigure(10, weight=1)
