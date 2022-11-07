# modules
import os
import csv
# set path to to the csv:
election_csv = os.path.join('/Users/terryschoch/Desktop/Data_Analytics/python-challenge/Resources/election_data.csv')

votes_cast = []
candidates = []

#Open the file, Specify the variable to hold the contents & account for header
with open(election_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(reader) 
    # loop for and votes_cast and candidates to lists
    for row in reader:
        votes_cast.append(row[0])
        candidates.append(row[2])
    
# create a list of the three candidates
candidate_list = list(set(candidates))

# should for loop through the candidate list index and find the vote shares for each
# i = 0
# for i in candidate_list:
#     vote_percentage = round((candidates.count(i)/(len(candidates))*100), 3)
#     print(vote_percentage)



# Print summaries: Header, total number of votes cast,
print('Election Results')
print('-' * 30)
print('Total Votes: ' + str(len(votes_cast)))
print("-" * 30)
# print(f'{candidate_list[0]}: {round(((candidates.count(candidate_list[0])/(len(candidates)))*100), 3)}% ({(candidates.count(candidate_list[0]))})') 
# print(f'{candidate_list[1]}: {round(((candidates.count(candidate_list[1])/(len(candidates)))*100), 3)}% ({(candidates.count(candidate_list[1]))})')
# print(f'{candidate_list[2]}: {round(((candidates.count(candidate_list[2])/(len(candidates)))*100), 3)}% ({(candidates.count(candidate_list[2]))})')
# should for loop through the candidate list index and find the vote shares for each
i = 0
for i in candidate_list:
    vote_percentage = round((candidates.count(i)/(len(candidates))*100), 3)
    print(str(i) + ": " + str(vote_percentage) + "% (" + str(candidates.count(i)) + ")")

# print(f'{candidate_list[0]}: {round(((candidates.count(candidate_list[0])/(len(candidates)))*100), 3)}% ({(candidates.count(candidate_list[0]))})') 
# print(f'{candidate_list[1]}: {round(((candidates.count(candidate_list[1])/(len(candidates)))*100), 3)}% ({(candidates.count(candidate_list[1]))})')
# print(f'{candidate_list[2]}: {round(((candidates.count(candidate_list[2])/(len(candidates)))*100), 3)}% ({(candidates.count(candidate_list[2]))})')
print("-" * 30)
print(f'Winner: ')

# # Specify the file to write to
# election_results = os.path.join('/Users/terryschoch/Desktop/Data_Analytics/python-challenge/PyPoll/election_results.txt')

# # # Open the file using "write" mode. Specify the variable to hold the contents
# # with open(election_results, 'w') as datafile:
# #     # Initialize csv.writer
# #     writer = csv.writer(datafile)
# #     # Write the first row (column headers)
# #     writer.writerow('Election Results')
# #     writer.writerow('-' * 30)
# #     # Write the rest
# #     writer.writerows(candidate_list)


# candidate_list = set(candidates)
# choices = list(candidate_list)

# for candidate in candidate_list:
#      print(candidate)
# print(candidate_list[0])

# index = (choices.index(candidates[0]))
# print(index)

# print(candidates.count(choices[0]))
# print(candidates.count(choices[1]))
# print(candidates.count(choices[2]))



# from collections import Counter
# candidate_votes = Counter(candidates)
# print(candidate_votes)
# new = (sum(candidate_votes))
# print(new)

# for i, v in enumerate(candidate_votes):
#     if i == 0:
#         print(v)
# split_place = candidate_votes[1]/1
# print(split_place)


# votepercent = (candidates.count(candidate_list[0])/(len(candidates)))
# x = round((votepercent*100), 2)
# print(round((votepercent*100), 3))


# candidate_list = set(candidates)
# for candidate in candidate_list:
#     print(candidate)



# average_change = round(sum(changes)/(len(changes) - 1), 2)
# print("Average Change: $" + str(average_change))
# # determine max increase, its index and corresponding months; repeat for decrease - print results
# grincrease = max(newprofit_loss)
# increase_index = newprofit_loss.index(grincrease)
# grincrease_month = months[increase_index]