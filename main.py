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

# Create a styled Text box
text_box = tk.Text(win, height=8, width=50, font=custom_font,
                   bg="#ecf0f1", fg="#2c3e50", insertbackground="#2c3e50",
                   bd=0, padx=10, pady=10)
text_box.pack(pady=10)

# Variable to store timer ID
timer_id = None

# Function to clear the text
def clear_text():
    text_box.delete("1.0", tk.END)
    label.config(text="💨 Text cleared due to 5 sec of no typing!")


