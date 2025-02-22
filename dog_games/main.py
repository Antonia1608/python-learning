import tkinter as tk
from tkinter import ttk
import random
from game_data import DOG_GAMES

class DogGameGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Honden Spelletjes Generator")
        self.root.geometry("600x400")
        
        # Hoofdframe
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Titel
        title_label = ttk.Label(main_frame, text="🐕 Honden Spelletjes Generator 🎮", 
                              font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=20)
        
        # Knop
        self.generate_button = ttk.Button(main_frame, text="Genereer spelletje!", 
                                        command=self.generate_game)
        self.generate_button.grid(row=1, column=0, pady=10)
        
        # Display frames
        self.game_frame = ttk.LabelFrame(main_frame, text="Jouw spelletje", padding="10")
        self.game_frame.grid(row=2, column=0, pady=10, sticky=(tk.W, tk.E))
        
        # Labels voor speldetails
        self.name_label = ttk.Label(self.game_frame, text="", font=('Helvetica', 12, 'bold'))
        self.name_label.grid(row=0, column=0, pady=5, sticky=tk.W)
        
        self.desc_label = ttk.Label(self.game_frame, text="", wraplength=500)
        self.desc_label.grid(row=1, column=0, pady=5, sticky=tk.W)
        
        self.details_label = ttk.Label(self.game_frame, text="")
        self.details_label.grid(row=2, column=0, pady=5, sticky=tk.W)
        
        # Filter opties
        filter_frame = ttk.LabelFrame(main_frame, text="Filters", padding="10")
        filter_frame.grid(row=3, column=0, pady=10, sticky=(tk.W, tk.E))
        
        self.difficulty_var = tk.StringVar(value="Alle")
        ttk.Label(filter_frame, text="Moeilijkheid:").grid(row=0, column=0, padx=5)
        difficulty_combo = ttk.Combobox(filter_frame, textvariable=self.difficulty_var, 
                                      values=["Alle", "Makkelijk", "Gemiddeld", "Moeilijk"])
        difficulty_combo.grid(row=0, column=1, padx=5)
        
        self.max_duration_var = tk.StringVar(value="Alle")
        ttk.Label(filter_frame, text="Max. Duur:").grid(row=0, column=2, padx=5)
        duration_combo = ttk.Combobox(filter_frame, textvariable=self.max_duration_var,
                                    values=["Alle", "5 min", "10 min", "15 min", "20 min"])
        duration_combo.grid(row=0, column=3, padx=5)

    def generate_game(self):
        # Filter games based on selected criteria
        filtered_games = DOG_GAMES.copy()
        
        if self.difficulty_var.get() != "Alle":
            filtered_games = [game for game in filtered_games 
                            if game["difficulty"] == self.difficulty_var.get()]
        
        if self.max_duration_var.get() != "Alle":
            max_minutes = int(self.max_duration_var.get().split()[0])
            filtered_games = [game for game in filtered_games 
                            if int(game["duration"].split()[0].split("-")[0]) <= max_minutes]
        
        if not filtered_games:
            self.name_label.config(text="Geen spelletjes gevonden met deze criteria!")
            self.desc_label.config(text="")
            self.details_label.config(text="")
            return
        
        # Select random game from filtered list
        game = random.choice(filtered_games)
        
        # Update display
        self.name_label.config(text=game["name"])
        self.desc_label.config(text=game["description"])
        self.details_label.config(
            text=f"\nDuur: {game['duration']}\nMoeilijkheid: {game['difficulty']}")

def main():
    root = tk.Tk()
    app = DogGameGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()