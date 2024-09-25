import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x400")
        
        self.login_successful = False
        self.is_admin = False

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("TCombobox", font=("Arial", 12))

        self.option_label = ttk.Label(root, text="Choose Option")
        self.option_label.pack(pady=5)
        self.option_var = tk.StringVar(value="login")
        self.option_menu = ttk.Combobox(root, textvariable=self.option_var, state="readonly")
        self.option_menu['values'] = ("login", "create account")
        self.option_menu.pack(pady=5)
        self.option_menu.bind("<<ComboboxSelected>>", self.update_form)
        
        self.username_label = ttk.Label(root, text="Username")
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(root)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(root, text="Password")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(root, show='*')
        self.password_entry.pack(pady=5)

        self.account_type_label = ttk.Label(root, text="Account Type")
        self.account_type_label.pack(pady=5)
        self.account_type_var = tk.StringVar(value="user")
        self.account_type_menu = ttk.Combobox(root, textvariable=self.account_type_var, state="readonly")
        self.account_type_menu['values'] = ("user", "admin")
        self.account_type_menu.pack(pady=5)
        self.account_type_menu.bind("<<ComboboxSelected>>", self.update_admin_fields)

        self.admin_password_label = ttk.Label(root, text="Admin Password")
        self.admin_password_entry = ttk.Entry(root, show='*')

        self.submit_button = ttk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

        self.conn = sqlite3.connect('users.db')
        self.create_user_table()
        self.update_form()

    def create_user_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS users
                             (username TEXT PRIMARY KEY NOT NULL,
                             password TEXT NOT NULL,
                             is_admin BOOLEAN NOT NULL);''')
        self.conn.commit()

    def update_form(self, event=None):
        option = self.option_var.get()
        if option == "login":
            self.account_type_label.pack_forget()
            self.account_type_menu.pack_forget()
            self.admin_password_label.pack_forget()
            self.admin_password_entry.pack_forget()
        else:
            self.account_type_label.pack(pady=5)
            self.account_type_menu.pack(pady=5)
            self.update_admin_fields()

    def update_admin_fields(self, event=None):
        if self.account_type_var.get() == "admin":
            self.admin_password_label.pack(pady=5)
            self.admin_password_entry.pack(pady=5)
        else:
            self.admin_password_label.pack_forget()
            self.admin_password_entry.pack_forget()

    def submit(self):
        option = self.option_var.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if option == "login":
            self.login(username, password)
        else:
            account_type = self.account_type_var.get()
            if account_type == "admin":
                admin_password = self.admin_password_entry.get()
                if admin_password != "Safi123":
                    messagebox.showerror("Create Account", "Invalid admin password")
                    return
            self.create_account(username, password, account_type == "admin")

        if self.login_successful:
            self.is_admin = self.check_if_admin(username)
            self.root.destroy()

    def login(self, username, password):
        cursor = self.conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        if result:
            self.login_successful = True
        else:
            messagebox.showerror("Login", "Invalid username or password")

    def create_account(self, username, password, is_admin):
        cursor = self.conn.execute("SELECT * FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        if result:
            messagebox.showerror("Create Account", "Username already exists")
        else:
            self.conn.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
                              (username, password, is_admin))
            self.conn.commit()
            if is_admin:
                messagebox.showinfo("Create Account", "Admin account created successfully!")
            else:
                messagebox.showinfo("Create Account", "User account created successfully!")
            self.login_successful = True

    def check_if_admin(self, username):
        cursor = self.conn.execute("SELECT is_admin FROM users WHERE username=?", (username,))
        result = cursor.fetchone()
        return result[0] if result else False

    def __del__(self):
        self.conn.close()
