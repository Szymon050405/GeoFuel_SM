import tkinter as tk
from tkinter import ttk

class StationManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Zarządzania Stacjami Benzynowymi")
        self.root.geometry("800x600")

        self.tab_control = ttk.Notebook(self.root)

        # Puste zakładki
        self.station_tab = ttk.Frame(self.tab_control)
        self.employee_tab = ttk.Frame(self.tab_control)
        self.client_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.station_tab, text="Stacje")
        self.tab_control.add(self.employee_tab, text="Pracownicy")
        self.tab_control.add(self.client_tab, text="Klienci")

        self.tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = StationManagerApp(root)
    root.mainloop()