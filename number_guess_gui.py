import tkinter as tk
import random

# Main application class
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.high_score = None  # To store best (lowest) attempt count
        self.setup_difficulty_screen()  # Show difficulty selection at start

    def setup_difficulty_screen(self):
        # Clear previous widgets (if any)
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create and pack difficulty selection buttons
        tk.Label(self.root, text="Choose Difficulty", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Easy (1-10)", command=lambda: self.start_game(10, 5)).pack(pady=5)
        tk.Button(self.root, text="Medium (1-50)", command=lambda: self.start_game(50, 7)).pack(pady=5)
        tk.Button(self.root, text="Hard (1-100)", command=lambda: self.start_game(100, 10)).pack(pady=5)

    def start_game(self, max_num, max_attempts):
        self.max_num = max_num           # Max number based on difficulty
        self.max_attempts = max_attempts # Max tries allowed
        self.secret_number = random.randint(1, max_num)  # Generate secret number
        self.attempts = 0                # Reset attempt count

        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Label to show game instruction
        self.label = tk.Label(self.root, text=f"Guess a number between 1 and {max_num}", font=("Arial", 14))
        self.label.pack(pady=10)

        # Entry for number input
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)
        self.entry.focus()

        # Submit button
        self.submit_btn = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_btn.pack(pady=5)

        # Message label to show feedback
        self.message = tk.Label(self.root, text="")
        self.message.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())  # Get number from entry
            self.attempts += 1

            # Clear entry field
            self.entry.delete(0, tk.END)

            if guess < 1 or guess > self.max_num:
                self.message.config(text=f"Please enter a number between 1 and {self.max_num}")
                return

            if guess < self.secret_number:
                self.message.config(text="📉 Too low!")
            elif guess > self.secret_number:
                self.message.config(text="📈 Too high!")
            else:
                # Correct guess
                text = f"🎉 Correct! You guessed it in {self.attempts} attempts."
                if self.high_score is None or self.attempts < self.high_score:
                    self.high_score = self.attempts
                    text += "\n🏆 New High Score!"
                self.end_game(text)
                return

            # If attempts are exhausted
            if self.attempts >= self.max_attempts:
                self.end_game(f"❌ Game Over! The number was {self.secret_number}")

        except ValueError:
            # If user enters non-numeric input
            self.message.config(text="❌ Please enter a valid number.")

    def end_game(self, result_message):
        # Clear current game screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Show result
        tk.Label(self.root, text=result_message, font=("Arial", 14)).pack(pady=10)

        # Replay or quit buttons
        tk.Button(self.root, text="Play Again", command=self.setup_difficulty_screen).pack(pady=5)
        tk.Button(self.root, text="Quit", command=self.root.destroy).pack(pady=5)

# Create the window and start the game
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
