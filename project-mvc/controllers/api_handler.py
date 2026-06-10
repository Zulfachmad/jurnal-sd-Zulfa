import random

# Simulasikan data dari database
users = [{"id": 1, "name": "Admin"}, {"id": 2, "name": "User"}]

def get_users():
    # Simulasi server sibuk secara acak (angka 0 atau 1)
    if random.choice([0, 1]) == 0:
        return {"status": "error", "message": "Server sedang sibuk, silakan coba lagi!"}
    
    return {"status": "success", "data": users}