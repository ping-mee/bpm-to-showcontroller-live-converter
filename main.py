import tkinter as tk
from tkinter import ttk
import numpy as np

def bpm_to_fader(bpm):
    """Convert BPM to fader value using linear interpolation."""
    bpm_values = [0, 15, 30, 60, 120, 216]
    fader_values = [0, 10, 21, 41, 82, 157]
    
    return int(np.interp(bpm, bpm_values, fader_values))

def convert(event=None):
    """Get BPM input, convert it, and display the result."""
    try:
        bpm = float(bpm_entry.get())
        fader_value = bpm_to_fader(bpm)
        result_label.config(text=f"Fader Value: {fader_value}")
    except ValueError:
        result_label.config(text="Please enter a valid BPM")

# Create UI
root = tk.Tk()
root.title("BPM to Showcontroller Live calculator")
root.geometry("300x150")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Enter BPM:").pack()
bpm_entry = ttk.Entry(frame)
bpm_entry.pack()
bpm_entry.bind("<Return>", convert)  # Bind Enter key to conversion function

convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.pack(pady=5)

result_label = ttk.Label(frame, text="")
result_label.pack()

root.mainloop()
