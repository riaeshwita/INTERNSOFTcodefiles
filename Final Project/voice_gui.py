import tkinter as tk
from tkinter import scrolledtext
import threading
import voice_assistant  # Import the assistant logic

# Function to update log_area with messages
def update_log(text):
    log_area.insert(tk.END, text + "\n")
    log_area.see(tk.END)

# Function to start the assistant in a new thread
def start_assistant():
    # Start the assistant logic in a separate thread
    threading.Thread(target=voice_assistant.start_assistant_logic, args=(update_log,), daemon=True).start()
    update_log("Assistant started...\n")

# Setup UI
root = tk.Tk()
root.title("Jarvis - Voice Assistant")
root.geometry("500x400")

root.config(bg="#E2EAF4")

# Title Label with background color change to match the window's background
title = tk.Label(root, text="JARVIS - Voice Assistant", font=("Calibri", 16, "bold"), bg="#E2EAF4", fg="#000000")
title.pack(pady=20)


start_button = tk.Button(
    root,
    text="Start Assistant",
    command=start_assistant,
    bg="#B7C5D5",       # Button background color (greenish)
    fg="black",         # Text color
    activebackground="#A1B0C5",  # Color when pressed
    font=("Calibri", 12, "bold"),  # Modern font
    relief="flat",      # Removes sharp edges (optional)
    padx=10, pady=5     # Padding inside the button
)
start_button.pack(pady=10)


log_area = scrolledtext.ScrolledText(
    root,
    width=60,
    height=15,
    bg="#E2EAF4",             # Light grey background
    fg="#000000",             # Dark text
    insertbackground="black", # Cursor color
    font=("Calibri", 11),    # Modern font
    relief="flat",            # Flat border
    borderwidth=2,            # Slight border
    wrap=tk.WORD              # Wrap words neatly
)
log_area.pack(pady=10)


exit_button = tk.Button(
    root,
    text="Exit",
    command=root.quit,
    bg="#B7C5D5",            # Red background
    fg="black",              # White text
    activebackground="#A1B0C5",  # Slightly darker red when clicked
    font=("Calibri", 12, "bold"),  # Same modern font
    relief="flat",           # Flat edges
    padx=10, pady=5          # Internal padding
)
exit_button.pack(pady=10)


root.mainloop()
