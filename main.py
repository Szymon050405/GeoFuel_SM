import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StationManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Zarządzania Stacjami Benzynowymi")
        self.root.geometry("900x600")

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

        # Przyciski akcji
        button_frame = tk.Frame(self.station_tab)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Dodaj stację", command=self.add_station)
        update_button = tk.Button(button_frame, text="Aktualizuj zaznaczoną", command=self.update_station)
        delete_button = tk.Button(button_frame, text="Usuń zaznaczoną", command=self.delete_station)

        add_button.grid(row=0, column=0, padx=10)
        update_button.grid(row=0, column=1, padx=10)
        delete_button.grid(row=0, column=2, padx=10)

    def add_station(self):
        print("Dodaj stację - tu będzie formularz")

    def update_station(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Wybierz stację do aktualizacji.")
            return
        values = self.tree.item(selected[0], "values")
        print("Aktualizuj:", values)
        # Tu można otworzyć formularz edycji z wartościami

    def delete_station(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Brak wyboru", "Wybierz stację do usunięcia.")
            return
        confirm = messagebox.askyesno("Potwierdź", "Czy na pewno chcesz usunąć zaznaczoną stację?")
        if confirm:
            self.tree.delete(selected[0])
            print("Usunięto stację.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StationManagerApp(root)
    root.mainloop()
