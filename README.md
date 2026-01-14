# 🔐 Password Generator & Encryptor (Python)

A graphical **Password Generator and Encryptor** built with Python and Tkinter.  
This application allows users to generate passwords of varying strength and length, then encrypt them using a simple date-based cipher.

---

## ✨ Features

### Password Generator
- Choose password length: **4, 6, 8, 10, or 12**
- Select strength:
  - **Weak** – lowercase letters
  - **Intermediate** – mixed case letters
  - **Strong** – letters, numbers, and symbols
- One-click **copy to clipboard**
- Visual feedback when copying

### Password Encryptor
- Encrypts any password using a **dynamic encryption key**
- Encryption key is based on the **current day and month**
- Copy encrypted passwords instantly
- Simple character-shifting cipher

---

## 🛠 Technologies Used

- **Python 3** (required)
- **Tkinter** (built-in GUI)
- **ttkthemes** (UI theming)
- **random** (built-in, password generation)
- **datetime** (built-in, encryption key generation)

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Install the external dependency:
   ```bash
   pip install ttkthemes
Ensure dice.png is in the same directory as the script

Run the program:

bash
Copy code
python password_generator.py
📂 Required Files
password_generator.py

dice.png

⚠️ Notes
This project is intended for educational purposes

The encryption method is not cryptographically secure

Generated passwords are suitable for learning/demo use, not sensitive data

👤 Author
AlexIsNotInset
