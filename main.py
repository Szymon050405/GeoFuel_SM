from tkinter import *

def zmien_tekst():
    etykieta.config(text="Kliknięto przycisk!")

root = Tk()
root.title("Moja aplikacja")
root.geometry("400x300")

etykieta = Label(root, text="Witaj w aplikacji!", font=("Arial", 14))
etykieta.pack(pady=20)

przycisk = Button(root, text="Kliknij mnie", command=zmien_tekst)
przycisk.pack()

root.mainloop()