import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv) as csv_file:
    
    # create a csvreader
    csv_reader = csv.reader(csv_file, delimiter= ",")

    header_row = next(csv_reader)

    #empty dictinoary since multiple candidates and vairables
    Total_Votes = []
    Complete_Candidates= []
    Candidates = []
    Votes_For_Candidates= {}

    for row in csv_reader:
        Total_Votes.append(row[0])
        Vote_Total =len(Total_Votes)
        Complete_Candidates.append(row[2])
    for Candidate in Complete_Candidates:
        Candidates =[]
        if Candidate not in Candidates:
            Candidates.append(Candidate)
            print(Candidate)



















print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {Vote_Total}")
print("----------------------------------------")
    