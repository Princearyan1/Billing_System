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

Enjoy Billing!

📸 Screenshots
(Add screenshots here showing the GUI layout, bill generation, and price manager)

🔧 Customization
Add Items: Click on + Add Item in any category frame.

Update Prices: Click Manage Prices → Choose a category → Update or remove items.

Saved Bills: Found in the bills/ directory as .txt files.

👨‍💻 Developed By
Prince Aryan
📧 princearyan9934@gmail.com
🔗 GitHub | LinkedIn


