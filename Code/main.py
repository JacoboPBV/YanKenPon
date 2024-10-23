import tkinter as tk
"""
from math import floor
from random import random
from tkinter import messagebox
"""
import PvE
import PvP

# Ventana que va a contener el menú
main = tk.Tk()
main.title("Piedra, papel, tijera")
main.geometry("200x100+50+50")


def nuevo_pve():
    PvE.PvE()


def nuevo_pvp():
    PvP.PvP()


def salir():
    main.destroy()


# Menu
menu = tk.Menu(main)
main.config(menu=menu)

menu_partida = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Partida", menu=menu_partida)
menu_partida.add_command(label="Nueva Partida vs IA", command=nuevo_pve)
menu_partida.add_command(label="Nueva partida vs Jugador", command=nuevo_pvp)
menu.add_command(label="Salir", command=salir)

# Mainloop
main.mainloop()

"""
def nueva_partida_vs_ia():
    # Ventana para la partida contra la máquina
    root = tk.Toplevel()
    root.title("Jugador vs IA")
    root.geometry("800x600+300+50")

    def jugar_piedra():
        value_jugada_player.set("Piedra")
        jugar_IA()
        añadir_puntos(elegir_ganador())

    def jugar_papel():
        value_jugada_player.set("Papel")
        jugar_IA()
        añadir_puntos(elegir_ganador())

    def jugar_tijeras():
        value_jugada_player.set("Tijeras")
        jugar_IA()
        añadir_puntos(elegir_ganador())

    def jugar_IA():
        jugada_IA = floor((random() * 100) % 3)  # Selecciona un número del 0 al 2 aleatorio
        if jugada_IA == 0:
            value_jugada_IA.set("Piedra")
        elif jugada_IA == 1:
            value_jugada_IA.set("Papel")
        elif jugada_IA == 2:
            value_jugada_IA.set("Tijeras")
        else:
            root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
            messagebox.showinfo("Número no encontrado", "Cerrando la partida...")
            root.destroy()

    def elegir_ganador():
        resultado = None  # Inicializamos la variable para guardar al ganador
        root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
        if value_jugada_player.get() == "Piedra":
            if value_jugada_IA.get() == "Piedra":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Es un empate.")
            elif value_jugada_IA.get() == "Papel":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Gana la IA.")
            elif value_jugada_IA.get() == "Tijeras":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Ganas tú.")
        elif value_jugada_player.get() == "Papel":
            if value_jugada_IA.get() == "Piedra":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Ganas tú.")
            elif value_jugada_IA.get() == "Papel":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Es un empate.")
            elif value_jugada_IA.get() == "Tijeras":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Gana la IA.")
        elif value_jugada_player.get() == "Tijeras":
            if value_jugada_IA.get() == "Piedra":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Gana la IA.")
            elif value_jugada_IA.get() == "Papel":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Ganas tú.")
            elif value_jugada_IA.get() == "Tijeras":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador saca " + value_jugada_player.get() + ". La IA saca " + value_jugada_IA.get() + ". Es un empate.")
        else:
            messagebox.showinfo("Error inesperado", "Cerrando la aplicación...")
            root.quit()

        root.attributes("-disabled",
                        False)  # Habilita de nuevo la ventana después de cerrar el messagebox correspondiente
        return resultado

    def añadir_puntos(res):
        if res > 0:  # Si gana el jugador, actualiza su marcador
            puntos_player.set(puntos_player.get() + 1)
            puntuacion_jugador1.config(text="PUNTUACIÓN JUGADOR: " + str(puntos_player.get()))
        elif res < 0:  # Si gana la máquina, actualiza su marcador
            puntos_IA.set(puntos_IA.get() + 1)
            puntuacion_jugador2.config(text="PUNTUACIÓN IA: " + str(puntos_IA.get()))

        if puntos_IA.get() == 3 or puntos_player.get() == 3:  # Si la partida se acaba, elige ganador
            root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
            if puntos_IA.get() == 3:
                messagebox.showinfo("Partida terminada", "GANADOR: IA")
            else:
                messagebox.showinfo("Partida terminada", "GANADOR: TÚ")

            root.destroy()  # Cierra la partida, pero no la aplicación

    tk.Label(root).grid(row=0, column=0)  # Label decorativa para centrar el grid

    # Jugadas
    value_jugada_player = tk.StringVar()
    value_jugada_player.set(str(None))
    value_jugada_IA = tk.StringVar()
    value_jugada_IA.set(str(None))

    # Puntuación
    puntos_player = tk.IntVar()
    puntos_player.set(0)
    puntos_IA = tk.IntVar()
    puntos_IA.set(0)

    # Grid
    puntuacion_jugador1 = tk.Label(root, text="PUNTUACIÓN JUGADOR: " + str(puntos_player.get()))
    puntuacion_jugador1.grid(row=1, column=1, columnspan=2, pady=20)
    puntuacion_jugador2 = tk.Label(root, text="PUNTUACIÓN IA: " + str(puntos_IA.get()))
    puntuacion_jugador2.grid(row=1, column=4, columnspan=2, pady=20)
    piedra = tk.Button(root, text="PIEDRA", command=jugar_piedra)
    piedra.grid(row=2, column=1, padx=15)
    papel = tk.Button(root, text="PAPEL", command=jugar_papel)
    papel.grid(row=2, column=3, padx=15)
    tijeras = tk.Button(root, text="TIJERAS", command=jugar_tijeras)
    tijeras.grid(row=2, column=5, padx=15)

    tk.Label(root).grid(row=10, column=10)  # Label decorativa para centrar el grid

    # Configuración grid
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(10, weight=1)
    root.grid_columnconfigure(10, weight=1)


def nueva_partida_vs_jugador():
    # Ventana para la partida contra otro jugador
    root = tk.Toplevel()
    root.title("Jugador vs Jugador")
    root.geometry("800x600+300+50")

    def jugar_piedra():
        value_jugada_player[turno.get() - 1] = "Piedra"
        if turno.get() == 1:
            turno.set(2)
            marcador_turno.config(text="TURNO: JUGADOR " + str(turno.get()))
        else:
            turno.set(1)
            marcador_turno.config(text="TURNO: JUGADOR " + str(turno.get()))
            añadir_puntos(elegir_ganador())

    def jugar_papel():
        value_jugada_player[turno.get() - 1] = "Papel"
        if turno.get() == 1:
            turno.set(2)
            marcador_turno.config(text="TURNO: JUGADOR " + str(turno.get()))
        else:
            turno.set(1)
            marcador_turno.config(text="TURNO: JUGADOR " + str(turno.get()))
            añadir_puntos(elegir_ganador())

    def jugar_tijeras():
        value_jugada_player[turno.get() - 1] = "Tijeras"
        if turno.get() == 1:
            turno.set(2)
            marcador_turno.config(text="TURNO: JUGADOR " + str(turno.get()))
        else:
            turno.set(1)
            marcador_turno.config(text="TURNO: JUGADOR " + str(turno.get()))
            añadir_puntos(elegir_ganador())

    def elegir_ganador():
        resultado = None  # Inicializamos la variable para guardar al ganador
        root.attributes("-disabled", True)  # Deshabilita la ventana de juego para impedir bugs
        if value_jugada_player[0] == "Piedra":
            if value_jugada_player[1] == "Piedra":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Es un empate.")
            elif value_jugada_player[1] == "Papel":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Gana el jugador 2.")
            elif value_jugada_player[1] == "Tijeras":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Gana el jugador 1.")
        elif value_jugada_player[0] == "Papel":
            if value_jugada_player[1] == "Piedra":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Gana el jugador 1.")
            elif value_jugada_player[1] == "Papel":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Es un empate.")
            elif value_jugada_player[1] == "Tijeras":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Gana el jugador 2.")
        elif value_jugada_player[0] == "Tijeras":
            if value_jugada_player[1] == "Piedra":
                resultado = -1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Gana el jugador 2.")
            elif value_jugada_player[1] == "Papel":
                resultado = 1
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Gana el jugador 1.")
            elif value_jugada_player[1] == "Tijeras":
                resultado = 0
                messagebox.showinfo("",
                                    "El jugador 1 saca " + value_jugada_player[0] + ". El jugador 2 " +
                                    value_jugada_player[1] + ". Es un empate.")
        else:
            messagebox.showinfo("Error inesperado", "Cerrando la aplicación...")
            root.quit()

        root.attributes("-disabled",
                        False)  # Habilita de nuevo la ventana después de cerrar el messagebox correspondiente
        return resultado

    def añadir_puntos(res):
        if res > 0:  # Si gana el jugador 1
            puntos_player1.set(puntos_player1.get() + 1)
            puntuacion_jugador1.config(text="PUNTUACIÓN JUGADOR 1: " + str(puntos_player1.get()))
        elif res < 0:  # Si gana el jugador 2
            puntos_player2.set(puntos_player2.get() + 1)
            puntuacion_jugador2.config(text="PUNTUACIÓN JUGADOR 2: " + str(puntos_player2.get()))

        if puntos_player2.get() == 3 or puntos_player1.get() == 3:  # Si la partida se acaba, elige ganador
            if puntos_player2.get() == 3:
                root.attributes("-disabled", True)  # Deshabilita la ventana del juego para impedir bugs
                messagebox.showinfo("Partida terminada", "GANADOR: Jugador 2")
            else:
                messagebox.showinfo("Partida terminada", "GANADOR: Jugador 1")

            root.destroy()  # Cierra la partida, pero no la aplicación

    tk.Label(root).grid(row=0, column=0)  # Label decorativa para centrar el grid

    # Jugadas
    value_jugada_player = ["", ""]

    # Turno
    turno = tk.IntVar()
    turno.set(1)

    # Puntuación
    puntos_player1 = tk.IntVar()
    puntos_player1.set(0)
    puntos_player2 = tk.IntVar()
    puntos_player2.set(0)

    # Grid
    marcador_turno = tk.Label(root, text="TURNO: JUGADOR " + str(turno.get()))
    marcador_turno.grid(row=1, column=2, columnspan=3)
    puntuacion_jugador1 = tk.Label(root, text="PUNTUACIÓN JUGADOR 1: " + str(puntos_player1.get()))
    puntuacion_jugador1.grid(row=2, column=1, columnspan=2, pady=20)
    puntuacion_jugador2 = tk.Label(root, text="PUNTUACIÓN JUGADOR 2: " + str(puntos_player2.get()))
    puntuacion_jugador2.grid(row=2, column=4, columnspan=2, pady=20)
    piedra = tk.Button(root, text="PIEDRA", command=jugar_piedra)
    piedra.grid(row=3, column=1, padx=15)
    papel = tk.Button(root, text="PAPEL", command=jugar_papel)
    papel.grid(row=3, column=3, padx=15)
    tijeras = tk.Button(root, text="TIJERAS", command=jugar_tijeras)
    tijeras.grid(row=3, column=5, padx=15)

    tk.Label(root).grid(row=10, column=10)  # Label decorativa para centrar el grid

    # Configuración grid
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(10, weight=1)
    root.grid_columnconfigure(10, weight=1)
"""
