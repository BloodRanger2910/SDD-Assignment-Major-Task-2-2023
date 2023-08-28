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
import tkinter as tk
from PIL import Image, ImageTk

class App(ctk.CTk): 
    def __init__(self):
        ctk.CTk.__init__(self)  # Create the application window
        self.title("Cricket Scoring")  # Set the desired title
        self.geometry("900x700")
        self.resizable(False, False) #fixed window size
        self.iconbitmap(r"CricketScorkingApplicaton\Assests\Cricket_Icon.ico") #application icon
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
        self._frame.pack(fill="both", expand=True)  # Fill both directions

class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        # main menu image
        MainMenuLogo = ctk.CTkImage(dark_image=Image.open(r"CricketScorkingApplicaton\Assests\Cricket_Logo.png"), size=(400, 400))
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
            self.master.destroy()  # Close the entire application

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
        go = msg.askokcancel(title="Confirm?", message="Confirm Names?")
        if go:
            global Team1Players
            Team1Players = []
            for entry in playername_entries_team1:
                Team1Players.append(entry.get())
            global Team2Players
            Team2Players = []
            for entry in playername_entries_team2:
                Team2Players.append(entry.get())
            global Team1Name
            Team1Name = team1name_entry.get()
            global Team2Name
            Team2Name = team2name_entry.get()
            if Team1Name=="" or Team2Name=="":
                msg.showerror(title="Invalid!",
                                     message="The Team Name entry fields are empty.\nPlease check that all fields have been filled in.")
                return
            for member in Team1Players:
                if member=="":
                    msg.showerror(title="Invalid!",
                                     message="One or more entry fields under Team 1's Players are empty.\nPlease check that all fields have been filled in.")
                    return
            for member in Team2Players:
                if member=="":
                    msg.showerror(title="Error",
                                     message="One or more entry fields under Team 2's Players are empty.\nPlease check that all fields have been filled in.")
                    return
            self.master.switch_frame(ScoringFrame)

class ScoringFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master, width=900, height=700)
        global player1names
        player1names = Team1Players
        global player2names
        player2names = Team2Players
        global team1name
        team1name = Team1Name
        global team2name
        team2name = Team2Name
        
        self.team_label = ctk.CTkLabel(self, text=f"Teams: {team1name} vs {team2name}")
        self.team_label.pack(pady=10)
        self.player_label = ctk.CTkLabel(self, text=f"Team 1 Players: {player1names} \nvs \nTeam 2 Players:5 b {player2names}")
        self.player_label.pack(pady=10)
        
        # Contine button
        Continue = ctk.CTkButton(self,  text="Contine",
                                    command=lambda: master.switch_frame(TossFrame))
        Continue.pack(pady=10)
        
class TossFrame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master, width=900, height=700)

        global team1name
        team1name = Team1Name
        global team2name
        team2name = Team2Name
        
        self.toss_label = ctk.CTkLabel(self, text="Toss Time! Click the button to determine batting and bowling teams.")
        self.toss_label.pack(pady=10)

        self.toss_button = ctk.CTkButton(self, text="Toss", command=self.perform_toss)
        self.toss_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)

        # Initialize the Continue button but keep it hidden for now
        self.continue_button = ctk.CTkButton(self, text="Continue",
                                             command=lambda: master.switch_frame(ScoringGameFrame))
        self.continue_button.pack(pady=10)
        self.continue_button.pack_forget()  # Hide the button initially
        
    def perform_toss(self):
        global batting_team
        global bowling_team
        tossing_team = Team1Name if random.choice([True, False]) else Team2Name

        choice = msg.askyesno("Toss Result", f"{tossing_team} won the toss!\nDo you want to bowl?")

        if choice:  # Yes means they want to bowl
            batting_team, bowling_team = Team1Name if tossing_team == Team2Name else Team2Name, tossing_team
        else:  # No means they want to bat
            batting_team, bowling_team = tossing_team, Team1Name if tossing_team == Team2Name else Team2Name

        # Display the toss result
        toss_result = f"{tossing_team} won the toss and chose to {'bowl' if choice else 'bat'}.\n{bowling_team} will be bowling.\n{batting_team} will be batting."
        self.result_label.configure(text=toss_result)

        # Show the Continue button
        self.continue_button.pack()

        # Hide Toss Button
        self.toss_button.pack_forget()
        
        
