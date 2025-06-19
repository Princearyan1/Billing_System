# 🧾 Prince Billing Software

**Prince Billing Software** is a full-featured desktop billing application developed using Python and Tkinter. It simulates a point-of-sale system for a small retail store and includes features for billing, tax calculations, item price management, bill saving, and search functionality.

## ✨ Features

- 🎯 Graphical User Interface using **Tkinter**
- 👤 Customer detail entry with bill number auto-generation
- 🛒 Three product categories:
  - Medical Items
  - Grocery Items
  - Cold Drinks
- ➕ Add custom items with dynamic price input
- 💵 Calculates total price with applicable taxes:
  - 5% tax on Medical and Grocery
  - 10% tax on Cold Drinks
- 🧾 Bill generation and display in text area
- 💾 Save generated bills as `.txt` files
- 🔍 Search saved bills by bill number
- 🛠️ Manage and update item prices through GUI
- 🌓 Dark-themed modern interface with color customization

- Billing_System/
│
├── bills/ # Saved bills stored as text files
├── item_prices.json # Stores item prices persistently
├── billing_app.py # Main application script
└── README.md # Project documentation

markdown
Copy
Edit

## 🛠 Requirements

- Python 3.x
- Standard libraries only (`tkinter`, `os`, `json`, `random`)

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Princearyan1/Billing_System.git
   cd Billing_System
Run the application

bash
Copy
Edit
python billing_app.py
Make sure Python is installed and added to your system’s PATH.


🔧 Customization
Add Items: Click on + Add Item in any category frame.

Update Prices: Click Manage Prices → Choose a category → Update or remove items.

Saved Bills: Found in the bills/ directory as .txt files.

screenshots
![first](https://github.com/user-attachments/assets/b79b9ab9-884e-4791-93bb-d4b7de15581a)
![Screenshot 2025-06-20 000605](https://github.com/user-attachments/assets/d63e2747-8e48-4c0e-a7e9-0678f3e666a9)

![Screenshot 2025-06-20 000855](https://github.com/user-attachments/assets/73164237-732b-4ece-a54e-04360aa56c07)

![Screenshot 2025-06-20 000919](https://github.com/user-attachments/assets/ebfdab5d-2ea7-4489-9a42-279c97ffe2b9)

![Screenshot 2025-06-20 000939](https://github.com/user-attachments/assets/66520275-da26-4704-b3b4-af8d6be3fc30)




👨‍💻 Developed By
Prince Aryan
📧 princearyan9934@gmail.com
🔗 GitHub | LinkedIn


