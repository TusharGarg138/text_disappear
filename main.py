import tkinter as tk
from tkinter import font

# Create the main window
win = tk.Tk()
win.title("⏳ Auto-Clear Typing Box")
win.geometry("500x300")
win.configure(bg="#2c3e50")  # Dark background

# Custom font
custom_font = font.Font(family="Helvetica", size=14)

# Add a label
label = tk.Label(win, text="Start typing... (text clears if idle 5s)",
                 font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50")
label.pack(pady=(20, 10))


