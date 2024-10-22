import tkinter as tk
from math import floor
from random import random
from tkinter import messagebox

main = tk.Tk()
main.title("Piedra, papel, tijera")
main.geometry("200x100")


def nueva_partida_vs_ia():
    root = tk.Toplevel()
    root.title("Jugador vs IA")
    root.geometry("800x600")

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
        jugada_IA = floor((random() * 100) % 3)
        if jugada_IA == 0:
            value_jugada_IA.set("Piedra")
        elif jugada_IA == 1:
            value_jugada_IA.set("Papel")
        elif jugada_IA == 2:
            value_jugada_IA.set("Tijeras")
        else:
            messagebox.showinfo("Número no encontrado", "Cerrando la aplicación...")
            root.destroy()

    def elegir_ganador():
        resultado = None
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

        return resultado

    def añadir_puntos(res):
        if res > 0:
            puntos_player.set(puntos_player.get() + 1)
            puntuacion_jugador1.config(text="PUNTUACIÓN JUGADOR: " + str(puntos_player.get()))
        elif res < 0:
            puntos_IA.set(puntos_IA.get() + 1)
            puntuacion_jugador2.config(text="PUNTUACIÓN IA: " + str(puntos_IA.get()))

        if puntos_IA.get() == 3 or puntos_player.get() == 3:
            if puntos_IA.get() == 3:
                messagebox.showinfo("Partida terminada", "GANADOR: IA")
            else:
                messagebox.showinfo("Partida terminada", "GANADOR: TÚ")

            root.destroy()  # Cierra la partida, pero no la aplicación

    tk.Label(root).grid(row=0, column=0)

    value_jugada_player = tk.StringVar()
    value_jugada_player.set(str(None))
    value_jugada_IA = tk.StringVar()
    value_jugada_IA.set(str(None))
    puntos_player = tk.IntVar()
    puntos_player.set(0)
    puntos_IA = tk.IntVar()
    puntos_IA.set(0)

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

    tk.Label(root).grid(row=10, column=10)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(10, weight=1)
    root.grid_columnconfigure(10, weight=1)


def nueva_partida_vs_jugador():
    root = tk.Toplevel()
    root.title("Jugador vs Jugador")
    root.geometry("800x600")


menu = tk.Menu(main)
main.config(menu=menu)

menu_partida = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Partida", menu=menu_partida)
menu_partida.add_command(label="Nueva Partida vs IA", command=nueva_partida_vs_ia)
menu_partida.add_command(label="Nueva partida vs Jugador", command=nueva_partida_vs_jugador)

# Mainloop
main.mainloop()
