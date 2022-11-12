# modules
import os
import csv
# set path to to the csv:
election_csv = os.path.join('/Users/terryschoch/Desktop/Data_Analytics/python-challenge/Resources/election_data.csv')
# create lists to store total votes_cast and candidates who received votes
votes_cast = []
candidates = []
# open file, specify variable to hold the contents of file & account for header
with open(election_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader) 
    # loop for and append votes_cast and candidates to respective lists
    for row in reader:
        votes_cast.append(row[0])
        candidates.append(row[2]) 
# identify the unique candidate names and add to indexed list
candidate_list = list(set(candidates))
# print Header and Total votes_cast
print('Election Results')
print('-' * 30)
print('Total Votes: ' + str(len(votes_cast)))
print("-" * 30)
# create lists to store vote_results as well as vote_share percentage and total votes_earned per candidate
vote_results = []
vote_share = []
votes_earned = []
# create a function to append vote_share and votes_earned lists with respective results then:  
# find candidate name from candidate_list, their vote_share from share_percentage and their total votes_earned from candidates.count
# run function through a loop
def main():
    share_percentage = "{}%".format(round((candidates.count(i)/(len(candidates))*100), 3))
    vote_share.append(share_percentage)
    votes_earned.append("({})".format(candidates.count(i)))
    print(str(i) + ": " + str(share_percentage) + " (" + str(candidates.count(i)) + ")")
    return (str(i) + ": " + str(share_percentage) + " (" + str(candidates.count(i)) + ")")
for i in candidate_list:
    vote_results.append(main())
# find index of the winning vote share
winning_share = vote_share.index(max(vote_share))
# print Winner
print("-" * 30)
print(f'Winner: {candidate_list[winning_share]}')
print("-" * 30)

# -------------------------------------------
# Specify the file to write to
election_results = os.path.join('/Users/terryschoch/Desktop/Data_Analytics/python-challenge/PyPoll/election_results4.txt')
# Open the file using "write" mode. Specify variable to hold the text and results to be written and run for loop to write
words = ["Election Results", "-" * 30, "Total Votes: " + str(len(votes_cast)), "-" * 30, "\n".join(str(item) for item in vote_results), "-" * 30, "Winner: " + str(candidate_list[winning_share]), "-" * 30]
with open('election_results.txt', 'w') as f:
    for word in words:
        f.write(word + ("\n"))        
    f.close