# etap2_stacje.py

import tkinter as tk
from tkinter import ttk

class StationManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Zarządzania Stacjami Benzynowymi")
        self.root.geometry("800x600")

        self.tab_control = ttk.Notebook(self.root)
        self.station_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.station_tab, text="Stacje")
        self.tab_control.pack(expand=1, fill="both")

        self.setup_station_tab()

    def setup_station_tab(self):
        label = tk.Label(self.station_tab, text="Lista stacji benzynowych", font=("Arial", 14))
        label.pack(pady=10)

        add_button = tk.Button(self.station_tab, text="Dodaj stację", command=self.add_station)
        add_button.pack()

    def add_station(self):
        print("Dodaj stację - przyszła logika")

if __name__ == "__main__":
    root = tk.Tk()
    app = StationManagerApp(root)
    root.mainloop()
