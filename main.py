import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StationManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Zarządzania Stacjami Benzynowymi")
        self.root.geometry("1000x600")

        self.tab_control = ttk.Notebook(self.root)
        self.station_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.station_tab, text="Stacje")
        self.tab_control.pack(expand=1, fill="both")

        self.setup_station_tab()

    def setup_station_tab(self):
        label = tk.Label(self.station_tab, text="Lista stacji benzynowych", font=("Arial", 14))
        label.pack(pady=10)

        columns = ("id", "nazwa", "adres", "koordynaty")
        self.tree = ttk.Treeview(self.station_tab, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=150)
        self.tree.pack(expand=True, fill="both", padx=20, pady=10)

        # Przykładowe dane
        self.tree.insert("", "end", values=(1, "Stacja A", "ul. Główna 1", "50.061, 19.938"))
        self.tree.insert("", "end", values=(2, "Stacja B", "ul. Krakowska 22", "50.067, 19.912"))

        # Ramka na formularz i przyciski
        action_frame = tk.Frame(self.station_tab)
        action_frame.pack(pady=10, fill="x", padx=20)

        # Pola tekstowe
        tk.Label(action_frame, text="ID").grid(row=0, column=0)
        self.id_entry = tk.Entry(action_frame, width=10)
        self.id_entry.grid(row=1, column=0, padx=5)

        tk.Label(action_frame, text="Nazwa").grid(row=0, column=1)
        self.name_entry = tk.Entry(action_frame)
        self.name_entry.grid(row=1, column=1, padx=5)

        tk.Label(action_frame, text="Adres").grid(row=0, column=2)
        self.address_entry = tk.Entry(action_frame, width=30)
        self.address_entry.grid(row=1, column=2, padx=5)

        tk.Label(action_frame, text="Koordynaty").grid(row=0, column=3)
        self.coord_entry = tk.Entry(action_frame)
        self.coord_entry.grid(row=1, column=3, padx=5)

        # Przyciski
        button_frame = tk.Frame(action_frame)
        button_frame.grid(row=1, column=4, padx=10)

        tk.Button(button_frame, text="Dodaj", command=self.add_station).pack(side="top", pady=2)
        tk.Button(button_frame, text="Załaduj do edycji", command=self.load_for_edit).pack(side="top", pady=2)
        tk.Button(button_frame, text="Zapisz zmiany", command=self.save_changes).pack(side="top", pady=2)
        tk.Button(button_frame, text="Usuń", command=self.delete_station).pack(side="top", pady=2)

    def add_station(self):
        values = (
            self.id_entry.get(),
            self.name_entry.get(),
            self.address_entry.get(),
            self.coord_entry.get()
        )
        if any(v == "" for v in values):
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
            return
        self.tree.insert("", "end", values=values)
        self.clear_inputs()

    def load_for_edit(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Zaznacz stację do edycji.")
            return
        values = self.tree.item(selected[0], "values")
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.coord_entry.delete(0, tk.END)

        self.id_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.address_entry.insert(0, values[2])
        self.coord_entry.insert(0, values[3])

    def save_changes(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Zaznacz stację do edycji.")
            return
        new_values = (
            self.id_entry.get(),
            self.name_entry.get(),
            self.address_entry.get(),
            self.coord_entry.get()
        )
        if any(v == "" for v in new_values):
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
            return
        self.tree.item(selected[0], values=new_values)
        self.clear_inputs()

    def delete_station(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Zaznacz stację do usunięcia.")
            return
        confirm = messagebox.askyesno("Potwierdzenie", "Czy na pewno usunąć zaznaczoną stację?")
        if confirm:
            self.tree.delete(selected[0])
            self.clear_inputs()

    def clear_inputs(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.coord_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StationManagerApp(root)
    root.mainloop()
