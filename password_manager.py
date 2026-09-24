import secrets
import string

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Génère un mot de passe sécurisé selon les critères choisis."""
    alphabet = ""
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation
        
    if not alphabet:
        raise ValueError("Au moins un type de caractère doit être sélectionné.")
        
    # Utilisation du module secrets (recommandé pour la sécurité)
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password