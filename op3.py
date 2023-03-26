
import tkinter as tk
 
# Initialize the vote counts for each candidate to zero
Candidate1_votes = 0
Candidate2_votes = 0
Candidate3_votes = 0
 
# Create a function to display the vote count window
def display_vote_count():
    # Create a new window
    vote_count_window = tk.Toplevel(window)
    vote_count_window.title("Current Vote Counts")
 
    # Create a label to display the vote counts
    vote_counts_label = tk.Label(vote_count_window, text="Current Vote Counts:", font=("Arial", 12))
    vote_counts_label.pack(pady=10)
 
    Candidate1_votes_label = tk.Label(vote_count_window, text="ALLAN: " + str(Candidate1_votes))
    Candidate1_votes_label.pack(pady=5)
 
    Candidate2_votes_label = tk.Label(vote_count_window, text="NAND: " + str(Candidate2_votes))
    Candidate2_votes_label.pack(pady=5)
 
    Candidate3_votes_label = tk.Label(vote_count_window, text="RAVI: " + str(Candidate3_votes))
    Candidate3_votes_label.pack(pady=5)
 
# Create a window
window = tk.Tk()
window.title("Smart Voting System")
 
# Create labels
title_label = tk.Label(window, text="Welcome to Smart Voting System", font=("Arial", 18))
title_label.pack(pady=20)
 
question_label = tk.Label(window, text="Please select your preferred candidate:", font=("Arial", 12))
question_label.pack(pady=10)
 
# Create radio buttons for candidate selection
candidate_var = tk.StringVar()
 
Candidate1_rb = tk.Radiobutton(window, text="ALLAN", variable=candidate_var, value="ALLAN")
Candidate1_rb.pack(pady=5)
 
Candidate2_rb = tk.Radiobutton(window, text="NAND", variable=candidate_var, value="NAND")
Candidate2_rb.pack(pady=5)
 
Candidate3_rb = tk.Radiobutton(window, text="RAVI", variable=candidate_var, value="RAVI")
Candidate3_rb.pack(pady=5)
 
# Create a function to submit the vote
def submit_vote():
    global Candidate1_votes, Candidate2_votes, Candidate3_votes
    
    selected_candidate = candidate_var.get()
    
    # Update the vote count for the selected candidate
    if selected_candidate == "ALLAN":
        Candidate1_votes += 1
    elif selected_candidate == "NAND":
        Candidate2_votes += 1
    elif selected_candidate == "RAVI":
        Candidate3_votes += 1
        
    # Display the confirmation message
    confirmation_label.config(text="Your vote for " + selected_candidate + " has been recorded.")
#confirmation_label.config(text="Your vote has been recorded")
#confirmation_label.config(text="Thank you, Visit next Election")
    
# Create a button to submit the vote
submit_button = tk.Button(window, text="Submit", command=submit_vote)
submit_button.pack(pady=20)
 
# Create a label to display confirmation message after submitting vote
confirmation_label = tk.Label(window, font=("Arial", 12))
confirmation_label.pack(pady=10)
 
# Create a button to display the vote count
display_vote_count_button = tk.Button(window, text="Display Vote Count", command=display_vote_count)
display_vote_count_button.pack(pady=10)
 
# Start the GUI
window.mainloop()

