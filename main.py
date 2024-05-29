import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Canvas, PhotoImage
from calculations import calculate_dice_game_probabilities


def create_dice_entries(frame, entries, num_dice):
    for widget in frame.winfo_children():
        widget.destroy()

    entries.clear()
    for i in range(num_dice):
        label = tk.Label(frame, text=f"Dice {i+1} Value:")
        label.grid(row=i, column=0, padx=5, pady=2)
        entry = tk.Entry(frame)
        entry.grid(row=i, column=1, padx=5, pady=2)
        entries.append(entry)


def get_dice_values(entries):
    values = []
    for entry in entries:
        value = entry.get().strip()
        if not value.isdigit() or int(value) <= 0:
            raise ValueError("All dice values must be positive integers.")
        values.append(int(value))
    return values


def show_results(player1_dice_values, player2_dice_values):
    prob_1_wins, prob_2_wins, prob_tie = calculate_dice_game_probabilities(player1_dice_values, player2_dice_values)
    result_text = f"Player 1 Wins: {100 * prob_1_wins:.1f}%\nPlayer 2 Wins: {100 * prob_2_wins:.1f}%\nTie: {100 * prob_tie:.1f}%"
    messagebox.showinfo("Results", result_text)


class DiceGameProbabilityCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dice Game Probability Calculator")

        self.player1_dice_entries = []
        self.player2_dice_entries = []

        # Player 1 inputs
        self.create_label("Player 1:", 0, 0)
        self.create_label("Number of Dice:", 1, 0)
        self.player1_dice_combobox = self.create_combobox(list(range(1, 21)), 1, 1)
        self.player1_dice_combobox.bind("<<ComboboxSelected>>",
                                        lambda event: self.update_dice_entries(event, "player1"))

        self.player1_values_frame = tk.Frame(self)
        self.player1_values_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.update_dice_entries_initial("player1")

        # Player 2 inputs
        self.create_label("Player 2:", 3, 0)
        self.create_label("Number of Dice:", 4, 0)
        self.player2_dice_combobox = self.create_combobox(list(range(1, 21)), 4, 1)
        self.player2_dice_combobox.bind("<<ComboboxSelected>>",
                                        lambda event: self.update_dice_entries(event, "player2"))

        self.player2_values_frame = tk.Frame(self)
        self.player2_values_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.update_dice_entries_initial("player2")

        # Canvas for animation and images
        self.canvas = Canvas(self, width=400, height=300)
        self.canvas.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        self.dice_image = PhotoImage(file="dice.png")  # Ensure you have a dice.png file
        self.dice = self.canvas.create_image(180, 150, image=self.dice_image)

        # Calculate button
        calculate_button = tk.Button(self, text="Calculate Probabilities", command=self.calculate_probabilities)
        calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def create_label(self, text, row, column, padx=10, pady=5, sticky=tk.W):
        label = tk.Label(self, text=text)
        label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return label

    def create_combobox(self, values, row, column, default=0, padx=10, pady=5, sticky=tk.W):
        combobox = ttk.Combobox(self, values=values)
        combobox.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        combobox.current(default)
        return combobox

    def update_dice_entries_initial(self, player):
        if player == "player1":
            frame = self.player1_values_frame
            entries = self.player1_dice_entries
        else:
            frame = self.player2_values_frame
            entries = self.player2_dice_entries

        create_dice_entries(frame, entries, 1)

    def update_dice_entries(self, event, player):
        num_dice = int(event.widget.get())

        if player == "player1":
            frame = self.player1_values_frame
            entries = self.player1_dice_entries
        else:
            frame = self.player2_values_frame
            entries = self.player2_dice_entries

        create_dice_entries(frame, entries, num_dice)

    def calculate_probabilities(self):
        try:
            player1_num_dice = int(self.player1_dice_combobox.get())
            player2_num_dice = int(self.player2_dice_combobox.get())

            player1_dice_values = get_dice_values(self.player1_dice_entries)
            player2_dice_values = get_dice_values(self.player2_dice_entries)

            if len(player1_dice_values) != player1_num_dice or len(player2_dice_values) != player2_num_dice:
                raise ValueError("Number of dice and number of values do not match.")

            # Animation loop before calculating probabilities
            self.animate_dice(callback=lambda: show_results(player1_dice_values, player2_dice_values))

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def animate_dice(self, callback):
        for i in range(10):
            self.canvas.move(self.dice, 10, 0)
            self.update()
            self.after(50)
            self.canvas.move(self.dice, -10, 0)
            self.update()
            self.after(50)
        self.after(0, callback)  # Call the callback after the animation loop completes


if __name__ == "__main__":
    app = DiceGameProbabilityCalculator()
    app.mainloop()
