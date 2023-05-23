
"""
Task Option 3 - Cricket
Your program must keep track of the two opposing teams. The user should be able to enter data on a ball-by-ball basis. 
Each ball should result in either a hit (with an amount of runs attached), a wide, a no-ball or a pass ball (with an amount of runs attached). 
The program should keep track of overs, providing indication when it’s time to swap ends. 
It should also keep track of outs, storing the bowler’s name whenever a batter gets out.

"""
import customtkinter as ctk

class TeamInputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1), weight=1)

        # Team 1 Frame
        self.team1_frame = ctk.CTkFrame(self)
        self.team1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.team1_label = ctk.CTkLabel(self.team1_frame, text="Team 1:")
        self.team1_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.team1_entry = ctk.CTkEntry(self.team1_frame)
        self.team1_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.player1_label = ctk.CTkLabel(self.team1_frame, text="Player Names:")
        self.player1_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.player_entries_team1 = []
        for i in range(11):
            label_text_team1 = f"Player {i+1}:"
            entry_team1 = ctk.CTkEntry(self.team1_frame)
            entry_team1.grid(row=i+2, column=0, padx=10, pady=5, sticky="w")
            self.player_entries_team1.append(entry_team1)

        # Team 2 Frame
        self.team2_frame = ctk.CTkFrame(self)
        self.team2_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.team2_label = ctk.CTkLabel(self.team2_frame, text="Team 2:")
        self.team2_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.team2_entry = ctk.CTkEntry(self.team2_frame)
        self.team2_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.player2_label = ctk.CTkLabel(self.team2_frame, text="Player Names:")
        self.player2_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.player_entries_team2 = []
        for i in range(11):
            label_text_team2 = f"Player {i+1}:"
            entry_team2 = ctk.CTkEntry(self.team2_frame)
            entry_team2.grid(row=i+2, column=0, padx=10, pady=5, sticky="w")
            self.player_entries_team2.append(entry_team2)

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


# Example usage
app = ctk.CTk()
team_frame = TeamInputFrame(app)
team_frame.pack(padx=10, pady=10)

app.mainloop()
