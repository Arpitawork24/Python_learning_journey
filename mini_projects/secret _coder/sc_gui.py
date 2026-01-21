# gui is done with the help of chatgpt
import tkinter as tk
import random
import string

last_result = ""   # to store last coded / decoded text

def code_word():
    global last_result
    word = entry.get()

    if word == "":
        result_label.config(text="Please enter a word 😅", fg="red")
        return
    elif len(word) < 3:
        result = word[::-1]
    else:
        temp = word[1:] + word[0]
        front_random = ''.join(random.choices(string.ascii_lowercase, k=3))
        back_random = ''.join(random.choices(string.ascii_lowercase, k=3))
        result = front_random + temp + back_random

    last_result = result
    result_label.config(text=f"Coded: {result}", fg="green")


def decode_word():
    global last_result
    word = entry.get()

    if word == "":
        result_label.config(text="Please enter a word 😅", fg="red")
        return
    elif len(word) < 3:
        result = word[::-1]
    else:
        temp = word[3:-3]
        result = temp[-1] + temp[:-1]

    last_result = result
    result_label.config(text=f"Decoded: {result}", fg="blue")


def copy_result():
    if last_result == "":
        result_label.config(text="Nothing to copy 😅", fg="red")
        return

    root.clipboard_clear()
    root.clipboard_append(last_result)
    result_label.config(text="Copied to clipboard 📋", fg="purple")


# MAIN WINDOW
root = tk.Tk()
root.title("Secret Coder 🔐")
root.geometry("420x350")
root.config(bg="#f0f8ff")

# TITLE
title = tk.Label(root, text="Secret Coder 🔐", font=("Arial", 20, "bold"),
                 bg="#f0f8ff", fg="#333")
title.pack(pady=15)

# INPUT LABEL
input_label = tk.Label(root, text="Enter your word:", font=("Arial", 12),
                       bg="#f0f8ff")
input_label.pack()

# ENTRY BOX
entry = tk.Entry(root, font=("Arial", 14), width=28)
entry.pack(pady=10)

# BUTTON FRAME
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=15)

# CODE BUTTON
code_btn = tk.Button(frame, text="CODE 🔒", font=("Arial", 12, "bold"),
                     bg="#9fd3c7", width=10, command=code_word)
code_btn.grid(row=0, column=0, padx=10)

# DECODE BUTTON
decode_btn = tk.Button(frame, text="DECODE 🔓", font=("Arial", 12, "bold"),
                       bg="#f4a6a6", width=10, command=decode_word)
decode_btn.grid(row=0, column=1, padx=10)

# COPY BUTTON
copy_btn = tk.Button(root, text="Copy Result 📋", font=("Arial", 11, "bold"),
                     bg="#d9b3ff", width=20, command=copy_result)
copy_btn.pack(pady=10)

# RESULT LABEL
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                        bg="#f0f8ff")
result_label.pack(pady=15)

root.mainloop()
