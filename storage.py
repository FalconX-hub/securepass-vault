import json
import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
DATA_FILE = "vault.json"

def load_or_create_key():
    """Charge la clé de chiffrement ou en génère une nouvelle si elle n'existe pas."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

def save_password_local(site_name, password):
    """Chiffre et sauvegarde un mot de passe associé à un nom de site."""
    key = load_or_create_key()
    fernet = Fernet(key)
    
    # Charger les données existantes
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
                
    # Chiffrer le mot de passe
    encrypted_pwd = fernet.encrypt(password.encode()).decode()
    data[site_name] = encrypted_pwd
    
    # Sauvegarder dans le fichier JSON
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_passwords():
    """Récupère et déchiffre tous les mots de passe enregistrés."""
    key = load_or_create_key()
    fernet = Fernet(key)
    
    if not os.path.exists(DATA_FILE):
        return {}
        
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return {}
            
    decrypted_data = {}
    for site, enc_pwd in data.items():
        try:
            decrypted_data[site] = fernet.decrypt(enc_pwd.encode()).decode()
        except Exception:
            decrypted_data[site] = "[Erreur de déchiffrement]"
            
    return decrypted_data