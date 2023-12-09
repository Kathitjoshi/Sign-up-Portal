Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
from tkinter import messagebox

def submit_signup():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    # Check if any field is empty
    if not username or not password or not email:
        messagebox.showerror("Error", "All fields must be filled")
        return

    # Display the sign-up information
    message = f"Sign-up successful!\nUsername: {username}\nPassword: {password}\nEmail: {email}"
    messagebox.showinfo("Success", message)

# Create the main window
root = tk.Tk()
root.title("Sign Up Portal")

# Create and place widgets
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_signup)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
