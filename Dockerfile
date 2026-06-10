FROM python:3.9-slim

WORKDIR /app

# Menentukan nilai default untuk variabel lingkungan
ENV APP_USER="Developer Mahasiswa"
ENV APP_ENV="development"

# Salin semua file dari folder project-mvc ke dalam kontainer
COPY project-mvc/ .

CMD ["python", "app.py"]