import tkinter as tk
from PIL import ImageTk, Image
import os

def start_button_clicked():
    os.system('python main.py')

def exit_button_clicked():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Menu")

# Set the window size and position it in the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Make the window full screen
root.attributes('-fullscreen', True)

# Load the background image
background_image = ImageTk.PhotoImage(Image.open("free.jpg"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the start button with a futuristic style
start_button = tk.Button(root, text="Start", command=start_button_clicked, bg="white", font=("Arial", 20), relief=tk.RAISED, bd=3)
start_button.config(fg="blue", activebackground="gray", activeforeground="white")
start_button.place(relx=0.5, rely=0.4, anchor="center")

# Create the exit button with a futuristic style
exit_button = tk.Button(root, text="Exit", command=exit_button_clicked, bg="white", font=("Arial", 20), relief=tk.RAISED, bd=3)
exit_button.config(fg="red", activebackground="gray", activeforeground="white")
exit_button.place(relx=0.5, rely=0.6, anchor="center")

# Start the main loop
root.mainloop()
