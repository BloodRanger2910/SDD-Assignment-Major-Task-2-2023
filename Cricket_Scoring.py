# Import necessary libraries
import customtkinter as ctk
import random
from tkinter import messagebox as msg
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

# Define the main application class
class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Cricket Scoring")
        self.geometry("900x700")
        self.resizable(False, False)
        self.iconbitmap(("Assest\Cricket_Icon.ico"))
        self._frame = None
        global TeamTabs
        TeamTabs = None

        # Call switch_frame to show the MainMenuFrame initially
        self.switch_frame(MainMenuFrame)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

# Define the MainMenuFrame class
class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        # Main menu image
        MainMenuLogo = ctk.CTkImage(dark_image=Image.open(("Assets\Cricket_Logo.png")), size=(400, 400))
        MainMenu = ctk.CTkLabel(self, image=MainMenuLogo, text="")
        MainMenu.pack(padx=50)

        # Play button
        play_button = ctk.CTkButton(self, height=75, width=375, corner_radius=40,
                                    text="Play", command=lambda: master.switch_frame(TeamInputFrame))
        play_button.pack(pady=10)

        # Quit button
        quit_button = ctk.CTkButton(self, height=75, width=375, corner_radius=40,
                                    text="Quit", command=self.close_program)
        quit_button.pack(pady=10)

    def close_program(self):
        close = msg.askyesno(title="Close Now?", message="Are you sure?")
        if close:
            self.master.destroy()

# Define the TeamInputFrame class
class TeamInputFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master, width=900, height=700)
        global playername_entries_team1
        playername_entries_team1 = []
        global playername_entries_team2
        playername_entries_team2 = []
        global team1name_entry
        global team2name_entry
        
        # Team 1 and 2 Frame
        team1_frame = ctk.CTkFrame(self)
        team1_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        team2_frame = ctk.CTkFrame(self)
        team2_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
       # Set row and column weights for resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        

        # Team 1 Name and Player Entry
        team1_label = ctk.CTkLabel(team1_frame, text="Team 1:", )
        team1_label.grid(row=0, column=0, padx=5, pady=10)   
        team1_label.configure(font=("Arial", 30))
        team1name_entry = ctk.CTkEntry(team1_frame, placeholder_text="Team 1 Name", 
                                       width=250, 
                                       height=50,
                                       font=("Arial", 20))
        team1name_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        player1_label = ctk.CTkLabel(team1_frame, text="Player Names:")
        player1_label.configure(font=("Arial", 30))
        player1_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        for i in range(11):
            entry_team1 = ctk.CTkEntry(team1_frame, placeholder_text=f"Player Name {i+1}", width=250)
            entry_team1.grid(row=i+2, column=0, columnspan=2, padx=10, pady=5)
            entry_team1.configure(width=425) 
            playername_entries_team1.append(entry_team1)

        # Team 2 Label and Entry
        team2_label = ctk.CTkLabel(team2_frame, text="Team 2:")
        team2_label.grid(row=0, column=0, padx=10, pady=10)
        team2_label.configure(font=("Arial", 30))
        team2name_entry = ctk.CTkEntry(team2_frame, placeholder_text="Team 2 Name",
                                       width=250, 
                                       height=50,
                                       font=("Arial", 20))
        team2name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        player2_label = ctk.CTkLabel(team2_frame, text="Player Names:")
        player2_label.configure(font=("Arial", 30))
        player2_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        for i in range(11):
            entry_team2 = ctk.CTkEntry(team2_frame, width=30, placeholder_text=f"Player Name {i+1}")
            entry_team2.grid(row=i+2, column=0, columnspan=2, padx=10, pady=5)
            entry_team2.configure(width=425) 
            playername_entries_team2.append(entry_team2)

        confirm_button = ctk.CTkButton(self, text="Confirm", 
                               command=lambda: self.confirmnames())
        confirm_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="nsew") 
        self.update() 
        confirm_button.configure(height=100) 


