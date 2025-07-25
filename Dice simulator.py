import tkinter as tk
import random

# Dice faces as text
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# Function to roll the dice
def roll_dice():
    number = random.randint(1, 6)
    result.set(f"You rolled: {dice_faces[number]}")

# Creating GUI window
window = tk.Tk()
window.title("Dice Simulator 🎲")
window.geometry("300x200")

# Variable to display result
result = tk.StringVar()
result.set("Click to roll the dice!")

# Label to show result
label = tk.Label(window, textvariable=result, font=("Arial", 20))
label.pack(pady=30)

# Button to roll
button = tk.Button(window, text="Roll Dice", command=roll_dice, font=("Arial", 14))
button.pack()

# Keep the window running
window.mainloop()
