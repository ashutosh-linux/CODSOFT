import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer for the password length.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    result_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
label = tk.Label(root, text="Enter the desired password length:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Password:")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
