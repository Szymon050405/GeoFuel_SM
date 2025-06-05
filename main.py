from tkinter import *

root = Tk()
root.title("Zarządzanie stacjami")
root.geometry("800x200")

frame1 = Frame(root)
frame1.pack(pady=10)

Button(frame1, text="Stacje", width=15, command=lambda: print("Stacje")).pack(side=LEFT, padx=5)
Button(frame1, text="Pracownicy", width=15, command=lambda: print("Pracownicy")).pack(side=LEFT, padx=5)
Button(frame1, text="Klienci", width=15, command=lambda: print("Klienci")).pack(side=LEFT, padx=5)

frame2 = Frame(root)
frame2.pack(pady=10)

Button(frame2, text="Mapa: Stacje", width=15, command=lambda: print("Mapa stacji")).pack(side=LEFT, padx=5)
Button(frame2, text="Mapa: Pracownicy", width=15, command=lambda: print("Mapa pracowników")).pack(side=LEFT, padx=5)
Button(frame2, text="Mapa: Klienci", width=15, command=lambda: print("Mapa klientów")).pack(side=LEFT, padx=5)

root.mainloop()