from tkinter import *

root = Tk()
root.title("Zarządzanie stacjami")
root.geometry("800x250")
root.configure(bg="#f0f0f0")  # delikatne tło

# ---- Sekcja 1: Zarządzanie danymi ----
Label(root, text="Zarządzanie danymi", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=(10, 0))

frame1 = Frame(root, bg="#f0f0f0")
frame1.pack(pady=10)

Button(frame1, text="Stacje", width=20, height=2, font=("Arial", 11), command=lambda: print("Stacje")).pack(side=LEFT, padx=10)
Button(frame1, text="Pracownicy", width=20, height=2, font=("Arial", 11), command=lambda: print("Pracownicy")).pack(side=LEFT, padx=10)
Button(frame1, text="Klienci", width=20, height=2, font=("Arial", 11), command=lambda: print("Klienci")).pack(side=LEFT, padx=10)

# ---- Sekcja 2: Generowanie map ----
Label(root, text="Generowanie map", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=(15, 0))

frame2 = Frame(root, bg="#f0f0f0")
frame2.pack(pady=10)

Button(frame2, text="Mapa: Stacje", width=20, height=2, font=("Arial", 11), command=lambda: print("Mapa stacji")).pack(side=LEFT, padx=10)
Button(frame2, text="Mapa: Pracownicy", width=20, height=2, font=("Arial", 11), command=lambda: print("Mapa pracowników")).pack(side=LEFT, padx=10)
Button(frame2, text="Mapa: Klienci", width=20, height=2, font=("Arial", 11), command=lambda: print("Mapa klientów")).pack(side=LEFT, padx=10)

root.mainloop()