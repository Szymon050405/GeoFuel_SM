from tkinter import *

def zmien_tekst():
    etykieta.config(text="Kliknięto przycisk 1!")

def pokaz_powitanie():
    etykieta.config(text="Witaj ponownie!")

def wyczysc_tekst():
    etykieta.config(text="")

root = Tk()
root.title("Moja aplikacja")
root.geometry("400x300")

etykieta = Label(root, text="Witaj w aplikacji!", font=("Arial", 14))
etykieta.pack(pady=20)

przycisk1 = Button(root, text="Przycisk 1", command=zmien_tekst)
przycisk1.pack(pady=5)

przycisk2 = Button(root, text="Pokaż powitanie", command=pokaz_powitanie)
przycisk2.pack(pady=5)

przycisk3 = Button(root, text="Wyczyść tekst", command=wyczysc_tekst)
przycisk3.pack(pady=5)

root.mainloop()