import tkinter as tk
import random
import time

class ReactionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaction Time Game in python")

        self.instructions_label = tk.Label(
            root, 
            text="Click the button as soon as hit button turns green!", 
            font=("Helvetica", 16)
        )
        self.instructions_label.pack(pady=20)

        self.start_button = tk.Button(
            root, 
            text="test your reaction time[start]", 
            font=("Helvetica", 16), 
            command=self.start_game
        )
        self.start_button.pack(pady=20)

        self.game_button = tk.Button(
            root, 
            text="hit Me!", 
            font=("Helvetica", 16), 
            state=tk.DISABLED, 
            command=self.record_reaction
        )
        self.game_button.pack(pady=20)

        self.reaction_time_label = tk.Label(
            root, 
            text="", 
            font=("Helvetica", 16)
        )
        self.reaction_time_label.pack(pady=20)

        self.start_time = None
        self.reaction_time = None

    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.reaction_time_label.config(text="")
        self.game_button.config(bg="red", state=tk.DISABLED)
        delay = random.randint(2000, 5000)
        self.root.after(delay, self.change_button_color)

    def change_button_color(self):
        self.game_button.config(bg="green", state=tk.NORMAL)
        self.start_time = time.time()

    def record_reaction(self):
        if self.start_time:
            self.reaction_time = time.time() - self.start_time
            self.reaction_time_label.config(
                text=f"Your reaction time is {self.reaction_time:.3f} seconds very nice, hit the start button to try again.."
            )
        self.start_button.config(state=tk.NORMAL)
        self.game_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = ReactionGame(root)
    root.mainloop()
