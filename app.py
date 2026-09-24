import tkinter as tk
from tkinter import messagebox
from password_manager import generate_password
from storage import save_password_local, get_passwords

def handle_generation():
    try:
        pwd = generate_password(length=16)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, pwd)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def handle_save():
    site = entry_site.get().strip()
    pwd = entry_result.get().strip()
    
    if not site:
        messagebox.showwarning("Attention", "Veuillez entrer un nom de site ou de service !")
        return
    if not pwd:
        messagebox.showwarning("Attention", "Aucun mot de passe à sauvegarder !")
        return
        
    save_password_local(site, pwd)
    messagebox.showinfo("Succès", f"Mot de passe pour '{site}' sauvegardé et chiffré avec succès !")
    entry_site.delete(0, tk.END)

def show_vault():
    """Affiche les mots de passe enregistrés dans une nouvelle fenêtre."""
    passwords = get_passwords()
    
    vault_window = tk.Toplevel(root)
    vault_window.title("Mon Coffre-Fort")
    vault_window.geometry("350x300")
    
    tk.Label(vault_window, text="Mots de passe enregistrés :", font=("Arial", 12, "bold")).pack(pady=10)
    
    text_area = tk.Text(vault_window, font=("Arial", 10), width=40, height=12)
    text_area.pack(padx=10, pady=5)
    
    if not passwords:
        text_area.insert(tk.END, "Aucun mot de passe sauvegardé pour l'instant.")
    else:
        for site, pwd in passwords.items():
            text_area.insert(tk.END, f"• {site} : {pwd}\n")
            
    text_area.config(state=tk.DISABLED)

# --- Configuration de la fenêtre principale ---
root = tk.Tk()
root.title("SecurePass Vault - Beginner's Paradise")
root.geometry("400x420")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="Gestionnaire de Mots de Passe", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=15)

# Nom du site
tk.Label(root, text="Nom du site / service :", bg="#f0f0f0", font=("Arial", 10)).pack()
entry_site = tk.Entry(root, font=("Arial", 11), width=25)
entry_site.pack(pady=5)

# Champ pour le mot de passe
tk.Label(root, text="Mot de passe généré :", bg="#f0f0f0", font=("Arial", 10)).pack()
entry_result = tk.Entry(root, font=("Arial", 11), justify="center", width=25)
entry_result.pack(pady=5)

# Boutons d'action
btn_generate = tk.Button(root, text="Générer un mot de passe", font=("Arial", 10), bg="#4CAF50", fg="white", width=22, command=handle_generation)
btn_generate.pack(pady=8)

btn_save = tk.Button(root, text="Sauvegarder dans le coffre", font=("Arial", 10), bg="#FF9800", fg="white", width=22, command=handle_save)
btn_save.pack(pady=5)

btn_view = tk.Button(root, text="Voir mon coffre-fort", font=("Arial", 10), bg="#2196F3", fg="white", width=22, command=show_vault)
btn_view.pack(pady=5)

root.mainloop()