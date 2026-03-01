import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"

def log_key(event):
    key = event.keysym
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {key}\n")

    status_label.config(text=f"Last key logged: {key}")

def clear_log():
    with open(LOG_FILE, "w") as file:
        file.write("")
    status_label.config(text="Log file cleared.")

# Create window
root = tk.Tk()
root.title("Educational Key Event Logger")
root.geometry("400x250")

instructions = tk.Label(
    root,
    text="Click inside this window and start typing.\nKeys will be logged to key_log.txt",
    wraplength=350
)
instructions.pack(pady=20)

clear_button = tk.Button(root, text="Clear Log File", command=clear_log)
clear_button.pack(pady=10)

status_label = tk.Label(root, text="No keys logged yet.")
status_label.pack(pady=10)

# Bind key press event (ONLY inside this window)
root.bind("<Key>", log_key)

root.mainloop()