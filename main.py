
import tkinter as tk
from tkinter import ttk, messagebox
import tkintermapview

class StationManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Zarządzania Siecią Stacji Benzynowych")
        self.root.geometry("1100x700")

        self.markers = []

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

    def setup_map_tab(self):
        label = tk.Label(self.map_tab, text="Mapa obiektów (tkintermapview)", font=("Arial", 14))
        label.pack(pady=10)

        self.map_widget = tkintermapview.TkinterMapView(self.map_tab, width=1000, height=600)
        self.map_widget.pack(fill="both", expand=True, padx=20, pady=20)

        self.map_widget.set_position(52.23, 21.00)
        self.map_widget.set_zoom(6)

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
                    coord_value = entries_dict['koordynaty'].get().replace(',', '.')
                    lat_lon = coord_value.strip().split()
                    if len(lat_lon) != 2:
                        raise ValueError
                    lat, lon = float(lat_lon[0]), float(lat_lon[1])
                    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                        raise ValueError
            except:
                messagebox.showerror("Błąd", "Popraw dane")
                return

            if any(v == "" for v in values):
                messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
                return

            tree_widget.insert("", "end", values=values)
            clear_entries()

            # Dodaj marker do mapy
            if hasattr(self, 'map_widget') and 'koordynaty' in entries_dict:
                try:
                    coord_value = entries_dict['koordynaty'].get().replace(',', '.')
                    lat_lon = coord_value.strip().split()
                    if len(lat_lon) == 2:
                        lat, lon = float(lat_lon[0]), float(lat_lon[1])
                        label_entry = entries_dict.get('nazwa') or entries_dict.get('imię')
                        text = label_entry.get() if label_entry else "Obiekt"
                        marker = self.map_widget.set_marker(lat, lon, text=text)
                        self.map_widget.set_position(lat, lon)
                        self.markers.append(marker)
                except Exception as e:
                    print("Błąd ustawiania znacznika:", e)

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

        hint = tk.Label(self.root, text="Koordynaty: np. 50.061 19.938 – szer. dł.", font=("Arial", 8), fg="gray")
        hint.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)


if __name__ == "__main__":
    root = tk.Tk()
    app = StationManagerApp(root)
    root.mainloop()
