import tkinter as tk
from tkinter import ttk
import random
from game_data import DOG_GAMES
import os

class DogGameGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Speel mee met Khyra")
        self.root.geometry("700x600")
        self.root.configure(bg='#E8F4F8')  # Zachte blauwe achtergrond
        
        if os.path.exists("dog_icon.ico"):
            self.root.iconbitmap("dog_icon.ico")
        
        # Hoofdframe met achtergrondkleur
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Style configuratie
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Comic Sans MS', 24, 'bold'), foreground='#4A90E2')
        style.configure('Game.TLabel', font=('Segoe UI', 11), foreground='#2C3E50')
        style.configure('Header.TLabel', font=('Comic Sans MS', 14, 'bold'), foreground='#4A90E2')
        style.configure('Tip.TLabel', font=('Segoe UI', 10, 'italic'), foreground='#6C757D')
        
        # Titel
        title_label = ttk.Label(main_frame, 
                              text="Speel mee met Khyra",
                              style='Title.TLabel')
        title_label.grid(row=0, column=0, pady=20)
        
        # Knop met opmaak
        self.generate_button = tk.Button(main_frame, 
                                       text="Nieuw Spelletje!",
                                       font=('Comic Sans MS', 12, 'bold'),
                                       bg='#4CAF50',
                                       fg='white',
                                       relief='raised',
                                       command=self.generate_game,
                                       padx=20,
                                       pady=10,
                                       cursor='hand2')  # Hand cursor bij hover
        self.generate_button.grid(row=1, column=0, pady=20)
        
        # Display frames met opmaak
        self.game_frame = ttk.LabelFrame(main_frame, 
                                       text="✨ Jouw spelletje ✨", 
                                       padding="15")
        self.game_frame.grid(row=2, column=0, pady=15, sticky=(tk.W, tk.E))
        
        # Labels voor speldetails met opmaak
        self.name_label = ttk.Label(self.game_frame, text="", style='Header.TLabel')
        self.name_label.grid(row=0, column=0, pady=5, sticky=tk.W)
        
        self.desc_label = ttk.Label(self.game_frame, text="", 
                                  wraplength=600, style='Game.TLabel')
        self.desc_label.grid(row=1, column=0, pady=5, sticky=tk.W)
        
        self.details_label = ttk.Label(self.game_frame, text="", style='Game.TLabel')
        self.details_label.grid(row=2, column=0, pady=5, sticky=tk.W)
        
        # Filter frame met nieuwe stijl
        filter_frame = ttk.LabelFrame(main_frame, text="🎯 Kies je spelletje", padding="15")
        filter_frame.grid(row=3, column=0, pady=15, sticky=(tk.W, tk.E))
        
        # Combobox style
        style.configure('TCombobox', font=('Segoe UI', 10))
        style.configure('TLabelframe.Label', font=('Comic Sans MS', 12, 'bold'), foreground='#4A90E2')
        
        # Eerste rij filters
        self.difficulty_var = tk.StringVar(value="Alle")
        ttk.Label(filter_frame, text="Moeilijkheid:", style='Game.TLabel').grid(row=0, column=0, padx=5)
        difficulty_combo = ttk.Combobox(filter_frame, textvariable=self.difficulty_var,
                                      values=["Alle", "Makkelijk", "Gemiddeld", "Moeilijk"],
                                      font=('Segoe UI', 10))
        difficulty_combo.grid(row=0, column=1, padx=5)
        
        self.max_duration_var = tk.StringVar(value="Alle")
        ttk.Label(filter_frame, text="Max. Duur:", style='Game.TLabel').grid(row=0, column=2, padx=5)
        duration_combo = ttk.Combobox(filter_frame, textvariable=self.max_duration_var,
                                    values=["Alle", "5 min", "10 min", "15 min", "20 min"],
                                    font=('Segoe UI', 10))
        duration_combo.grid(row=0, column=3, padx=5)
        
        # Tweede rij filters
        self.type_var = tk.StringVar(value="Alle")
        ttk.Label(filter_frame, text="Type:", style='Game.TLabel').grid(row=1, column=0, padx=5, pady=(10,0))
        type_combo = ttk.Combobox(filter_frame, textvariable=self.type_var,
                                values=["Alle", "Herstel", "Actief"],
                                font=('Segoe UI', 10))
        type_combo.grid(row=1, column=1, padx=5, pady=(10,0))
        
        # Tip label met nieuwe stijl
        self.tip_label = ttk.Label(main_frame, 
                                text="💡 Tip: Kies 'Herstel' voor rustige spelletjes tijdens herstel",
                                style='Tip.TLabel',
                                wraplength=600)
        self.tip_label.grid(row=4, column=0, pady=15)

    def generate_game(self):
        # Voeg subtiel fade effect toe
        self.game_frame.grid_remove()
        self.root.update()
        
        # Filter games based on selected criteria
        filtered_games = DOG_GAMES.copy()
        
        if self.difficulty_var.get() != "Alle":
            filtered_games = [game for game in filtered_games 
                            if game["difficulty"] == self.difficulty_var.get()]
        
        if self.max_duration_var.get() != "Alle":
            max_minutes = int(self.max_duration_var.get().split()[0])
            filtered_games = [game for game in filtered_games 
                            if int(game["duration"].split()[0].split("-")[0]) <= max_minutes]
        
        if self.type_var.get() != "Alle":
            filtered_games = [game for game in filtered_games 
                            if game["type"] == self.type_var.get()]
        
        if not filtered_games:
            self.name_label.config(text="🤔 Geen spelletjes gevonden met deze criteria!")
            self.desc_label.config(text="")
            self.details_label.config(text="")
        else:
            # Select random game from filtered list
            game = random.choice(filtered_games)
            
            # Update display with emoji's
            self.name_label.config(text=f"🎯 {game['name']}")
            self.desc_label.config(text=f"📝 {game['description']}")
            self.details_label.config(
                text=f"\n⏱️ Duur: {game['duration']}\n📊 Moeilijkheid: {game['difficulty']}\n🎮 Type: {game['type']}")
        
        # Toon frame weer met fade effect
        self.game_frame.grid()

def main():
    root = tk.Tk()
    app = DogGameGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()