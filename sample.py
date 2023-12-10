import tkinter as tk

def check_login():
    if username.get() == "user" and password.get() == "password":
        login_status.config(text="Login successful")
    else:
        login_status.config(text="Invalid username or password")

root = tk.Tk()
root.title("Simple Login")

username_label = tk.Label(root, text="Username")
username_label.pack()
username = tk.Entry(root)
username.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password = tk.Entry(root, show="*")
password.pack()

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

login_status = tk.Label(root, text="")
login_status.pack()

root.mainloop()

