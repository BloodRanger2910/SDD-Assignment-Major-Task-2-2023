
"""
Task Option 3 - Cricket
Your program must keep track of the two opposing teams. The user should be able to enter data on a ball-by-ball basis. 
Each ball should result in either a hit (with an amount of runs attached), a wide, a no-ball or a pass ball (with an amount of runs attached). 
The program should keep track of overs, providing indication when it’s time to swap ends. 
It should also keep track of outs, storing the bowler’s name whenever a batter gets out.

"""
import customtkinter as ctk

class App:
    def __init__(self):
       
        self.app = ctk.CTk()  # Create the application window
        self.app.title("My Cricket Application")  # Set the desired title

        #get screen dimensions
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()

        #set the window size to match the screen
        self.app.geometry(f'{screen_width}x{screen_height}')
        
        # Create the frames for ther application (ADD MORE FRAMES HERE)
        self.team_selection_frame = ctk.CTkFrame(self.app)
        self.main_menu_frame = MainMenuFrame(self.app, self.team_selection_frame)
        self.team_input_frame = TeamInputFrame(self.team_selection_frame)

        self.main_menu_frame.play_button.configure(command=self.switch_to_team_selection)

    def run(self):
        # Display the main menu frame
        self.main_menu_frame.pack(padx=10, pady=10)
        self.app.mainloop()  # Start the application main loop

    def switch_to_team_selection(self):
        # Switch to the team selection frame
        self.main_menu_frame.pack_forget()
        self.team_selection_frame.pack()
        self.team_input_frame.pack(padx=10, pady=10)


class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, master, team_selection_frame):
        super().__init__(master)  # Initialize the parent class
        self.grid_columnconfigure(0, weight=1)
        self.team_selection_frame = team_selection_frame

        # Play button
        self.play_button = ctk.CTkButton(self, text="Play")
        self.play_button.pack(pady=10)

        # How to Use button
        self.how_to_use_button = ctk.CTkButton(self, text="How to Use")
        self.how_to_use_button.pack(pady=10)

        # Quit button
        self.quit_button = ctk.CTkButton(self, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=10)

    def quit_game(self):
        self.master.quit()


class TeamInputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)  # Initialize the parent class
        self.grid_columnconfigure((0, 1), weight=1)

        # Team 1 Frame
        self.team1_frame = ctk.CTkFrame(self)
        self.team1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Team 1 Label and Entry
        self.team1_label = ctk.CTkLabel(self.team1_frame, text="Team 1:")
        self.team1_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")
        self.team1_entry = ctk.CTkEntry(self.team1_frame)
        self.team1_entry.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        self.player1_label = ctk.CTkLabel(self.team1_frame, text="Player Names:")
        self.player1_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.player_entries_team1 = []
        for i in range(11):
            entry_team1 = ctk.CTkEntry(self.team1_frame, placeholder_text=f"Player {i+1}")
            entry_team1.grid(row=i+2, column=0, padx=10, pady=5, sticky="we")
            self.player_entries_team1.append(entry_team1)

        # Team 2 Frame
        self.team2_frame = ctk.CTkFrame(self)
        self.team2_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.team2_label = ctk.CTkLabel(self.team2_frame, text="Team 2:")
        self.team2_label.grid(row=0, column=0, padx=10, pady=10)
        self.team2_entry = ctk.CTkEntry(self.team2_frame, width=250, height=50)
        self.team2_entry.grid(row=0, column=1, padx=10, pady=10)

        self.player2_label = ctk.CTkLabel(self.team2_frame, text="Player Names:")
        self.player2_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.player_entries_team2 = []
        for i in range(11):
            entry_team2 = ctk.CTkEntry(self.team2_frame, placeholder_text=f"Player {i+1}")
            entry_team2.grid(row=i+2, column=0, padx=10, pady=5, sticky="w")
            self.player_entries_team2.append(entry_team2)
    
        self.confirm_button = ctk.CTkButton(self, text="Confirm", command=self.switch_to_scoring_frame)
        self.confirm_button.grid(row=1, column=0, columnspan=2, pady=10)        
            
    def get_team_names(self):
        team1 = self.team1_entry.get()
        team2 = self.team2_entry.get()
        return team1, team2

    def get_player_names(self):
        player_names_team1 = []
        player_names_team2 = []
        for entry_team1, entry_team2 in zip(self.player_entries_team1, self.player_entries_team2):
            name_team1 = entry_team1.get()
            name_team2 = entry_team2.get()
            player_names_team1.append(name_team1)
            player_names_team2.append(name_team2)
        return player_names_team1, player_names_team2

    def switch_to_scoring_frame(self):
        team_names = self.get_team_names()
        player_names = self.get_player_names()
        self.pack_forget()
        scoring_frame = ScoringFrame(self.master, team_names, player_names)
        scoring_frame.pack(padx=10, pady=10)


class ScoringFrame(ctk.CTkFrame):
    def __init__(self, master, team_names, player_names):
        super().__init__(master)
        self.team_names = team_names
        self.player_names = player_names

        self.team_label = ctk.CTkLabel(self, text=f"Teams: {team_names[0]} vs {team_names[1]}")
        self.team_label.pack(pady=10)

        self.player_label = ctk.CTkLabel(self, text=f"Players: {player_names[0]} vs {player_names[1]}")
        self.player_label.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.switch_to_team_input_frame)
        self.back_button.pack(pady=10)

    def switch_to_team_input_frame(self):
        self.pack_forget()
        team_input_frame = TeamInputFrame(self.master)
        team_input_frame.pack(padx=10, pady=10)


# Create and run the application
app = App()
app.run()