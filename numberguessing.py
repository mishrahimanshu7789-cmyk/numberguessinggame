import random
import tkinter as tk
from tkinter import messagebox

MIN_NUM = 1
MAX_NUM = 100
MAX_ATTEMPTS = 7


class GuessingGame:
    def __init__(self, root):
        self.root = root
        root.title("Number Guessing Game")
        root.geometry("360x320")
        root.resizable(False, False)

        tk.Label(root, text="Number Guessing Game",
                 font=("Helvetica", 16, "bold")).pack(pady=(15, 5))
        tk.Label(root, text=f"I'm thinking of a number between {MIN_NUM} and {MAX_NUM}.",
                 font=("Helvetica", 10)).pack()

        self.entry = tk.Entry(root, font=("Helvetica", 14), justify="center", width=10)
        self.entry.pack(pady=15)
        self.entry.bind("<Return>", lambda e: self.check_guess())

        self.guess_btn = tk.Button(root, text="Guess", width=12, command=self.check_guess)
        self.guess_btn.pack()

        self.message = tk.Label(root, text="Make your first guess!",
                                font=("Helvetica", 12), wraplength=320)
        self.message.pack(pady=15)

        self.attempts_label = tk.Label(root, font=("Helvetica", 10))
        self.attempts_label.pack()

        self.history_label = tk.Label(root, font=("Helvetica", 9), fg="gray", wraplength=320)
        self.history_label.pack(pady=5)

        tk.Button(root, text="New Game", width=12, command=self.new_game).pack(pady=10)

        self.new_game()

    def new_game(self):
        self.secret = random.randint(MIN_NUM, MAX_NUM)
        self.attempts = 0
        self.history = []
        self.message.config(text="Make your first guess!", fg="black")
        self.history_label.config(text="")
        self.update_attempts()
        self.guess_btn.config(state="normal")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def update_attempts(self):
        left = MAX_ATTEMPTS - self.attempts
        self.attempts_label.config(text=f"Attempts left: {left}")

    def end_game(self):
        self.guess_btn.config(state="disabled")
        self.entry.config(state="disabled")

    def check_guess(self):
        text = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        try:
            guess = int(text)
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a whole number.")
            return

        if not MIN_NUM <= guess <= MAX_NUM:
            messagebox.showwarning("Out of range",
                                   f"Enter a number between {MIN_NUM} and {MAX_NUM}.")
            return

        self.attempts += 1
        self.history.append(guess)
        self.history_label.config(text="Guesses: " + ", ".join(map(str, self.history)))
        self.update_attempts()

        if guess == self.secret:
            self.message.config(
                text=f"🎉 Correct! You got it in {self.attempts} "
                     f"attempt{'s' if self.attempts != 1 else ''}.",
                fg="green")
            self.end_game()
        elif self.attempts >= MAX_ATTEMPTS:
            self.message.config(text=f"Game over! The number was {self.secret}.", fg="red")
            self.end_game()
        elif guess < self.secret:
            self.message.config(text="Too low! Try higher ⬆️", fg="blue")
        else:
            self.message.config(text="Too high! Try lower ⬇️", fg="orange")


if __name__ == "__main__":
    root = tk.Tk()
    GuessingGame(root)
    root.mainloop()