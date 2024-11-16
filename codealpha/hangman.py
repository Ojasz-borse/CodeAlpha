import tkinter as tk
import random

# Hangman word list
words = ['python', 'java', 'hangman', 'programming', 'computer']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        # Game variables
        self.word = random.choice(words).upper()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6

        # GUI setup
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 24), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)

        # Hangman canvas
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.update_hangman_graphic()

        # Display word
        self.word_display = tk.StringVar()
        self.word_display.set(" ".join(["_" if letter not in self.guessed_letters else letter for letter in self.word]))
        word_label = tk.Label(self.root, textvariable=self.word_display, font=("Helvetica", 20), bg="#f0f0f0", fg="#333")
        word_label.pack(pady=10)

        # Entry and submit button for letter guesses
        self.entry = tk.Entry(self.root, font=("Helvetica", 16), justify="center")
        self.entry.pack(pady=10)

        submit_button = tk.Button(self.root, text="Guess", font=("Helvetica", 14), command=self.guess_letter)
        submit_button.pack()

        # Message label for feedback
        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#f0f0f0", fg="#d9534f")
        self.message_label.pack(pady=10)

    def update_hangman_graphic(self):
        """Draw hangman on canvas based on incorrect guesses."""
        self.canvas.delete("all")
        # Base
        self.canvas.create_line(20, 180, 180, 180, width=3)
        self.canvas.create_line(60, 180, 60, 20, width=3)
        self.canvas.create_line(60, 20, 120, 20, width=3)
        self.canvas.create_line(120, 20, 120, 40, width=3)

        # Parts based on incorrect guesses
        if self.incorrect_guesses >= 1:  # Head
            self.canvas.create_oval(100, 40, 140, 80, width=3)
        if self.incorrect_guesses >= 2:  # Body
            self.canvas.create_line(120, 80, 120, 130, width=3)
        if self.incorrect_guesses >= 3:  # Left arm
            self.canvas.create_line(120, 90, 90, 110, width=3)
        if self.incorrect_guesses >= 4:  # Right arm
            self.canvas.create_line(120, 90, 150, 110, width=3)
        if self.incorrect_guesses >= 5:  # Left leg
            self.canvas.create_line(120, 130, 90, 160, width=3)
        if self.incorrect_guesses >= 6:  # Right leg
            self.canvas.create_line(120, 130, 150, 160, width=3)

    def guess_letter(self):
        """Handle letter guessing logic."""
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter!")
        elif guess in self.word:
            self.guessed_letters.add(guess)
            self.message_label.config(text="Good guess!", fg="#5cb85c")
            self.update_word_display()
            if all(letter in self.guessed_letters for letter in self.word):
                self.message_label.config(text="Congratulations! You've won!", fg="#5cb85c")
        else:
            self.incorrect_guesses += 1
            self.guessed_letters.add(guess)
            self.message_label.config(text="Incorrect guess!", fg="#d9534f")
            self.update_hangman_graphic()
            if self.incorrect_guesses == self.max_incorrect_guesses:
                self.message_label.config(text=f"Game Over! The word was: {self.word}", fg="#d9534f")

    def update_word_display(self):
        """Update the displayed word based on guessed letters."""
        displayed_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_display.set(displayed_word)

# Main
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
