import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Progressbar
from click import launch
from sympy import im
import wget
from tkinter import *
from tkinter import messagebox as mb
import requests
import webbrowser


class App:
    def launchScrap(self):
        print("ok")

    def __init__(self, window):
        self.window = window
        self.window.title("Compteur de mot de passe ")
        self.window.geometry("1080x720")
        self.window.minsize(720, 360)
        self.window.config(background='#2C2323')
        # frame
        frame = Frame(self.window, bg='#2C2323')

        # image
        width = 300
        height = 300
        image = PhotoImage(file='images.png').zoom(7).subsample(32)
        canvas = Canvas(frame, width=width, height=height,
                        bg='#60108E', bd=0, highlightthickness=0)
        canvas.create_image(width / 2, height / 2, image=image)
        canvas.grid(row=0, column=0, sticky=W)

        frame2 = Frame(frame, bg='#2C2323')
        frame3 = Frame(frame, bg='#2C2323')
        # titre
        label = Label(frame2, text=" Se loger",
                      font="Bahnschrift, 20", bg='#2C2323', fg='white')
        label.pack()

        # champ ou le nombre sera entrez
        entry2 = Entry(frame3, font="Bahnschrift, 20",
                       bg='#2C2323', fg='white', bd=0, highlightthickness=0)
        entry2.pack()

        # bouton
        button = Button(frame2, text=" Générer le fichier excel", font="Bahnschrift, 20",
                        bg='#2C2323', fg='white', command=self.launchScraping)
        button.pack(fill=X)

        # self.label2 = Label(frame2, text="",
        #                font="Bahnschrift, 20", bg='#2C2323', fg='white')
        # self.label2.pack()
        # afficher la frame
        frame2.grid(row=0, column=1, sticky=W)
        frame3.grid(row=0, column=1, sticky=N)
        frame.pack(expand=YES)

        # menu
        # menu = Menu(self.window)
        # menu_bar = Menu(menu, tearoff=0, bg='white')
        # menu_bar.add_command(label="Quitter", command=self.window.quit)
        # menu_bar.add_command(label="Générer", command=self.launchScrap)

        # menu.add_cascade(label="Fichier", menu=menu_bar, font='blue')
        # self.window.config(menu=menu)

        self.window.mainloop()

    def launchScraping(self):
        requests.get(
            "https://maker.ifttt.com/trigger/notif/with/key/R0mt4AISyN9Zw__1RuU9M?value1=Starting&&value2=Seloger")
        mb.showinfo('Ok', 'Un navigateur va être ouvert afin de générer le fichier excel des 150 derniers jours.\nVeuillez ne pas fermer la fenêtre du programme ainsi que celle du navigateur.')
        url = "https://gitlab.com/danhab05/selogercode/-/raw/master/prog.py"
        try:
            os.remove("prog.py")
        except FileNotFoundError:
            pass
        wget.download(url, 'prog.py')
        print("Donwloaded")
        try:
            exec(open('prog.py', encoding="utf-8").read())
            self.window.destroy()
            # mb.showinfo('Ok', 'Le fichier excel a bien été generé')
            webbrowser.open(
                "https://docs.google.com/spreadsheets/d/1i4Y2RkLIUK2caK-v4MDCyRM0RdxrHf7EGJSUq9tU5xs/edit?usp=sharing")
            return "okd"
        except Exception:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
