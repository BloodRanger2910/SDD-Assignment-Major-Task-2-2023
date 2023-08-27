"""
Task Option 3 - Cricket
Your program must keep track of the two opposing teams. The user should be able to enter data on a ball-by-ball basis. 
Each ball should result in either a hit (with an amount of runs attached), a wide, a no-ball or a pass ball (with an amount of runs attached). 
The program should keep track of overs, providing indication when it’s time to swap ends. 
It should also keep track of outs, storing the bowler’s name whenever a batter gets out.

"""
import customtkinter as ctk
import random
from tkinter import messagebox as msg
from tkinter import *

class App(ctk.CTk): 

    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)  # Create the application window
        self.title("My Cricket Application")  # Set the desired title
    
        #get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        #set the window size to match the screen
        self.geometry(f'{screen_width}x{screen_height}')
        self.resizable(False, False)
        
        app = ctk.CTkFrame(self) #first frame, fills root window, parent of all other frames/screens
        app.pack(side="top", fill="both", expand=True)
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)

        self.frames["MainMenuFrame"] = MainMenuFrame(parent=app, controller=self)
        self.frames["TeamInputFrame"] = TeamInputFrame(parent=app, controller=self)
        self.frames["TeamReviewFrame"] = TeamReviewFrame(parent=app, controller=self)

        self.frames["MainMenuFrame"].grid(row=0, column=0, sticky="nsew")
        self.frames["TeamInputFrame"].grid(row=0, column=0, sticky="nsew")
        self.frames["TeamReviewFrame"].grid(row=0, column=0, sticky="nsew")
        
        # shows startscreen first (when __init__ runs)
        self.show_frame("MainMenuFrame")
    
    # brings the parsed frame to the top (ie changes the displayed screen)
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainMenuFrame(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller        
        # Play button
        play_button = ctk.CTkButton(self, text="Play",
                                    command=lambda: controller.show_frame("TeamInputFrame"))
        play_button.pack(pady=10)

        # How to Use button
        how_to_use_button = ctk.CTkButton(self, text="How to Use")
        how_to_use_button.pack(pady=10)

        # Quit button
        quit_button = ctk.CTkButton(self, text="Quit", 
                                    command=lambda: self.closeprogram())
        quit_button.pack(pady=10)
    
    def closeprogram(self):
        close = msg.askyesno(title="Close Now?", message="Are you sure?")
        if close == True:
            self.quit()

class TeamInputFrame(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Team 1 Frame
        team1_frame = ctk.CTkFrame(self)
        team1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Team 1 Label and Entry
        team1_label = ctk.CTkLabel(team1_frame, text="Team 1:", )
        team1_label.grid(row=0, column=0, padx=5, pady=10)   
        team1_label.configure(font=("Arial", 30))
        team1_entry = ctk.CTkEntry(team1_frame, width=250, height=50)
        team1_entry.grid(row=0, column=1, padx=5, pady=10)

        player1_label = ctk.CTkLabel(self.team1_frame, text="Player Names:")
        player1_label.configure(font=("Arial", 30))
        player1_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        global player_entries_team1
        player_entries_team1 = []
        for i in range(11):
            entry_team1 = ctk.CTkEntry(team1_frame, placeholder_text=f"Player {i+1}", width=250)
            entry_team1.grid(row=i+2, column=0, columnspan=2, padx=10, pady=5, sticky="we")
            player_entries_team1.append(entry_team1)

        # Team 2 Frame
        team2_frame = ctk.CTkFrame(self)
        team2_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Team 2 Label and Entry
        team2_label = ctk.CTkLabel(team2_frame, text="Team 2:")
        team2_label.grid(row=0, column=0, padx=10, pady=10)
        team2_label.configure(font=("Arial", 30))
        team2_entry = ctk.CTkEntry(team2_frame, width=250, height=50)
        team2_entry.grid(row=0, column=1, padx=10, pady=10)

        player2_label = ctk.CTkLabel(team2_frame, text="Player Names:")
        player2_label.configure(font=("Arial", 30))
        player2_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        global player_entries_team2
        player_entries_team2 = []
        for i in range(11):
            entry_team2 = ctk.CTkEntry(team2_frame, width=30, placeholder_text=f"Player {i+1}")
            entry_team2.grid(row=i+2, column=0, columnspan=2, padx=10, pady=5, sticky="we")
            player_entries_team2.append(entry_team2)


        confirm_button = ctk.CTkButton(self, text="Confirm", 
                                       command=lambda: controller.show_frame("TeamReviewFrame"))
        confirm_button.grid(row=1, column=0, columnspan=2, pady=10)   
            
    def closeprogram(self, controller):
        self.controller = controller
        go = msg.askokcancel(title="Confirm?", message="Confirm Names?")
        if go:
            controller.show_frame("TeamReviewFrame")
            
    def get_team_names(self):
        team1 = self.team1_entry.get()
        team2 = self.team2_entry.get()
        return team1, team2

    def get_player_names(self):
        player_names_team1 = []
        player_names_team2 = []
        for entry_team1, entry_team2 in zip(player_entries_team1, player_entries_team2):
            name_team1 = entry_team1.get()
            name_team2 = entry_team2.get()
            player_names_team1.append(name_team1)
            player_names_team2.append(name_team2)
        return player_names_team1, player_names_team2
class TeamReviewFrame(ctk.CTkFrame):
    def __init__(self, parent, team_names, player_names):
        super().__init__(parent)


        self.team_label = ctk.CTkLabel(self, text=f"Teams: {team_names[0]} vs {team_names[1]}")
        self.team_label.pack(pady=10)

        self.player_label = ctk.CTkLabel(self, text=f"Players: {player_names[0]} vs {player_names[1]}")
        self.player_label.pack(pady=10)

#        self.back_button = ctk.CTkButton(self, text="Back", command=)
#        self.back_button.pack(pady=10)
#
#        self.next_button = ctk.CTkButton(self, text="Next", command=)
#        self.next_button.pack(pady=10)

#class TossFrame(ctk.CTkFrame):
#    def __init__(self, parent, team_names):
#        super().__init__(parent)
#
#        self.toss_label = ctk.CTkLabel(self, text="Toss Time! Click the button to determine batting and bowling teams.")
#        self.toss_label.pack(pady=10)
#
#        self.toss_button = ctk.CTkButton(self, text="Toss", command=self.perform_toss)
#        self.toss_button.pack(pady=10)
#
#        self.result_label = ctk.CTkLabel(self, text="")
#        self.result_label.pack(pady=10)
#
#    def perform_toss(self):
#        batting_team = random.choice(self.team_names)
#        bowling_team = self.team_names[0] if batting_team != self.team_names[0] else self.team_names[1]
#        toss_result = f"{batting_team} won the toss and chose to bat.\n{bowling_team} will be bowling."
#        self.result_label.configure(text=toss_result)

# Create and run the application
app = App()
app.mainloop()