import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calculations import calculate_dice_game_probabilities
import numpy as np

def calculate_probabilities():
    try:
        # Get the number of dice and their sizes from user inputs
        player1_num_dice = int(player1_dice_combobox.get())
        player2_num_dice = int(player2_dice_combobox.get())

        player1_dice_values = [int(dice.strip()) for dice in player1_values_entry.get().split(',')]
        player2_dice_values = [int(dice.strip()) for dice in player2_values_entry.get().split(',')]

        if len(player1_dice_values) != player1_num_dice or len(player2_dice_values) != player2_num_dice:
            raise ValueError("Number of dice and number of values do not match.")
        
        # Calculate the probabilities
        prob_1_wins, prob_2_wins, prob_tie = calculate_dice_game_probabilities(player1_dice_values, player2_dice_values)
        
        # Display the results
        result_text = f"Player 1 Wins: {100*prob_1_wins:.1f}%\nPlayer 2 Wins: {100*prob_2_wins:.1f}%\nTie: {100*prob_tie:.1f}%"
        messagebox.showinfo("Results", result_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up the main window
root = tk.Tk()
root.title("Dice Game Probability Calculator")

# Player 1 inputs
player1_label = tk.Label(root, text="Player 1:")
player1_label.grid(row=0, column=0, padx=10, pady=5)

player1_dice_label = tk.Label(root, text="Number of Dice:")
player1_dice_label.grid(row=1, column=0, padx=10, pady=5)
player1_dice_combobox = ttk.Combobox(root, values=list(range(1, 21)))
player1_dice_combobox.grid(row=1, column=1, padx=10, pady=5)
player1_dice_combobox.current(0)  # Set default value

player1_values_label = tk.Label(root, text="Dice Values (comma separated):")
player1_values_label.grid(row=2, column=0, padx=10, pady=5)
player1_values_entry = tk.Entry(root)
player1_values_entry.grid(row=2, column=1, padx=10, pady=5)

# Player 2 inputs
player2_label = tk.Label(root, text="Player 2:")
player2_label.grid(row=3, column=0, padx=10, pady=5)

player2_dice_label = tk.Label(root, text="Number of Dice:")
player2_dice_label.grid(row=4, column=0, padx=10, pady=5)
player2_dice_combobox = ttk.Combobox(root, values=list(range(1, 21)))
player2_dice_combobox.grid(row=4, column=1, padx=10, pady=5)
player2_dice_combobox.current(0)  # Set default value

player2_values_label = tk.Label(root, text="Dice Values (comma separated):")
player2_values_label.grid(row=5, column=0, padx=10, pady=5)
player2_values_entry = tk.Entry(root)
player2_values_entry.grid(row=5, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Probabilities", command=calculate_probabilities)
calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
