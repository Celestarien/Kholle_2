import tkinter
from tkinter import *
import subprocess
import os


app = tkinter.Tk()
app.geometry("640x480")
app.title("Ping & Pong")

def game():
    os.system("python test.py")



#Menu
mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Jouer", command=game)
first_menu.add_separator()
first_menu.add_command(label="Quitter", command=app.quit)

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="Giovannangeli Julien")

mainmenu.add_cascade(label="Menu Principal", menu=first_menu)
mainmenu.add_cascade(label="Crédits", menu=second_menu)


app.wm_resizable(0,0)
app.config(menu=mainmenu)
app.mainloop()


