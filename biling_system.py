from tkinter import *
from tkinter import messagebox, ttk
import random
import os
import json

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Retail Billing ")
        
        # Color scheme
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.accent_color = "#3498db"
        self.button_color = "#2980b9"
        self.highlight_color = "#e74c3c"
        
        # Load item prices from file or create default
        self.load_item_prices()
        
        # Main frame styling
        self.root.configure(bg=self.bg_color)
        
        # Title
        title = Label(self.root, text="Prince Billing Software", 
                     font=('Helvetica', 30, 'bold'), pady=2, bd=12, 
                     bg=self.accent_color, fg=self.fg_color, relief=GROOVE)
        title.pack(fill=X)
        
        # Variables
        self.setup_variables()
        
        # Customer Details Frame
        self.create_customer_frame()
        
        # Product Frames
        self.create_medical_frame()
        self.create_grocery_frame()
        self.create_cold_drinks_frame()
        
        # Bill Area
        self.create_bill_frame()
        
        # Buttons Frame
        self.create_buttons_frame()
        
        self.welcome_bill()

    def setup_variables(self):
        # Medical Variables
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()
        
        # Grocery Variables
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        
        # Cold Drinks Variables
        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()
        
        # Total Prices
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
        
        # Customer Details
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
        # Taxes
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        
        # Custom Items
        self.custom_medical_items = []
        self.custom_grocery_items = []
        self.custom_cold_drink_items = []
        
        # Temporary calculation variables
        self.total_medical_price = 0
        self.total_grocery_price = 0
        self.total_cold_drinks_price = 0
        self.total_bill = 0

    def load_item_prices(self):
        try:
            with open('item_prices.json', 'r') as f:
                self.item_prices = json.load(f)
        except:
            # Default prices if file doesn't exist
            self.item_prices = {
                'medical': {
                    'Sanitizer': 2,
                    'Mask': 5,
                    'Hand Gloves': 12,
                    'Dettol': 30,
                    'Newsprin': 5,
                    'Thermal Gun': 15
                },
                'grocery': {
                    'Rice': 10,
                    'Food Oil': 10,
                    'Wheat': 10,
                    'Daal': 6,
                    'Flour': 8,
                    'Maggi': 5
                },
                'cold_drinks': {
                    'Sprite': 10,
                    'Limka': 10,
                    'Mazza': 10,
                    'Coke': 10,
                    'Fanta': 10,
                    'Mountain Duo': 10
                }
            }
            self.save_item_prices()

    def save_item_prices(self):
        with open('item_prices.json', 'w') as f:
            json.dump(self.item_prices, f)

    def create_customer_frame(self):
        F1 = LabelFrame(self.root, text="Customer Details", 
                       font=('Helvetica', 15, 'bold'), bd=10, 
                       fg=self.fg_color, bg=self.bg_color)
        F1.place(x=0, y=80, relwidth=1)
        
        # Customer Name
        cname_lbl = Label(F1, text="Customer Name:", bg=self.bg_color, 
                         fg=self.fg_color, font=('Helvetica', 14))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        cname_txt = Entry(F1, width=20, textvariable=self.c_name, 
                         font=('Helvetica', 14), bd=5, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=5)
        
        # Customer Phone
        cphn_lbl = Label(F1, text="Customer Phone:", bg=self.bg_color, 
                        fg=self.fg_color, font=('Helvetica', 14))
        cphn_lbl.grid(row=0, column=2, padx=10, pady=5, sticky='w')
        cphn_txt = Entry(F1, width=20, textvariable=self.c_phone, 
                        font=('Helvetica', 14), bd=5, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=5)
        
        # Bill Number
        c_bill_lbl = Label(F1, text="Bill Number:", bg=self.bg_color, 
                          fg=self.fg_color, font=('Helvetica', 14))
        c_bill_lbl.grid(row=0, column=4, padx=10, pady=5, sticky='w')
        c_bill_txt = Entry(F1, width=15, textvariable=self.bill_no, 
                          font=('Helvetica', 14), bd=5, relief=GROOVE, 
                          state='readonly')
        c_bill_txt.grid(row=0, column=5, pady=5, padx=5)
        
        # Search Bill
        bil_btn = Button(F1, text="Search Bill", command=self.find_bill, 
                        width=12, bd=5, font=('Helvetica', 12, 'bold'), 
                        bg=self.button_color, fg=self.fg_color, relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    def create_medical_frame(self):
        # Destroy existing frame if it exists
        if hasattr(self, 'F2'):
            self.F2.destroy()
            
        self.F2 = LabelFrame(self.root, text="Medical Items", 
                           font=('Helvetica', 15, 'bold'), bd=10, 
                           fg=self.fg_color, bg=self.bg_color)
        self.F2.place(x=5, y=180, width=325, height=380)
        
        # Medical Items
        row_counter = 0
        for item, price in self.item_prices['medical'].items():
            var_name = f"medical_{item.lower().replace(' ', '_')}"
            
            # Create variable if it doesn't exist
            if not hasattr(self, var_name):
                setattr(self, var_name, IntVar(value=0))
            
            var = getattr(self, var_name)
            
            lbl = Label(self.F2, text=f"{item} (Rs.{price})", 
                       font=('Helvetica', 12), bg=self.bg_color, fg=self.fg_color)
            lbl.grid(row=row_counter, column=0, padx=5, pady=5, sticky='w')
            
            txt = Entry(self.F2, width=8, textvariable=var, 
                       font=('Helvetica', 12), bd=3, relief=GROOVE)
            txt.grid(row=row_counter, column=1, padx=5, pady=5)
            
            row_counter += 1
        
        # Add Custom Medical Item Button
        add_btn = Button(self.F2, text="+ Add Item", command=lambda: self.add_custom_item('medical'), 
                        width=10, bd=3, font=('Helvetica', 10, 'bold'), 
                        bg=self.button_color, fg=self.fg_color, relief=GROOVE)
        add_btn.grid(row=row_counter, columnspan=2, pady=10)

    def create_grocery_frame(self):
        # Destroy existing frame if it exists
        if hasattr(self, 'F3'):
            self.F3.destroy()
            
        self.F3 = LabelFrame(self.root, text="Grocery Items", 
                           font=('Helvetica', 15, 'bold'), bd=10, 
                           fg=self.fg_color, bg=self.bg_color)
        self.F3.place(x=340, y=180, width=325, height=380)
        
        # Grocery Items
        row_counter = 0
        for item, price in self.item_prices['grocery'].items():
            var_name = f"grocery_{item.lower().replace(' ', '_')}"
            
            # Create variable if it doesn't exist
            if not hasattr(self, var_name):
                setattr(self, var_name, IntVar(value=0))
            
            var = getattr(self, var_name)
            
            lbl = Label(self.F3, text=f"{item} (Rs.{price})", 
                       font=('Helvetica', 12), bg=self.bg_color, fg=self.fg_color)
            lbl.grid(row=row_counter, column=0, padx=5, pady=5, sticky='w')
            
            txt = Entry(self.F3, width=8, textvariable=var, 
                       font=('Helvetica', 12), bd=3, relief=GROOVE)
            txt.grid(row=row_counter, column=1, padx=5, pady=5)
            
            row_counter += 1
        
        # Add Custom Grocery Item Button
        add_btn = Button(self.F3, text="+ Add Item", command=lambda: self.add_custom_item('grocery'), 
                        width=10, bd=3, font=('Helvetica', 10, 'bold'), 
                        bg=self.button_color, fg=self.fg_color, relief=GROOVE)
        add_btn.grid(row=row_counter, columnspan=2, pady=10)

    def create_cold_drinks_frame(self):
        # Destroy existing frame if it exists
        if hasattr(self, 'F4'):
            self.F4.destroy()
            
        self.F4 = LabelFrame(self.root, text="Cold Drinks", 
                           font=('Helvetica', 15, 'bold'), bd=10, 
                           fg=self.fg_color, bg=self.bg_color)
        self.F4.place(x=675, y=180, width=325, height=380)
        
        # Cold Drinks Items
        row_counter = 0
        for item, price in self.item_prices['cold_drinks'].items():
            var_name = f"cold_{item.lower().replace(' ', '_')}"
            
            # Create variable if it doesn't exist
            if not hasattr(self, var_name):
                setattr(self, var_name, IntVar(value=0))
            
            var = getattr(self, var_name)
            
            lbl = Label(self.F4, text=f"{item} (Rs.{price})", 
                       font=('Helvetica', 12), bg=self.bg_color, fg=self.fg_color)
            lbl.grid(row=row_counter, column=0, padx=5, pady=5, sticky='w')
            
            txt = Entry(self.F4, width=8, textvariable=var, 
                       font=('Helvetica', 12), bd=3, relief=GROOVE)
            txt.grid(row=row_counter, column=1, padx=5, pady=5)
            
            row_counter += 1
        
        # Add Custom Cold Drink Item Button
        add_btn = Button(self.F4, text="+ Add Item", command=lambda: self.add_custom_item('cold_drinks'), 
                        width=10, bd=3, font=('Helvetica', 10, 'bold'), 
                        bg=self.button_color, fg=self.fg_color, relief=GROOVE)
        add_btn.grid(row=row_counter, columnspan=2, pady=10)

    def create_bill_frame(self):
        self.F5 = Frame(self.root, bd=10, relief=GROOVE, bg=self.bg_color)
        self.F5.place(x=1010, y=180, width=350, height=380)
        
        bill_title = Label(self.F5, text="Bill Area", font=('Helvetica', 16, 'bold'), 
                         bd=7, relief=GROOVE, bg=self.accent_color, fg=self.fg_color)
        bill_title.pack(fill=X)
        
        scroll_y = Scrollbar(self.F5, orient=VERTICAL)
        self.txtarea = Text(self.F5, yscrollcommand=scroll_y.set, 
                          font=('Courier', 12), bd=5, relief=GROOVE, 
                          bg='#f8f9fa', fg='#212529')
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    def create_buttons_frame(self):
        self.F6 = LabelFrame(self.root, text="Bill Summary", 
                           font=('Helvetica', 14, 'bold'), bd=10, 
                           fg=self.fg_color, bg=self.bg_color)
        self.F6.place(x=0, y=560, relwidth=1, height=140)
        
        # Price Labels and Entries
        labels = [
            ("Total Medical Price", self.medical_price, 0, 0),
            ("Total Grocery Price", self.grocery_price, 1, 0),
            ("Total Cold Drinks Price", self.cold_drinks_price, 2, 0),
            ("Medical Tax (5%)", self.medical_tax, 0, 2),
            ("Grocery Tax (5%)", self.grocery_tax, 1, 2),
            ("Cold Drinks Tax (10%)", self.cold_drinks_tax, 2, 2)
        ]
        
        for text, var, row, col in labels:
            lbl = Label(self.F6, text=text, font=('Helvetica', 12), 
                       bg=self.bg_color, fg=self.fg_color)
            lbl.grid(row=row, column=col, padx=5, pady=2, sticky='w')
            ent = Entry(self.F6, width=15, textvariable=var, 
                      font=('Helvetica', 12), bd=3, relief=GROOVE, 
                      state='readonly')
            ent.grid(row=row, column=col+1, padx=5, pady=2)
        
        # Action Buttons
        btn_f = Frame(self.F6, bd=5, relief=GROOVE, bg=self.bg_color)
        btn_f.place(x=700, width=600, height=100)
        
        buttons = [
            ("Total", self.total, 0, 0),
            ("Generate Bill", self.bill_area, 0, 1),
            ("Clear", self.clear_data, 0, 2),
            ("Exit", self.exit_app, 0, 3),
            ("Manage Prices", self.manage_prices, 1, 1),
            ("Save Bill", self.save_bill, 1, 2)  # Added Save Bill button
        ]
        
        for text, cmd, row, col in buttons:
            btn = Button(btn_f, text=text, command=cmd, bd=3, 
                        font=('Helvetica', 12, 'bold'), 
                        bg=self.button_color, fg=self.fg_color)
            btn.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=2)

    def add_custom_item(self, category):
        popup = Toplevel(self.root)
        popup.title(f"Add Custom {category.replace('_', ' ').title()} Item")
        popup.geometry("400x200")
        popup.configure(bg=self.bg_color)
        
        Label(popup, text="Item Name:", bg=self.bg_color, fg=self.fg_color, 
             font=('Helvetica', 12)).grid(row=0, column=0, padx=5, pady=5)
        name_entry = Entry(popup, font=('Helvetica', 12))
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        Label(popup, text="Price:", bg=self.bg_color, fg=self.fg_color, 
             font=('Helvetica', 12)).grid(row=1, column=0, padx=5, pady=5)
        price_entry = Entry(popup, font=('Helvetica', 12))
        price_entry.grid(row=1, column=1, padx=5, pady=5)
        
        def save_item():
            name = name_entry.get().strip()
            try:
                price = float(price_entry.get())
                if name and price > 0:
                    self.item_prices[category][name] = price
                    self.save_item_prices()
                    messagebox.showinfo("Success", f"{name} added to {category} items!")
                    popup.destroy()
                    # Refresh the relevant frame
                    if category == 'medical':
                        self.create_medical_frame()
                    elif category == 'grocery':
                        self.create_grocery_frame()
                    else:
                        self.create_cold_drinks_frame()
                else:
                    messagebox.showerror("Error", "Please enter valid name and price")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid price")
        
        Button(popup, text="Save", command=save_item, bg=self.button_color, 
              fg=self.fg_color, font=('Helvetica', 12)).grid(row=2, columnspan=2, pady=10)

    def manage_prices(self):
        popup = Toplevel(self.root)
        popup.title("Manage Item Prices")
        popup.geometry("600x400")
        popup.configure(bg=self.bg_color)
        
        notebook = ttk.Notebook(popup)
        notebook.pack(expand=1, fill='both')
        
        # Create tabs for each category
        categories = ['medical', 'grocery', 'cold_drinks']
        tab_names = ['Medical Items', 'Grocery Items', 'Cold Drinks']
        
        for cat, name in zip(categories, tab_names):
            frame = Frame(notebook, bg=self.bg_color)
            notebook.add(frame, text=name)
            
            # Create a canvas and scrollbar
            canvas = Canvas(frame, bg=self.bg_color)
            scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas, bg=self.bg_color)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            # Add items to the scrollable frame
            for i, (item, price) in enumerate(self.item_prices[cat].items()):
                row_frame = Frame(scrollable_frame, bg=self.bg_color)
                row_frame.pack(fill='x', pady=2)
                
                Label(row_frame, text=item, width=20, anchor='w', 
                     bg=self.bg_color, fg=self.fg_color).pack(side='left', padx=5)
                
                price_var = StringVar(value=str(price))
                Entry(row_frame, textvariable=price_var, width=10, 
                     font=('Helvetica', 12)).pack(side='left', padx=5)
                
                def save_change(cat=cat, item=item, var=price_var):
                    try:
                        new_price = float(var.get())
                        if new_price > 0:
                            self.item_prices[cat][item] = new_price
                            self.save_item_prices()
                            messagebox.showinfo("Success", f"Price updated for {item}")
                            # Refresh all frames to show updated prices
                            self.create_medical_frame()
                            self.create_grocery_frame()
                            self.create_cold_drinks_frame()
                        else:
                            messagebox.showerror("Error", "Price must be positive")
                    except ValueError:
                        messagebox.showerror("Error", "Please enter a valid price")
                
                Button(row_frame, text="Update", command=save_change, 
                      bg=self.button_color, fg=self.fg_color).pack(side='left', padx=5)
                
                if item not in ['Sanitizer', 'Mask', 'Hand Gloves', 'Dettol', 'Newsprin', 'Thermal Gun',
                              'Rice', 'Food Oil', 'Wheat', 'Daal', 'Flour', 'Maggi',
                              'Sprite', 'Limka', 'Mazza', 'Coke', 'Fanta', 'Mountain Duo']:
                    def remove_item(cat=cat, item=item):
                        del self.item_prices[cat][item]
                        self.save_item_prices()
                        messagebox.showinfo("Success", f"{item} removed")
                        popup.destroy()
                        self.manage_prices()  # Refresh the window
                        # Refresh the relevant frame
                        if cat == 'medical':
                            self.create_medical_frame()
                        elif cat == 'grocery':
                            self.create_grocery_frame()
                        else:
                            self.create_cold_drinks_frame()
                    
                    Button(row_frame, text="Remove", command=remove_item, 
                          bg=self.highlight_color, fg=self.fg_color).pack(side='left', padx=5)

    def total(self):
        # Calculate Medical Prices
        self.total_medical_price = 0
        for item, price in self.item_prices['medical'].items():
            var_name = f"medical_{item.lower().replace(' ', '_')}"
            if hasattr(self, var_name):
                var = getattr(self, var_name)
                self.total_medical_price += var.get() * price
        
        self.medical_price.set(f"Rs. {self.total_medical_price:.2f}")
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set(f"Rs. {self.c_tax:.2f}")
        
        # Calculate Grocery Prices
        self.total_grocery_price = 0
        for item, price in self.item_prices['grocery'].items():
            var_name = f"grocery_{item.lower().replace(' ', '_')}"
            if hasattr(self, var_name):
                var = getattr(self, var_name)
                self.total_grocery_price += var.get() * price
        
        self.grocery_price.set(f"Rs. {self.total_grocery_price:.2f}")
        self.g_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set(f"Rs. {self.g_tax:.2f}")
        
        # Calculate Cold Drinks Prices
        self.total_cold_drinks_price = 0
        for item, price in self.item_prices['cold_drinks'].items():
            var_name = f"cold_{item.lower().replace(' ', '_')}"
            if hasattr(self, var_name):
                var = getattr(self, var_name)
                self.total_cold_drinks_price += var.get() * price
        
        self.cold_drinks_price.set(f"Rs. {self.total_cold_drinks_price:.2f}")
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set(f"Rs. {self.c_d_tax:.2f}")
        
        # Calculate Total Bill
        self.total_bill = sum([
            self.total_medical_price, self.total_grocery_price, 
            self.total_cold_drinks_price, self.c_tax, 
            self.g_tax, self.c_d_tax
        ])

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to  Store\n")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n===========================================")
        self.txtarea.insert(END, "\nProduct\t\tQTY\t\tPrice")
        self.txtarea.insert(END, "\n===========================================")

    def bill_area(self):
        if not self.c_name.get() or not self.c_phone.get():
            messagebox.showerror("Error", "Customer details are required")
            return
        
        if (self.medical_price.get() == "" and 
            self.grocery_price.get() == "" and 
            self.cold_drinks_price.get() == ""):
            messagebox.showerror("Error", "No products purchased")
            return
        
        self.welcome_bill()
        
        # Medical Items
        for item, price in self.item_prices['medical'].items():
            var_name = f"medical_{item.lower().replace(' ', '_')}"
            if hasattr(self, var_name):
                var = getattr(self, var_name)
                if var.get() != 0:
                    self.txtarea.insert(END, f"\n{item}\t\t{var.get()}\t\tRs.{var.get() * price:.2f}")
        
        # Grocery Items
        for item, price in self.item_prices['grocery'].items():
            var_name = f"grocery_{item.lower().replace(' ', '_')}"
            if hasattr(self, var_name):
                var = getattr(self, var_name)
                if var.get() != 0:
                    self.txtarea.insert(END, f"\n{item}\t\t{var.get()}\t\tRs.{var.get() * price:.2f}")
        
        # Cold Drinks
        for item, price in self.item_prices['cold_drinks'].items():
            var_name = f"cold_{item.lower().replace(' ', '_')}"
            if hasattr(self, var_name):
                var = getattr(self, var_name)
                if var.get() != 0:
                    self.txtarea.insert(END, f"\n{item}\t\t{var.get()}\t\tRs.{var.get() * price:.2f}")
        
        # Taxes
        self.txtarea.insert(END, "\n===========================================")
        if float(self.medical_tax.get()[4:]) > 0:
            self.txtarea.insert(END, f"\nMedical Tax (5%)\t\t\t{self.medical_tax.get()}")
        if float(self.grocery_tax.get()[4:]) > 0:
            self.txtarea.insert(END, f"\nGrocery Tax (5%)\t\t\t{self.grocery_tax.get()}")
        if float(self.cold_drinks_tax.get()[4:]) > 0:
            self.txtarea.insert(END, f"\nCold Drinks Tax (10%)\t\t\t{self.cold_drinks_tax.get()}")
        
        self.txtarea.insert(END, "\n===========================================")
        self.txtarea.insert(END, f"\nTotal Bill:\t\t\tRs.{self.total_bill:.2f}")
        self.txtarea.insert(END, "\n===========================================")
        self.txtarea.insert(END, "\nThank you for shopping with us!")

    def save_bill(self):
        if not self.txtarea.get('1.0', 'end-1c').strip():
            messagebox.showerror("Error", "No bill to save")
            return
            
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op:
            # Create bills directory if it doesn't exist
            if not os.path.exists('bills'):
                os.makedirs('bills')
            
            bill_data = self.txtarea.get('1.0', END)
            with open(f"bills/{self.bill_no.get()}.txt", "w") as f:
                f.write(bill_data)
            
            messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} saved successfully")
            
            # Generate a new bill number for next transaction
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.clear_data(keep_customer=True)

    def find_bill(self):
        if not self.search_bill.get():
            messagebox.showerror("Error", "Please enter a bill number to search")
            return
        
        if not os.path.exists('bills'):
            messagebox.showerror("Error", "No bills found")
            return
        
        found = False
        for filename in os.listdir('bills'):
            if filename.split('.')[0] == self.search_bill.get():
                with open(f'bills/{filename}', 'r') as f:
                    self.txtarea.delete('1.0', END)
                    self.txtarea.insert(END, f.read())
                found = True
                break
        
        if not found:
            messagebox.showerror("Error", "Bill not found")

    def clear_data(self, keep_customer=False):
        op = messagebox.askyesno("Clear", "Do you really want to clear?")
        if not op:
            return
        
        # Clear all item quantities
        for category in ['medical', 'grocery', 'cold_drinks']:
            for item in self.item_prices[category].keys():
                var_name = f"{category.split('_')[0]}_{item.lower().replace(' ', '_')}"
                if hasattr(self, var_name):
                    getattr(self, var_name).set(0)
        
        # Clear prices and taxes
        self.medical_price.set("")
        self.grocery_price.set("")
        self.cold_drinks_price.set("")
        self.medical_tax.set("")
        self.grocery_tax.set("")
        self.cold_drinks_tax.set("")
        
        if not keep_customer:
            self.c_name.set("")
            self.c_phone.set("")
        
        # Generate new bill number
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()