import csv
import numpy as numpy

#data is in the same folder as python file
data_path = "election_data.csv"
#Data has three columns:
#0: "Voter ID", 1: "County" 2: "Candidate"



#Goals:
#1. Count total number of votes
total_votes = 0

#2. Create a dictionary of candidates that keeps track of their vote count and percentage
unique_candidates = {}
#Function to help create new instances of candidates
def new_candidate_dictionary():
    return {"Total Votes":0,"Vote Percentage":0}
#Value to make sure candidates are not duplicated
unique_candidate = True

#3. Determine a winner
election_tie = False
election_winner = ""
most_votes = 0

with open(data_path) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    #pull out header we won't need this data
    csv_header = next(election_data)
    for vote in election_data:
        total_votes += 1
        Voter_id = vote[0]
        County = vote[1]
        Candidate = vote[2]
        #Check if this candidate is new
        for candidate in unique_candidates:
            if Candidate == candidate:
                #if not unique don't create a new dictionary
                unique_candidate = False
                #Update the total votes for that candidate
                unique_candidates[Candidate]["Total Votes"] += 1
                #Exit loop: we don't need to check the other candidates
                break
        #If this is a new candidate add them to the dictionary
        if unique_candidate == True:
            unique_candidates[Candidate] = new_candidate_dictionary()
            #then add to the vote count for that candidate
            unique_candidates[Candidate]["Total Votes"] += 1
        #The next vote may be for a new candidate
        unique_candidate = True
    #Once the loop is complete we should have the total votes for all candidates
csvfile.close()

#Now go through our dictionary of candidates and update the vote percentage
for candidate in unique_candidates:
    counted_votes = unique_candidates[candidate]["Total Votes"]
    vote_percentage = round((counted_votes/total_votes)*100,2)
    unique_candidates[candidate]["Vote Percentage"] = vote_percentage

#Determine winnter
for candidate in unique_candidates:
    counted_votes = unique_candidates[candidate]["Total Votes"]
    if counted_votes > most_votes:
        most_votes = counted_votes
        election_winner = candidate

#Check for tie now that we have an unoffical winner
for candidate in unique_candidates:
    counted_votes = unique_candidates[candidate]["Total Votes"]
    if candidate != election_winner and counted_votes == most_votes:
        election_tie = True

if election_tie:
    election_winner += " (tied with another candidate)"

#Format Results
format_candidate_dictionary = ""
for candidate in unique_candidates:
    counted_votes = unique_candidates[candidate]["Total Votes"]
    vote_percentage = unique_candidates[candidate]["Vote Percentage"]
    candidate_info = f"{candidate}: {vote_percentage}% ({counted_votes})\n"
    format_candidate_dictionary += candidate_info

#note that there will be a new line at the end of the formatted candidate dictionary
results = f"\
Election Results\n\
------------------------\n\
Total Votes: {total_votes}\n\
------------------------\n\
{format_candidate_dictionary}\
------------------------\n\
Winner: {election_winner}\n\
------------------------"

print(f"\n{results}")

#create text file
new_text_file = "election_results.txt"
with open(new_text_file,'w') as text:
    text.write(results)
text.close()


