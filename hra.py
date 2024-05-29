import tkinter
import random

w = tkinter.Tk()
p = tkinter.Canvas(width=600, height=400)
p.pack()

hybstvorec = True

# Štvorec
square_size = 25
x = None
y = None

def move_square():
    global x, y

    # Vymazať starý štvorec
    p.delete("square")

    # Posunúť na nové miesto
    x = random.randint(0, 600 - square_size)
    y = random.randint(0, 400 - square_size)
    p.create_rectangle(x, y, x + square_size, y + square_size, fill="blue", tags="square")


def casovac():
    if hybstvorec:
        move_square()
    p.after(1500, casovac)


def klik(mys):
    global hybstvorec, x, y

    if x <= mys.x <= x + square_size and y <= mys.y <= y + square_size:
        hybstvorec = False
        p.delete("square")
        p.create_rectangle(x, y, x + square_size, y + square_size, fill="green", tags="square")
        vysledok.config(text="Zásah!")
    else:
        vysledok.config(text="Skús znova")

def novahra(mys):
    global hybstvorec
    p.delete("square")
    hybstvorec = True


# Pridanie popisku pre výsledok
vysledok = tkinter.Label(w, text="")
vysledok.pack()

# Pripojenie udalosti kliknutia myšou
p.bind("<Button-1>", klik)
p.bind("<Button-3>", novahra)

# Spustenie časovača
casovac()

w.mainloop()



