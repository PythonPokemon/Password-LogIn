import tkinter as tk
from tkinter import messagebox
import json
import os

# Überprüfen, ob die Benutzerdatenbank-Datei existiert, andernfalls erstellen wir eine leere Datenbank
if not os.path.exists("user_database.json"):
    with open("user_database.json", "w") as file:
        json.dump({}, file)

# Funktion zum Laden der Benutzerdatenbank aus der JSON-Datei
def load_user_database():
    with open("user_database.json", "r") as file:
        return json.load(file)

# Funktion zum Speichern der Benutzerdatenbank in der JSON-Datei
def save_user_database(database):
    with open("user_database.json", "w") as file:
        json.dump(database, file)

# Benutzer und Passwörter (in einer realen Anwendung sollten Passwörter verschlüsselt gespeichert werden)
users = load_user_database()

def register():
    username = register_username_entry.get()
    password = register_password_entry.get()

    if username and password:
        if username not in users:
            users[username] = password
            save_user_database(users)  # Benutzer in die Datenbank speichern
            messagebox.showinfo("Erfolgreich", "Registrierung erfolgreich!")
        else:
            messagebox.showerror("Fehler", "Benutzername bereits vergeben.")
    else:
        messagebox.showerror("Fehler", "Bitte Benutzernamen und Passwort eingeben.")

def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if username in users and password == users[username]:
        messagebox.showinfo("Erfolgreich", "Login erfolgreich!")
        open_test_window()
    else:
        messagebox.showerror("Fehler", "Ungültiger Benutzername oder Passwort")

def open_test_window():
    test_window = tk.Toplevel(root)
    test_window.title("Test")
    
    # Inhalte des Testfensters (Beispiel)
    label = tk.Label(test_window, text="Willkommen zum Testfenster!")
    label.pack()

# GUI erstellen
root = tk.Tk()
root.title("Registrierung und Login")

# Registrierungsfenster
register_label = tk.Label(root, text="Benutzername:")
register_label.pack()
register_username_entry = tk.Entry(root)
register_username_entry.pack()

register_label = tk.Label(root, text="Passwort:")
register_label.pack()
register_password_entry = tk.Entry(root, show="*")
register_password_entry.pack()

register_button = tk.Button(root, text="Registrieren", command=register)
register_button.pack()

# Einloggen-Fenster
login_label = tk.Label(root, text="Benutzername:")
login_label.pack()
login_username_entry = tk.Entry(root)
login_username_entry.pack()

login_label = tk.Label(root, text="Passwort:")
login_label.pack()
login_password_entry = tk.Entry(root, show="*")
login_password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# GUI starten
root.mainloop()