class ScoringGameFrame(ctk.CTkFrame):
    def __init__(self, master):
        global team1name, team2name, player1names, player2names, batting_team, bowling_team, TeamTabs
        self.tab1batting_team = batting_team
        self.tab1bowling_team = bowling_team
        self.t1battersOut = []
        self.t1player_runs = {}  # Dictionary to store player runs
        self.t1player_balls = {}  # Dictionary to store player balls
        self.t1teamRuns = 0
        self.t1wideBalls = 0
        self.t1teamNoBalls = 0
        self.t1teamWickets = 0
        self.t1overs = 0
        self.t1totalBalls = 0
        self.t1runs = 0  # Initialize the 'runs' attribute
        self.t1balls = 0  # Initialize the 'balls' attribute
        self.t1current_batter = None
        self.t1current_bowler = None
        
        self.tab2batting_team = bowling_team
        self.tab2bowling_team = batting_team
        self.t2battersOut = []
        self.t2player_runs = {}  # Dictionary to store player runs
        self.t2player_balls = {}  # Dictionary to store player balls
        self.t2teamRuns = 0
        self.t2wideBalls = 0
        self.t2teamNoBalls = 0
        self.t2teamWickets = 0
        self.t2overs = 0
        self.t2totalBalls = 0
        self.t2runs = 0  # Initialize the 'runs' attribute
        self.t2balls = 0  # Initialize the 'balls' attribute
        self.t2current_batter = None
        self.t2current_bowler = None
        
        ctk.CTkFrame.__init__(self, master, width=900, height=700)
        TeamTabs = ctk.CTkTabview(master=self)
        TeamTabs.pack(padx=20, pady=5, expand=True, fill=tk.BOTH)
        Team1Tab = TeamTabs.add(self.tab1batting_team)
        Team2Tab = TeamTabs.add(self.tab1bowling_team)
        

    #This entire section is dedicated to Team1Tab
        # Runs and Balls Label
        self.runs_label = ctk.CTkLabel(Team1Tab, text=f"Runs: {self.t1runs}")
        self.runs_label.pack(pady=10)
        self.balls_label = ctk.CTkLabel(Team1Tab, text=f"Balls: {self.t1runs}")
        self.balls_label.pack(pady=10)
        
        # Initialize player_runs and player_balls dictionaries
        for player in player1names + player2names:
            self.t1player_runs[player] = 0
            self.t1player_balls[player] = 0
            
         # Batting and Bowling Team Labels
        self.batting_label = ctk.CTkLabel(Team1Tab, text=f"Batting: {self.tab1batting_team}")
        self.batting_label.pack(pady=10)
        self.bowling_label = ctk.CTkLabel(Team1Tab, text=f"Bowling: {self.tab1bowling_team}")
        self.bowling_label.pack(pady=10)

        # Labels next to player selection ComboBoxes
        self.batter_label = ctk.CTkLabel(Team1Tab, text="Select Batter:")
        self.batter_label.pack(pady=5)
        self.batter_selection = ctk.CTkComboBox(Team1Tab, values=player1names if self.tab1batting_team == team1name else player2names)
        self.batter_selection.pack(pady=5)
        
        self.bowler_label = ctk.CTkLabel(Team1Tab, text="Select Bowler:")
        self.bowler_label.pack(pady=5)
        self.bowler_selection = ctk.CTkComboBox(Team1Tab, values=player1names if self.tab1bowling_team == team1name else player2names)
        self.bowler_selection.pack(pady=5)
        
        # Bind the ComboboxSelected event to update selected batter and bowler
        self.batter_selection.bind("<<ComboboxSelected>>", self.update_current_batter)
        self.bowler_selection.bind("<<ComboboxSelected>>", self.update_current_bowler)
        
        # Buttons for Runs and Actions
        run_buttons_frame = ctk.CTkFrame(Team1Tab, fg_color="transparent")
        run_buttons_frame.pack(pady=10)

        for i in range(1, 7):
            run_buttons_frame.grid_columnconfigure(i, weight=1)
            run_button = ctk.CTkButton(run_buttons_frame, text=str(i), command=lambda i=i: self.add_runs(i))
            run_button.grid(row=0, column=i, padx=2, pady=2)
            
        for i in range(1, 7):
            run_buttons_frame.grid_columnconfigure(i, weight=1)
            run_button = ctk.CTkButton(run_buttons_frame, text=str(i), command=lambda i=i: self.remove_runs(i))
            run_button.grid(row=1, column=i, padx=2, pady=2)
        
        runsLabel = ctk.CTkLabel(run_buttons_frame, text="Add Runs:")
        runsLabel.grid(row=0, column=0)
        runsRemoveLabel = ctk.CTkLabel(run_buttons_frame, text="Remove Runs:")
        runsRemoveLabel.grid(row=1, column=0)
        extrasLabel = ctk.CTkLabel(run_buttons_frame, text="Extras:")
        extrasLabel.grid(row=2, column=0)
        
        no_ball_button = ctk.CTkButton(run_buttons_frame, text="No Ball", command=self.add_no_ball)
        no_ball_button.grid(row=2, column=1, padx=2, pady=2)

        wide_button = ctk.CTkButton(run_buttons_frame, text="Wide", command=self.add_wide)
        wide_button.grid(row=2, column=2, padx=2, pady=2)

        wicket_button = ctk.CTkButton(run_buttons_frame, text="Wicket", command=self.record_wicket)
        wicket_button.grid(row=3, column=1, padx=2, pady=2)

    def add_runs(self, runs):
        # Update runs and balls for the current batter
        if self.t1current_batter:
            self.t1player_runs[self.t1current_batter] += 1
            self.t1player_balls[self.t1current_batter] += 1
        self.t1runs += runs
        self.t1balls += 1
        self.update_display()

    def remove_runs(self):
        if self.t1runs > 0:
            self.t1runs -= 1
            self.update_display()
        # Update runs and balls for the current batter
        if self.t1current_batter:
            self.t1player_runs[self.t1current_batter] += 1
            self.t1player_balls[self.t1current_batter] += 1
        self.t1runs += runs
        self.t1balls += 1
        self.update_display()


    def add_no_ball(self):
        # Update runs and balls for the current batter
        if self.t1current_batter:
            self.t1player_runs[self.t1current_batter] += 1
            self.t1player_balls[self.t1current_batter] += 1
        self.t1runs += 1
        self.t1balls += 1
        self.update_display()

    def add_wide(self):
        self.t1runs += 1
        self.t1balls += 1
        self.update_display()

    def record_wicket(self):
        wicket_popup = ctk.CTkToplevel(self)
        wicket_popup.title("Record Wicket")
        wicket_popup.geometry("300x150")

        wicket_label = ctk.CTkLabel(wicket_popup, text=f"{self.t1current_batter} out by {self.t1current_bowler}")
        wicket_label.pack(pady=10)

        remove_batter_button = ctk.CTkButton(wicket_popup, text="Remove Batter", command=self.remove_batter)
        remove_batter_button.pack(pady=5)
        
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
        self.batting_label.configure(text=f"Batting: {self.tab1batting_team}")
        self.bowling_label.configure(text=f"Bowling: {self.tab1bowling_team}")
        self.runs_label.configure(text=f"Runs: {self.t1runs}")
        self.balls_label.configure(text=f"Balls: {self.t1balls}")
    
    def display_player_statistics(self):
        stats = "Player Statistics:\n"
        for player in self.t1player_runs.keys():
            stats += f"{player}: Runs - {self.t1player_runs[player]}, Balls - {self.t1player_balls[player]}\n"
        msg.showinfo("Player Statistics", stats)
        
        
# Create and run the application
app = App()
app.mainloop()