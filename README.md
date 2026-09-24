# 🔐 SecurePass Vault

**SecurePass Vault** is a lightweight, local, and secure password manager built with Python and a Tkinter graphical user interface. It is designed to safely store and manage credentials locally without relying on complex third-party services.

---

## 🚀 Key Features

- **Robust Encryption:** Uses the `cryptography` library (Fernet symmetric encryption) to ensure that stored passwords remain fully encrypted locally.
- **Intuitive GUI:** A clean and user-friendly desktop interface built with `Tkinter` for easy credential management.
- **Secure Local Storage:** Credentials are saved locally in an encrypted JSON format (`vault.json`), paired with automated key management (`secret.key`).

---

## 🛠️ Built With

- **Language:** Python 3.8+
- **Graphical Interface:** Tkinter (Python standard library)
- **Security & Encryption:** `cryptography` (Fernet)
- **Data Handling:** `json`, `os`

---

## 📦 Installation & Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FalconX-hub/securepass-vault.git
   cd securepass-vault



Install the required dependencies:

    Bash
        pip install cryptography


Run the application:

    Bash
        python app.py