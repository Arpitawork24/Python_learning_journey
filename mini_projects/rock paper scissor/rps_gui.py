import tkinter as tk
import random

def play(user_choice):
    comp_choice = random.randint(1, 3)

    emojis = {1: "✊ Rock", 2: "✋ Paper", 3: "✌️ Scissor"}

    user_label.config(text=f"You chose: {emojis[user_choice]}")
    comp_label.config(text=f"Computer chose: {emojis[comp_choice]}")

    if user_choice == comp_choice:
        result = "It's a Draw 😐"
        result_label.config(fg="orange")
    elif user_choice == 1 and comp_choice == 2:
        result = "You Lose 😭"
        result_label.config(fg="red")
    elif user_choice == 1 and comp_choice == 3:
        result = "You Win 🥳"
        result_label.config(fg="green")
    elif user_choice == 2 and comp_choice == 1:
        result = "You Win 🥳"
        result_label.config(fg="green")
    elif user_choice == 2 and comp_choice == 3:
        result = "You Lose 😭"
        result_label.config(fg="red")
    elif user_choice == 3 and comp_choice == 1:
        result = "You Lose 😭"
        result_label.config(fg="red")
    elif user_choice == 3 and comp_choice == 2:
        result = "You Win 🥳"
        result_label.config(fg="green")

    result_label.config(text=result)

# Window
root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("400x400")
root.config(bg="#f0f8ff")   # light blue background

title = tk.Label(root, text="Rock Paper Scissor", font=("Arial", 20, "bold"),
                 bg="#f0f8ff", fg="#333")
title.pack(pady=15)

user_label = tk.Label(root, text="You chose: ", font=("Arial", 12),
                      bg="#f0f8ff")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12),
                      bg="#f0f8ff")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"),
                        bg="#f0f8ff")
result_label.pack(pady=20)

# Buttons frame
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

btn_rock = tk.Button(frame, text="✊", font=("Arial", 28), width=3,
                     bg="#ffd966", command=lambda: play(1))
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(frame, text="✋", font=("Arial", 28), width=3,
                      bg="#9fd3c7", command=lambda: play(2))
btn_paper.grid(row=0, column=1, padx=10)

btn_scissor = tk.Button(frame, text="✌️", font=("Arial", 28), width=3,
                        bg="#f4a6a6", command=lambda: play(3))
btn_scissor.grid(row=0, column=2, padx=10)

root.mainloop()