def confirmnames(self):
    # Ask for confirmation using a dialog
    go = msg.askokcancel(title="Confirm?", message="Confirm Names?")
    if go:
        # Initialize lists to store player names and team names
        global Team1Players
        Team1Players = []
        global Team2Players
        Team2Players = []

        # Collect player names from the input fields for both teams
        for entry in playername_entries_team1:
            Team1Players.append(entry.get())
        for entry in playername_entries_team2:
            Team2Players.append(entry.get())

        # Collect team names from the input fields
        global Team1Name
        Team1Name = team1name_entry.get()
        global Team2Name
        Team2Name = team2name_entry.get()

        # Check if team names are empty and display an error if so
        if Team1Name == "" or Team2Name == "":
            msg.showerror(title="Invalid!",
                          message="The Team Name entry fields are empty.\nPlease check that all fields have been filled in.")
            return

        # Check if player names for both teams are empty and display an error if so
        for member in Team1Players:
            if member == "":
                msg.showerror(title="Invalid!",
                              message="One or more entry fields under Team 1's Players are empty.\nPlease check that all fields have been filled in.")
                return
        for member in Team2Players:
            if member == "":
                msg.showerror(title="Error",
                              message="One or more entry fields under Team 2's Players are empty.\nPlease check that all fields have been filled in.")
                return

        # Switch to the ScoringFrame to proceed
        self.master.switch_frame(ScoringFrame)

# Define the ScoringFrame class
class ScoringFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master, width=900, height=700)
        
        # Store player names and team names for easier access
        global player1names
        player1names = Team1Players
        global player2names
        player2names = Team2Players
        global team1name
        team1name = Team1Name
        global team2name
        team2name = Team2Name
        
        # Display team names
        self.team_label = ctk.CTkLabel(self, text=f"Teams: {team1name} vs {team2name}")
        self.team_label.pack(pady=10)
        
        # Display player names for both teams
        self.player_label = ctk.CTkLabel(self, text=f"Team 1 Players: {player1names} \nvs \nTeam 2 Players: {player2names}")
        self.player_label.pack(pady=10)
        
        # Continue button to move to the next frame (TossFrame)
        Continue = ctk.CTkButton(self, text="Continue",
                                    command=lambda: master.switch_frame(TossFrame))
        Continue.pack(pady=10)

# Define the TossFrame class
class TossFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master, width=900, height=700)
        
        # Retrieve team names
        global team1name
        team1name = Team1Name
        global team2name
        team2name = Team2Name
        
        # Display toss-related instructions
        self.toss_label = ctk.CTkLabel(self, text="Toss Time! Click the button to determine batting and bowling teams.")
        self.toss_label.pack(pady=10)

        # Button to perform the toss
        self.toss_button = ctk.CTkButton(self, text="Toss", command=self.perform_toss)
        self.toss_button.pack(pady=10)

        # Label to display the toss result
        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)

        # Initialize the Continue button but keep it hidden initially
        self.continue_button = ctk.CTkButton(self, text="Continue",
                                             command=lambda: master.switch_frame(ScoringGameFrame))
        self.continue_button.pack(pady=10)
        self.continue_button.pack_forget()  # Hide the button initially
        
    def perform_toss(self):
        # Variables to store batting and bowling teams
        global batting_team
        global bowling_team
        
        # Determine the tossing team randomly
        tossing_team = Team1Name if random.choice([True, False]) else Team2Name
        
        # Ask for batting or bowling choice
        choice = msg.askyesno("Toss Result", f"{tossing_team} won the toss!\nDo you want to bowl?")
        
        # Assign teams based on choice
        if choice:  # Yes means they want to bowl
            batting_team, bowling_team = Team1Name if tossing_team == Team2Name else Team2Name, tossing_team
        else:  # No means they want to bat
            batting_team, bowling_team = tossing_team, Team1Name if tossing_team == Team2Name else Team2Name
        
        # Display the toss result
        toss_result = f"{tossing_team} won the toss and chose to {'bowl' if choice else 'bat'}.\n{bowling_team} will be bowling.\n{batting_team} will be batting."
        self.result_label.configure(text=toss_result)
        
        # Show the Continue button
        self.continue_button.pack()
        
        # Hide the Toss Button
        self.toss_button.pack_forget()
               
