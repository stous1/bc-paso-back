import secrets

secure_random = secrets.token_hex(32)  # Genera una cadena hexadecimal de 64 caracteres (32 bytes)
print(secure_random)