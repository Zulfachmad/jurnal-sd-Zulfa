import os
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

# Mengambil DB_PASSWORD dari environment variable
db_password = os.getenv("DB_PASSWORD")

def connect_database():
    if db_password:
        return f"Koneksi sukses menggunakan password: {db_password}"
    else:
        return "Koneksi gagal, password tidak ditemukan!"