# Define the ScoringGameFrame class
class ScoringGameFrame(ctk.CTkFrame):
    def __init__(self, master):
        # Initialize various attributes related to scoring and game progress
        global team1name, team2name, player1names, player2names, batting_team, bowling_team, TeamTabs
        self.tab1batting_team = batting_team
        self.tab1bowling_team = bowling_team
        self.t1battersOut = []
        self.t1player_runs = {}  # Dictionary to store player runs
        self.t1player_balls = {}  # Dictionary to store player balls
        self.t1wideBalls = 0
        self.t1teamNoBalls = 0
        self.t1runs = 0  # Initialize the 'runs' attribute
        self.t1balls = 0  # Initialize the 'balls' attribute
        self.t1current_batter = None
        self.t1current_bowler = None
        self.t1current_over_balls = 0
        self.t1overs = 0
        self.t1totalBalls = 0
        self.t1teamRuns = 0
        self.t1teamWickets = 0

        self.tab2batting_team = bowling_team
        self.tab2bowling_team = batting_team
        self.t2battersOut = []
        self.t2player_runs = {}  # Dictionary to store player runs
        self.t2player_balls = {}  # Dictionary to store player balls
        self.t2wideBalls = 0
        self.t2teamNoBalls = 0
        self.t2runs = 0  # Initialize the 'runs' attribute
        self.t2balls = 0  # Initialize the 'balls' attribute
        self.t2current_batter = None
        self.t2current_bowler = None
        self.t2current_over_balls = 0
        
        self.t2overs = 0
        self.t2totalBalls = 0
        self.t2teamRuns = 0
        self.t2teamWickets = 0
        
        # Call the superclass constructor to create the frame
        ctk.CTkFrame.__init__(self, master, width=900, height=700)
        # Create a tabbed view to display batting and bowling teams' information
        TeamTabs = ctk.CTkTabview(master=self)
        TeamTabs.pack(padx=20, pady=5, expand=True, fill=tk.BOTH)
        Team1Tab = TeamTabs.add(self.tab1batting_team)
        Team2Tab = TeamTabs.add(self.tab1bowling_team)
        
        # Display labels for batting and bowling teams
        self.t1batting_label = ctk.CTkLabel(Team1Tab, text=f"Batting Team: {self.tab1batting_team}")
        self.t1batting_label.pack(pady=10)
        self.t1bowling_label = ctk.CTkLabel(Team1Tab, text=f"Bowling Team: {self.tab1bowling_team}")
        self.t1bowling_label.pack(pady=10)

        # Display labels for runs, balls, extras, overs, and more
        self.t1runs_label = ctk.CTkLabel(Team1Tab, text=f"Runs: {self.t1runs}")
        self.t1runs_label.pack(pady=10)
        self.t1balls_label = ctk.CTkLabel(Team1Tab, text=f"Balls: {self.t1runs}")
        self.t1balls_label.pack(pady=10)
        self.t1wide_label = ctk.CTkLabel(Team1Tab, text=f"Wides: {self.t1wideBalls}")
        self.t1wide_label.pack(pady=10)
        self.t1overs_label = ctk.CTkLabel(Team1Tab, text=f"Overs: {self.t1overs}")
        self.t1overs_label.pack(pady=10)
        
        # Create dictionaries to store player runs and balls
        for player in player1names + player2names:
            self.t1player_runs[player] = 0
            self.t1player_balls[player] = 0
        
        # Display labels for selecting current batter and bowler
        self.batter_label = ctk.CTkLabel(Team1Tab, text="Select Batter:")
        self.batter_label.pack(pady=5)
        self.batter_selection = ctk.CTkComboBox(Team1Tab, values=player1names if self.tab1batting_team == team1name else player2names)
        self.batter_selection.pack(pady=5)
        
        self.bowler_label = ctk.CTkLabel(Team1Tab, text="Select Bowler:")
        self.bowler_label.pack(pady=5)
        self.bowler_selection = ctk.CTkComboBox(Team1Tab, values=player1names if self.tab1bowling_team == team1name else player2names)
        self.bowler_selection.pack(pady=5)
        
        # Bind events to update selected batter and bowler
        self.batter_selection.bind("<<ComboboxSelected>>", self.update_current_batter)
        self.bowler_selection.bind("<<ComboboxSelected>>", self.update_current_bowler)
        
        # Create buttons for adding runs, no balls, wides, wickets, and ending the game for Team1Tab
        run_buttons_frame = ctk.CTkFrame(Team1Tab, fg_color="transparent")
        run_buttons_frame.pack(pady=10)
        
        # Create buttons for adding runs 1-6 for Team1Tab
        for i in range(1, 7):
            run_buttons_frame.grid_columnconfigure(i, weight=1)
            run_button = ctk.CTkButton(run_buttons_frame, text=str(i), command=lambda i=i: self.add_runs(i))
            run_button.grid(row=0, column=i, padx=2, pady=2)
            
        # Create buttons for removing runs 1-6 for Team1Tab
        for i in range(1, 7):
            run_buttons_frame.grid_columnconfigure(i, weight=1)
            run_button = ctk.CTkButton(run_buttons_frame, text=str(i), command=lambda i=i: self.remove_runs(i))
            run_button.grid(row=1, column=i, padx=2, pady=2)
        
        # Display labels for run-related actions in Team1Tab
        tab1runsLabel = ctk.CTkLabel(run_buttons_frame, text="Add Runs:")
        tab1runsLabel.grid(row=0, column=0)
        tab1runsRemoveLabel = ctk.CTkLabel(run_buttons_frame, text="Remove Runs:")
        tab1runsRemoveLabel.grid(row=1, column=0)
        tab1extrasLabel = ctk.CTkLabel(run_buttons_frame, text="Extras:")
        tab1extrasLabel.grid(row=2, column=0)
        tab1wicketLabel = ctk.CTkLabel(run_buttons_frame, text="Wicket:")
        tab1wicketLabel.grid(row=3, column=0)
        tab1endgame = ctk.CTkLabel(run_buttons_frame, text="EndGame:")
        tab1endgame.grid(row=4, column=0)
        
        # Create buttons for no ball, wide, and wicket in Team1Tab
        no_ball_button = ctk.CTkButton(run_buttons_frame, text="No Ball", command=self.add_no_ball)
        no_ball_button.grid(row=2, column=1, padx=2, pady=2)

        wide_button = ctk.CTkButton(run_buttons_frame, text="Wide", command=self.add_wide)
        wide_button.grid(row=2, column=2, padx=2, pady=2)

        wicket_button = ctk.CTkButton(run_buttons_frame, text="Wicket", command=self.record_wicket)
        wicket_button.grid(row=3, column=1, padx=2, pady=2)
        
        # Create the "End Game" button for Team1Tab
        self.end_game_button = ctk.CTkButton(run_buttons_frame, text="End Game", command=self.display_end_game_results)
        self.end_game_button.grid(row=4, column=1, pady=10)
    
        # Display Batting and Bowling Team Labels for Team2Tab
        self.t2batting_label = ctk.CTkLabel(Team2Tab, text=f"Batting Team: {self.tab1batting_team}")
        self.t2batting_label.pack(pady=10)
        self.t2bowling_label = ctk.CTkLabel(Team2Tab, text=f"Bowling Team: {self.tab1bowling_team}")
        self.t2bowling_label.pack(pady=10)
    
        # Display Runs and Balls Labels for Team2Tab
        self.t2runs_label = ctk.CTkLabel(Team2Tab, text=f"Runs: {self.t2runs}")
        self.t2runs_label.pack(pady=10)
        self.t2balls_label = ctk.CTkLabel(Team2Tab, text=f"Balls: {self.t2runs}")
        self.t2balls_label.pack(pady=10)
        self.t2no_label = ctk.CTkLabel(Team2Tab, text=f"No Balls: {self.t2teamNoBalls}")
        self.t2no_label.pack(pady=10)
        self.t2wide_label = ctk.CTkLabel(Team2Tab, text=f"Wides: {self.t2wideBalls}")
        self.t2wide_label.pack(pady=10)
        self.t2overs_label = ctk.CTkLabel(Team2Tab, text=f"Overs: {self.t2overs}")
        self.t2overs_label.pack(pady=10)
        
        # Initialize player_runs and player_balls dictionaries for Team2Tab
        for player in player1names + player2names:
            self.t2player_runs[player] = 0
            self.t2player_balls[player] = 0

        # Labels next to player selection ComboBoxes for Team2Tab
        self.t2batter_label = ctk.CTkLabel(Team2Tab, text="Select Batter:")
        self.t2batter_label.pack(pady=5)
        self.t2batter_selection = ctk.CTkComboBox(Team2Tab, values=player1names if self.tab1batting_team == team1name else player2names)
        self.t2batter_selection.pack(pady=5)
        
        self.t2bowler_label = ctk.CTkLabel(Team2Tab, text="Select Bowler:")
        self.t2bowler_label.pack(pady=5)
        self.t2bowler_selection = ctk.CTkComboBox(Team2Tab, values=player1names if self.tab1bowling_team == team1name else player2names)
        self.t2bowler_selection.pack(pady=5)
        
        # Bind the ComboboxSelected event to update selected batter and bowler for Team2Tab
        self.t2batter_selection.bind("<<ComboboxSelected>>", self.tab2update_current_batter)
        self.t2bowler_selection.bind("<<ComboboxSelected>>", self.tab2update_current_bowler)
        
        # Buttons for Runs and Actions for Team2Tab
        tab2run_buttons_frame = ctk.CTkFrame(Team2Tab, fg_color="transparent")
        tab2run_buttons_frame.pack(pady=10)

        for i in range(1, 7):
            tab2run_buttons_frame.grid_columnconfigure(i, weight=1)
            run_button = ctk.CTkButton(tab2run_buttons_frame, text=str(i), command=lambda i=i: self.tab2add_runs(i))
            run_button.grid(row=0, column=i, padx=2, pady=2)
            
        for i in range(1, 7):
            tab2run_buttons_frame.grid_columnconfigure(i, weight=1)
            run_button = ctk.CTkButton(tab2run_buttons_frame, text=str(i), command=lambda i=i: self.tab2remove_runs(i))
            run_button.grid(row=1, column=i, padx=2, pady=2)
            
        # Display labels for run-related actions in Team2Tab
        tab2runsLabel = ctk.CTkLabel(tab2run_buttons_frame, text="Add Runs:")
        tab2runsLabel.grid(row=0, column=0)
        tab2runsRemoveLabel = ctk.CTkLabel(tab2run_buttons_frame, text="Remove Runs:")
        tab2runsRemoveLabel.grid(row=1, column=0)
        tab2extrasLabel = ctk.CTkLabel(tab2run_buttons_frame, text="Extras:")
        tab2extrasLabel.grid(row=2, column=0)
        tab2wicketLabel = ctk.CTkLabel(tab2run_buttons_frame, text="Wicket:")
        tab2wicketLabel.grid(row=3, column=0)

        # Create buttons for adding runs, no balls, wides, wickets, and ending the game for Team2Tab
        tab2run_buttons_frame = ctk.CTkFrame(Team2Tab, fg_color="transparent")
        tab2run_buttons_frame.pack(pady=10)
        
        # Create buttons for adding no ball, wide, and wicket in Team2Tab
        no_ball_button = ctk.CTkButton(tab2run_buttons_frame, text="No Ball", command=self.tab2add_no_ball)
        no_ball_button.grid(row=2, column=1, padx=2, pady=2)

        wide_button = ctk.CTkButton(tab2run_buttons_frame, text="Wide", command=self.tab2add_wide)
        wide_button.grid(row=2, column=2, padx=2, pady=2)

        wicket_button = ctk.CTkButton(tab2run_buttons_frame, text="Wicket", command=self.tab2record_wicket)
        wicket_button.grid(row=3, column=1, padx=2, pady=2)
        
        # Add the "End Game" button for Team2Tab
        self.end_game_button = ctk.CTkButton(tab2run_buttons_frame, text="End Game", command=self.display_end_game_results)
        self.end_game_button.grid(row=3, column=6, padx=2, pady=2)

    def display_end_game_results(self):
        # Create a new frame for displaying end game results
        end_game_frame = ctk.CTkToplevel(self)
        end_game_frame.title("End Game Results")
        end_game_frame.geometry("300x600")

        # Display game results for Team 1
        team1_results_label = ctk.CTkLabel(end_game_frame, text="Team 1 Results")
        team1_results_label.pack(pady=10)

        team1_runs_label = ctk.CTkLabel(end_game_frame, text=f"Runs: {self.t1runs}/{self.t1teamWickets}")
        team1_runs_label.pack(pady=5)

        team1_overs_label = ctk.CTkLabel(end_game_frame, text=f"Overs: {self.t1overs}.{self.t1current_over_balls}")
        team1_overs_label.pack(pady=5)

        # Display game results for Team 2
        team2_results_label = ctk.CTkLabel(end_game_frame, text="Team 2 Results")
        team2_results_label.pack(pady=10)

        team2_runs_label = ctk.CTkLabel(end_game_frame, text=f"Runs: {self.t2runs}/{self.t2teamWickets}")
        team2_runs_label.pack(pady=5)

        team2_overs_label = ctk.CTkLabel(end_game_frame, text=f"Overs: {self.t2overs}.{self.t2current_over_balls}")
        team2_overs_label.pack(pady=5)

    def add_runs(self, runs):
        # Update runs and balls for the current batter
        if self.t1current_batter:
            self.t1player_runs[self.t1current_batter] += 1
            self.t1player_balls[self.t1current_batter] += 1
        self.t1runs += runs
        self.t1balls += 1
        self.t1current_over_balls += 1
        if self.t1current_over_balls == 6:
            self.t1overs += 1
            self.t1current_over_balls = 0
        self.update_display()

    def remove_runs(self, runs):
        # Update runs and balls for the current batter
        if self.t1current_batter:
            self.t1player_runs[self.t1current_batter] -= 1
            self.t1player_balls[self.t1current_batter] -= 1
        self.t1runs -= runs
        self.t1balls -= 1
        self.update_display()

    def add_no_ball(self):
        # Update runs and balls for the current batter in Team1Tab
        if self.t1current_batter:
            self.t1player_runs[self.t1current_batter] += 1
            self.t1player_balls[self.t1current_batter] += 1
        self.t1runs += 1
        self.t1balls += 1
        self.t1teamNoBalls += 1
        self.update_display()

    def add_wide(self):
        self.t1runs += 1
        self.t1balls += 1
        self.t1wideBalls += 1
        self.update_display()

    def record_wicket(self):
        self.t1teamWickets += 1
        self.update_display()
        
    def update_current_batter(self, event):
        self.tab1current_batter = self.batter_selection.get()
        if self.tab1current_batter:
            self.update_display()

    def update_current_bowler(self, event):
        self.tab1current_bowler = self.bowler_selection.get()
        if self.tab1current_bowler:
            self.update_display()

    def remove_batter(self):
        if self.t1current_batter in player1names:
            player1names.remove(self.t1current_batter)
        if self.t1current_batter in player2names:
            player2names.remove(self.t1current_batter)

    def update_display(self):
        self.t1batting_label.configure(text=f"Batting Team: {self.tab1batting_team}")
        self.t1bowling_label.configure(text=f"Bowling Team: {self.tab1bowling_team}")
        self.t1runs_label.configure(text=f"Runs: {self.t1runs}")
        self.t1balls_label.configure(text=f"Balls: {self.t1balls}")
        self.t1no_label.configure(text=f"No Balls: {self.t1teamNoBalls}")
        self.t1wide_label.configure(text=f"Wides: {self.t1wideBalls}")
        self.t1overs_label.configure(text=f"Overs: {self.t1overs}.{self.t1current_over_balls}")
        
    def tab2add_runs(self, runs):
        # Update runs and balls for the current batter in Team2Tab
        if self.t2current_batter:
            self.t2player_runs[self.t2current_batter] += runs
            self.t2player_balls[self.t2current_batter] += 1
        self.t2runs += runs
        self.t2balls += 1
        self.t2current_over_balls += 1
        if self.t2current_over_balls == 6:
            self.t2overs += 1
            self.t2current_over_balls = 0
        self.tab2update_display()

    def tab2remove_runs(self, runs):
        # Update runs and balls for the current batter in Team2Tab
        if self.t2current_batter:
            self.t2player_runs[self.t2current_batter] -= runs
            self.t2player_balls[self.t2current_batter] -= 1
        self.t2runs -= runs
        self.t2balls -= 1
        self.tab2update_display()

    def tab2add_no_ball(self):
        # Update runs and balls for the current batter in Team2Tab
        if self.t2current_batter:
            self.t2player_runs[self.t2current_batter] += 1
            self.t2player_balls[self.t2current_batter] += 1
        self.t2runs += 1
        self.t2balls += 1
        self.t2teamNoBalls += 1
        self.tab2update_display()

    def tab2add_wide(self):
        self.t2runs += 1
        self.t2balls += 1
        self.t2wideBalls += 1
        self.tab2update_display()

    def tab2record_wicket(self):
        self.t2teamWickets += 1
        self.tab2update_display()

    def tab2update_current_batter(self, event):
        self.t2current_batter = self.t2batter_selection.get()
        if self.t2current_batter:
            self.tab2update_display()

    def tab2update_current_bowler(self, event):
        self.t2current_bowler = self.t2bowler_selection.get()
        if self.t2current_bowler:
            self.tab2update_display()

    def tab2remove_batter(self):
        if self.t2current_batter in player1names:
            player1names.remove(self.t2current_batter)
        if self.t2current_batter in player2names:
            player2names.remove(self.t2current_batter)
            
    def tab2update_display(self):
        self.t2batting_label.configure(text=f"Batting Team: {self.tab2batting_team}")
        self.t2bowling_label.configure(text=f"Bowling Team: {self.tab2bowling_team}")
        self.t2runs_label.configure(text=f"Runs: {self.t2runs}")
        self.t2balls_label.configure(text=f"Balls: {self.t2balls}")
        self.t2no_label.configure(text=f"No Balls: {self.t2teamNoBalls}")
        self.t2wide_label.configure(text=f"Wides: {self.t2wideBalls}")
        self.t2overs_label.configure(text=f"Overs: {self.t2overs}.{self.t2current_over_balls}")
        
# Create and run the application
app = App()
app.mainloop()