# API Contract - User Profile

**Endpoint:** `/api/v1/profile`  
**Method:** GET  
**Response Body (JSON):**
```json
{
  "id": 1,
  "username": "mahasiswa_sd",
  "email": "mhs@univ.ac.id",
  "avatar_url": "https://image.com/avatar.png"
}
```

---

# API Contract - Login

**Endpoint:** `/api/v1/login`  
**Method:** POST  

**Request Body (JSON):**
```json
{
  "email": "mhs@univ.ac.id",
  "password": "rahasia123"
}
```

**Response Body (JSON) - Success:**
```json
{
  "success": true,
  "token": "jwt_token_here",
  "user": {
    "id": 1,
    "username": "mahasiswa_sd",
    "email": "mhs@univ.ac.id"
  }
}
```

**Response Body (JSON) - Failed:**
```json
{
  "success": false,
  "message": "Email atau password salah"
}
```