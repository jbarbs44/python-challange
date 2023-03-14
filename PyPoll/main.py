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
    TotalVotes= 0 

    for row in csv_reader:
        Total_Votes.append(row[0])
        Vote_Total =len(Total_Votes)
        Complete_Candidates.append(row[2])
        TotalVotes +=1
        Candidates = row[2]
        if Candidates in Votes_For_Candidates:
            Votes_For_Candidates[Candidates] += 1
        else:
            Votes_For_Candidates[Candidates] = 1

#Percent Vote for Each Candidate
#Percent for Charles Casper Stockham
Votes_For_Candidates["Charles Casper Stockham%"] = round((Votes_For_Candidates["Charles Casper Stockham"]/TotalVotes) * 100,3)
print(Votes_For_Candidates["Charles Casper Stockham%"])

#Percent for Diana DeGette
Votes_For_Candidates["Diana DeGette%"] = round((Votes_For_Candidates["Diana DeGette"]/TotalVotes) * 100,3)
print(Votes_For_Candidates["Diana DeGette%"])

#Percent for Raymon Anthony Doane
Votes_For_Candidates["Raymon Anthony Doane%"] = round((Votes_For_Candidates["Raymon Anthony Doane"]/TotalVotes) * 100,3)
print(Votes_For_Candidates["Raymon Anthony Doane%"])

#To find the candidate winner
Votes_For_Candidates_Winner = max(Votes_For_Candidates, key=Votes_For_Candidates.get)

#Print each of the required statements as per the module
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {Vote_Total}")
print("----------------------------------------")
print(f"Charles Casper Stockham:  {Votes_For_Candidates['Charles Casper Stockham%']}% ({Votes_For_Candidates['Charles Casper Stockham']})")
print(f"Diana DeGette:  {Votes_For_Candidates['Diana DeGette%']}% ({Votes_For_Candidates['Diana DeGette']})")
print(f"Raymon Anthony Doane:  {Votes_For_Candidates['Raymon Anthony Doane%']}% ({Votes_For_Candidates['Raymon Anthony Doane']})")
print("----------------------------------------")
print(f"Winner: {Votes_For_Candidates_Winner}")
print("----------------------------------------")