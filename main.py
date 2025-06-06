import tkinter as tk
from tkinter import ttk, messagebox

class StationManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Zarządzania Siecią Stacji Benzynowych")
        self.root.geometry("1100x700")

        self.tab_control = ttk.Notebook(root)

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

    # ---------------- Zakładka STACJE ----------------
    def setup_station_tab(self):
        label = tk.Label(self.station_tab, text="Stacje Benzynowe", font=("Arial", 14))
        label.pack(pady=10)

        columns = ("id", "nazwa", "adres", "koordynaty")
        self.station_tree = ttk.Treeview(self.station_tab, columns=columns, show="headings")
        for col in columns:
            self.station_tree.heading(col, text=col.capitalize())
            self.station_tree.column(col, width=150)
        self.station_tree.pack(expand=True, fill="both", padx=20, pady=10)

        form_frame = self.create_form_frame(self.station_tab, columns)
        self.station_entries = form_frame['entries']
        self.create_crud_buttons(form_frame['frame'], self.station_entries, self.station_tree)

    # ---------------- Zakładka PRACOWNICY ----------------
    def setup_employee_tab(self):
        label = tk.Label(self.employee_tab, text="Pracownicy", font=("Arial", 14))
        label.pack(pady=10)

        columns = ("id", "imię", "nazwisko", "stacja", "koordynaty")
        self.employee_tree = ttk.Treeview(self.employee_tab, columns=columns, show="headings")
        for col in columns:
            self.employee_tree.heading(col, text=col.capitalize())
            self.employee_tree.column(col, width=150)
        self.employee_tree.pack(expand=True, fill="both", padx=20, pady=10)

        form_frame = self.create_form_frame(self.employee_tab, columns)
        self.employee_entries = form_frame['entries']
        self.create_crud_buttons(form_frame['frame'], self.employee_entries, self.employee_tree)

    # ---------------- Zakładka KLIENCI ----------------
    def setup_client_tab(self):
        label = tk.Label(self.client_tab, text="Klienci", font=("Arial", 14))
        label.pack(pady=10)

        columns = ("id", "imię", "nazwisko", "adres", "koordynaty")
        self.client_tree = ttk.Treeview(self.client_tab, columns=columns, show="headings")
        for col in columns:
            self.client_tree.heading(col, text=col.capitalize())
            self.client_tree.column(col, width=150)
        self.client_tree.pack(expand=True, fill="both", padx=20, pady=10)

        form_frame = self.create_form_frame(self.client_tab, columns)
        self.client_entries = form_frame['entries']
        self.create_crud_buttons(form_frame['frame'], self.client_entries, self.client_tree)

    # ---------------- Zakładka MAPY ----------------
    def setup_map_tab(self):
        label = tk.Label(self.map_tab, text="Tu będą mapy (do rozbudowy)", font=("Arial", 14))
        label.pack(pady=20)

    # ---------------- Pomocnicze ----------------
    def create_form_frame(self, parent, fields):
        frame = tk.Frame(parent)
        frame.pack(pady=10, fill="x", padx=20)
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(frame, text=field.capitalize()).grid(row=0, column=i)
            entry = tk.Entry(frame, width=15)
            entry.grid(row=1, column=i, padx=5)
            entries[field] = entry

        return {"frame": frame, "entries": entries}

    def create_crud_buttons(self, parent_frame, entries_dict, tree_widget):
        button_frame = tk.Frame(parent_frame)
        button_frame.grid(row=1, column=len(entries_dict), padx=10)

        def clear_entries():
            for entry in entries_dict.values():
                entry.delete(0, tk.END)

        def add_item():
            values = tuple(entry.get() for entry in entries_dict.values())
            try:
                if not entries_dict['id'].get().isdigit():
                    raise ValueError
                if 'imię' in entries_dict and not entries_dict['imię'].get().isalpha():
                    raise ValueError
                if 'nazwisko' in entries_dict and not entries_dict['nazwisko'].get().isalpha():
                    raise ValueError
                if 'koordynaty' in entries_dict:
                    float(entries_dict['koordynaty'].get().replace(',', '.'))
            except:
                messagebox.showerror("Błąd", "Popraw dane")
                return

            if any(v == "" for v in values):
                messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
                return
            tree_widget.insert("", "end", values=values)
            clear_entries()

        def load_item():
            selected = tree_widget.selection()
            if not selected:
                messagebox.showwarning("Brak wyboru", "Zaznacz rekord.")
                return
            values = tree_widget.item(selected[0], "values")
            for (key, entry), value in zip(entries_dict.items(), values):
                entry.delete(0, tk.END)
                entry.insert(0, value)

        def save_item():
            selected = tree_widget.selection()
            if not selected:
                messagebox.showwarning("Brak wyboru", "Zaznacz rekord.")
                return
            new_values = tuple(entry.get() for entry in entries_dict.values())
            tree_widget.item(selected[0], values=new_values)
            clear_entries()

        def delete_item():
            selected = tree_widget.selection()
            if not selected:
                messagebox.showwarning("Brak wyboru", "Zaznacz rekord.")
                return
            if messagebox.askyesno("Potwierdź", "Usunąć zaznaczony rekord?"):
                tree_widget.delete(selected[0])
                clear_entries()

        tk.Button(button_frame, text="Dodaj", command=add_item).pack(pady=2)
        tk.Button(button_frame, text="Załaduj", command=load_item).pack(pady=2)
        tk.Button(button_frame, text="Zapisz", command=save_item).pack(pady=2)
        tk.Button(button_frame, text="Usuń", command=delete_item).pack(pady=2)

# ---------------- RUN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = StationManagerApp(root)
    root.mainloop()