import tkinter as tk

main = tk.Tk()
main.title("Piedra, papel, tijera")
main.geometry("200x100")


def jugar_piedra():
    pass


def jugar_papel():
    pass


def jugar_tijeras():
    pass


def nueva_partida_vs_ia():
    root = tk.Toplevel()
    root.title("Jugador vs IA")
    root.geometry("800x600")

    tk.Label(root).grid(row=0, column=0)

    puntuacion = tk.Label(root, text="PUNTUACIÓN: 0")
    puntuacion.grid(row=1, column=1, columnspan=3, pady=20)
    piedra = tk.Button(root, text="PIEDRA", command=jugar_piedra)
    piedra.grid(row=2, column=1, padx=15)
    papel = tk.Button(root, text="PAPEL", command=jugar_papel)
    papel.grid(row=2, column=2, padx=15)
    tijeras = tk.Button(root, text="TIJERAS", command=jugar_tijeras)
    tijeras.grid(row=2, column=3, padx=15)

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

main.mainloop()
