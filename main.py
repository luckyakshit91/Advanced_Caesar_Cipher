import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

from caesar_cipher import encrypt, decrypt
from brute_force import brute_force_attack
from frequency_analysis import frequency_analysis
from aes_module import aes_encrypt
from database import save_message
from logger_module import log_message
from password_auth import check_password


# ---------------- PASSWORD CHECK ---------------- #
password = input("Enter password: ")

if not check_password(password):
    print("Access Denied")
    exit()


# ---------------- FUNCTIONS ---------------- #

def show_result(text):
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, text)


def encrypt_text():
    try:
        text = entry_text.get()
        shift = int(entry_shift.get())

        encrypted = encrypt(text, shift)

        save_message(text, encrypted)
        log_message(f"Encrypted: {encrypted}")

        show_result(encrypted)

    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number")


def decrypt_text():
    try:
        text = entry_text.get()
        shift = int(entry_shift.get())

        decrypted = decrypt(text, shift)

        show_result(decrypted)

    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number")


def brute_force_demo():
    text = entry_text.get()

    output = brute_force_attack(text)

    show_result(output)


def frequency_demo():
    text = entry_text.get()

    output = frequency_analysis(text)

    show_result(output)


def aes_demo():
    text = entry_text.get()

    encrypted = aes_encrypt(text)

    show_result(encrypted)


def encrypt_file():
    filename = filedialog.askopenfilename()

    if filename:
        with open(filename, "r") as file:
            data = file.read()

        encrypted = encrypt(data, 3)

        with open("encrypted_file.txt", "w") as file:
            file.write(encrypted)

        messagebox.showinfo("Success", "File Encrypted Successfully")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Advanced Caesar Cipher Security Suite")
root.geometry("950x700")
root.configure(bg="#121212")

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Segoe UI", 11, "bold"),
    padding=8
)

style.configure(
    "TLabel",
    background="#121212",
    foreground="white",
    font=("Segoe UI", 11)
)

# Title
title = tk.Label(
    root,
    text="ADVANCED CAESAR CIPHER SECURITY SUITE",
    font=("Segoe UI", 20, "bold"),
    fg="#00FF99",
    bg="#121212"
)
title.pack(pady=20)

# Text Label
ttk.Label(root, text="Enter Text").pack()

entry_text = tk.Entry(
    root,
    width=70,
    font=("Segoe UI", 12)
)
entry_text.pack(pady=10)

# Shift Label
ttk.Label(root, text="Shift Value").pack()

entry_shift = tk.Entry(
    root,
    width=20,
    font=("Segoe UI", 12)
)
entry_shift.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=20)

ttk.Button(
    button_frame,
    text="Encrypt",
    command=encrypt_text
).grid(row=0, column=0, padx=10, pady=10)

ttk.Button(
    button_frame,
    text="Decrypt",
    command=decrypt_text
).grid(row=0, column=1, padx=10, pady=10)

ttk.Button(
    button_frame,
    text="Brute Force Attack",
    command=brute_force_demo
).grid(row=1, column=0, padx=10, pady=10)

ttk.Button(
    button_frame,
    text="Frequency Analysis",
    command=frequency_demo
).grid(row=1, column=1, padx=10, pady=10)

ttk.Button(
    button_frame,
    text="AES Comparison",
    command=aes_demo
).grid(row=2, column=0, padx=10, pady=10)

ttk.Button(
    button_frame,
    text="Encrypt TXT File",
    command=encrypt_file
).grid(row=2, column=1, padx=10, pady=10)

# Result Section
result_title = tk.Label(
    root,
    text="RESULT",
    font=("Segoe UI", 14, "bold"),
    fg="#00FF99",
    bg="#121212"
)
result_title.pack(pady=10)

result_box = ScrolledText(
    root,
    width=100,
    height=18,
    font=("Consolas", 11),
    bg="#1E1E1E",
    fg="white",
    insertbackground="white"
)

result_box.pack(pady=10)

root.mainloop()