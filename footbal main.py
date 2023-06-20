import tkinter as tk
import random
import time
import logging

# Set the logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')

class FootballScoreInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Football Score Interface")

        self.team_a_score = 0
        self.team_b_score = 0
        self.count_time = 0

        self.team_a_label = tk.Label(master, text="Team A: 0", font=("Arial", 24))
        self.team_a_label.pack(pady=10)

        self.team_b_label = tk.Label(master, text="Team B: 0", font=("Arial", 24))
        self.team_b_label.pack(pady=10)

        self.count_time_label = tk.Label(master, text="Time: 0", font=("Arial", 24))
        self.count_time_label.pack(pady=10)

    def increment_team_a_score(self):
        self.team_a_score += 1
        self.update_scores()

    def increment_team_b_score(self):
        self.team_b_score += 1
        self.update_scores()

    def update_scores(self):
        self.team_a_label.config(text="Team A: {}".format(self.team_a_score))
        self.team_b_label.config(text="Team B: {}".format(self.team_b_score))

    def update_count_time(self):
        self.count_time_label.config(text=f"Time: {self.count_time}")

root = tk.Tk()
# Create an instance of the FootballScoreInterface class and run the interface
interface = FootballScoreInterface(root)
# root.mainloop()

# initial scores for two teams
countTime = 0

# main loop to update scores
while countTime <= 90:
    countTime =  countTime + 1
    interface.count_time = countTime
    interface.update_count_time()
    # randomly select a team to score
    highlights = random.randint(1, 20)
    
    # update the score for the selected team
    if highlights == 1:
        interface.team_a_score += 1
    elif highlights == 2:
        interface.team_b_score += 1
    
    # update the interface with the new scores
    interface.update_scores()
    root.update()
    # pause for a few seconds before the next update
    time.sleep(1)

