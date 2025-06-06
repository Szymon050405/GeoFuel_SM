import tkinter as tk
from tkinter import ttk, messagebox

class StationManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Zarządzania Siecią Stacji Benzynowych")
        self.root.geometry("1100x700")

        self.tab_control = ttk.Notebook(root)

        # Tworzenie zakładek
        self.station_tab = ttk.Frame(self.tab_control)
        self.employee_tab = ttk.Frame(self.tab_control)
        self.client_tab = ttk.Frame(self.tab_control)
        self.map_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.station_tab, text="Stacje")
        self.tab_control.add(self.employee_tab, text="Pracownicy")
        self.tab_control.add(self.client_tab, text="Klienci")
        self.tab_control.add(self.map_tab, text="Mapy")

        self.tab_control.pack(expand=1, fill="both")

        self.setup_station_tab()
        self.setup_employee_tab()
        self.setup_client_tab()
        self.setup_map_tab()

    # -------------------------------------
    # Zakładka: Stacje
    def setup_station_tab(self):
        label = tk.Label(self.station_tab, text="Stacje Benzynowe", font=("Arial", 14))
        label.pack(pady=10)

        columns = ("id", "nazwa", "adres", "koordynaty")
        self.station_tree = ttk.Treeview(self.station_tab, columns=columns, show="headings")
        for col in columns:
            self.station_tree.heading(col, text=col.capitalize())
            self.station_tree.column(col, width=150)
        self.station_tree.pack(expand=True, fill="both", padx=20, pady=10)

        self.station_tree.insert("", "end", values=(1, "Stacja A", "ul. Główna 1", "50.061, 19.938"))
        self.station_tree.insert("", "end", values=(2, "Stacja B", "ul. Krakowska 22", "50.067, 19.912"))

        form_frame = tk.Frame(self.station_tab)
        form_frame.pack(pady=10, fill="x", padx=20)

        # Pola tekstowe
        tk.Label(form_frame, text="ID").grid(row=0, column=0)
        self.station_id_entry = tk.Entry(form_frame, width=10)
        self.station_id_entry.grid(row=1, column=0, padx=5)

        tk.Label(form_frame, text="Nazwa").grid(row=0, column=1)
        self.station_name_entry = tk.Entry(form_frame)
        self.station_name_entry.grid(row=1, column=1, padx=5)

        tk.Label(form_frame, text="Adres").grid(row=0, column=2)
        self.station_address_entry = tk.Entry(form_frame, width=30)
        self.station_address_entry.grid(row=1, column=2, padx=5)

        tk.Label(form_frame, text="Koordynaty").grid(row=0, column=3)
        self.station_coord_entry = tk.Entry(form_frame)
        self.station_coord_entry.grid(row=1, column=3, padx=5)

        # Przyciski
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=1, column=4, padx=10)

        tk.Button(button_frame, text="Dodaj", command=self.add_station).pack(pady=2)
        tk.Button(button_frame, text="Załaduj", command=self.load_station).pack(pady=2)
        tk.Button(button_frame, text="Zapisz", command=self.save_station).pack(pady=2)
        tk.Button(button_frame, text="Usuń", command=self.delete_station).pack(pady=2)

    def add_station(self):
        values = (
            self.station_id_entry.get(),
            self.station_name_entry.get(),
            self.station_address_entry.get(),
            self.station_coord_entry.get()
        )
        if any(v == "" for v in values):
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
            return
        self.station_tree.insert("", "end", values=values)
        self.clear_station_fields()

    def load_station(self):
        selected = self.station_tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Zaznacz stację.")
            return
        values = self.station_tree.item(selected[0], "values")
        self.station_id_entry.delete(0, tk.END)
        self.station_name_entry.delete(0, tk.END)
        self.station_address_entry.delete(0, tk.END)
        self.station_coord_entry.delete(0, tk.END)
        self.station_id_entry.insert(0, values[0])
        self.station_name_entry.insert(0, values[1])
        self.station_address_entry.insert(0, values[2])
        self.station_coord_entry.insert(0, values[3])

    def save_station(self):
        selected = self.station_tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Zaznacz stację.")
            return
        new_values = (
            self.station_id_entry.get(),
            self.station_name_entry.get(),
            self.station_address_entry.get(),
            self.station_coord_entry.get()
        )
        self.station_tree.item(selected[0], values=new_values)
        self.clear_station_fields()

    def delete_station(self):
        selected = self.station_tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Zaznacz stację.")
            return
        if messagebox.askyesno("Potwierdzenie", "Usunąć zaznaczoną stację?"):
            self.station_tree.delete(selected[0])
            self.clear_station_fields()

    def clear_station_fields(self):
        self.station_id_entry.delete(0, tk.END)
        self.station_name_entry.delete(0, tk.END)
        self.station_address_entry.delete(0, tk.END)
        self.station_coord_entry.delete(0, tk.END)

    # -------------------------------------
    # Zakładka: Pracownicy
    def setup_employee_tab(self):
        label = tk.Label(self.employee_tab, text="Lista pracowników (do rozbudowy)", font=("Arial", 14))
        label.pack(pady=20)

    # -------------------------------------
    # Zakładka: Klienci
    def setup_client_tab(self):
        label = tk.Label(self.client_tab, text="Lista klientów (do rozbudowy)", font=("Arial", 14))
        label.pack(pady=20)

    # -------------------------------------
    # Zakładka: Mapy
    def setup_map_tab(self):
        label = tk.Label(self.map_tab, text="Tu będą mapy (do rozbudowy)", font=("Arial", 14))
        label.pack(pady=20)

# -------------------------------------
# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = StationManagerApp(root)
    root.mainloop()
