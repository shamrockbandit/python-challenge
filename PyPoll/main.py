import os
import csv

input_file = os.path.join("PyPoll/Resources/election_data.csv")
output_file = os.path.join("PyPoll/Resources/election_analysis.txt")

candidates = []
num_votes = 0
vote_count = []

with open(input_file) as vote_csv:
    vote_data = csv.reader(vote_csv)
    line = next(vote_data, None)

    for line in vote_data:
        num_votes = num_votes + 1
        candidate = line[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_count.append(1)

percentages = []
max_votes = vote_count[0]
max_index = 0
for count in range(len(candidates)):
    vote_percentage = vote_count[count] / num_votes * 100
    percentages.append(vote_percentage)
    voter_output = f"{candidates[count]}: {vote_percentage:.1f}% ({vote_count[count]:,})\n"
    print(voter_output)
    if vote_count[count] > max_votes:
        max_votes = vote_count[count]
        print(max_votes)
        max_index = count
    
winner = candidates[max_index]

output = (
f"final results \n"
f"-------------------------- \n"
f"total votes: {num_votes:,} \n"
f"winner: {winner}"
)

print(output)
with open(output_file, "w") as txt_file:
    txt_file.write(output)