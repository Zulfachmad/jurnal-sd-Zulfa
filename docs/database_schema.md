\# Database Schema



\## Tabel users



| Kolom       | Tipe Data      | Keterangan                     |

|-------------|----------------|--------------------------------|

| id          | INT (PK)       | Auto increment                 |

| username    | VARCHAR(100)   | Nama pengguna, unik            |

| email       | VARCHAR(255)   | Email, unik                    |

| password    | VARCHAR(255)   | Hash password                  |

| avatar\_url  | TEXT           | URL foto profil                |

| created\_at  | TIMESTAMP      | Waktu registrasi               |

| updated\_at  | TIMESTAMP      | Waktu update profil            |



\## Tabel sessions (opsional)



| Kolom       | Tipe Data      | Keterangan                     |

|-------------|----------------|--------------------------------|

| id          | INT (PK)       | Auto increment                 |

| user\_id     | INT (FK)       | Referensi ke users.id          |

| token       | VARCHAR(255)   | Token login                    |

| expires\_at  | TIMESTAMP      | Waktu kadaluarsa token         |

