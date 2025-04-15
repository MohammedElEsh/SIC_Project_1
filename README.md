# 💰 SIC Bank Management System

A **simple and powerful banking system** built with **Python**, developed during the **Samsung Innovation Campus (SIC)** course.  
It supports user registration, login, deposits, withdrawals, transfers, multi-currency support, and admin access to transaction logs.

> 🛠️ Also packaged as an `.exe` file using **PyInstaller**, making it easy to run on any Windows machine without Python.

---

## 🧾 Features

- 👤 User Registration & Login system
- 💸 Deposit and Withdraw funds (Supports: EGP 🇪🇬, USD 💵, SAR 🇸🇦)
- 🔁 Transfer funds between users
- 📄 View and edit account details
- 🧾 Transaction log saved in `transactions_log.json`
- 🔐 Admin Panel to monitor all activities
- 🧠 Smart validation for inputs (name, password, phone, etc.)
- 💾 Data stored in a JSON database (`Project_1_json.json`)
- 🪄 `.exe` version included for easy access

---

## 🧱 Project Structure

```
SIC_Project_1/
├── Project_1.py                 # Main Python source code
├── Project_1_json.json          # Database file storing users
├── transactions_log.json        # Logs all transactions (deposits, withdrawals, transfers)
├── Project_1.spec               # PyInstaller configuration file
├── dist/
│   ├── Project_1.exe            # Standalone executable file
└── README.md                    # You're reading it
```

---


## 🚀 How to Run

### ▶️ Option 1: Run with Python

Make sure Python is installed on your system (Python 3.10+ recommended):

```bash
git clone https://github.com/MohammedElEsh/SIC_Project_1.git
cd SIC_Project_1
python Project_1.py
```

> ✅ Make sure `Project_1_json.json` exists in the same folder before starting.

---

### 🖥️ Option 2: Run `.exe` (No Python needed)

1. Go to the `dist/` folder.
2. Ensure the `.exe` file and the JSON database (`Project_1_json.json`) are together.
3. Double-click `Project_1.exe` and enjoy!

---

## 💱 Supported Currencies

- **EGP** → Egyptian Pound (Default)
- **USD** → US Dollar
- **SAR** → Saudi Riyal

Exchange Rates used:

| Currency | Rate (to EGP) |
|----------|---------------|
| USD      | 30            |
| SAR      | 9             |
| EGP      | 1             |

---

## 📦 Technologies Used

- `Python 3.12`
- `JSON` for database
- `PyInstaller` for building `.exe`
- `OOP` concepts for clean code architecture
- CLI interface for interactivity

---

## 📸 Screenshots

> *(Add a screenshot if you'd like by placing an image in the repo and using)*  
```markdown
![Screenshot](images/demo.png)
```

---

## 👨‍💻 Author

**Mohammed El Esh**  
🎓 Samsung Innovation Campus Graduate  
🔗 [GitHub](https://github.com/MohammedElEsh)

---

## 📄 License

This project is licensed under the MIT License – feel free to use, modify, and share it!

---

## ❤️ Special Thanks

Thanks to the **Samsung Innovation Campus (SIC)** team for the training and support throughout this project.
