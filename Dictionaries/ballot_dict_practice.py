"""
The program below randomly generates a list of votes.
You are tasked with counting these votes.
Create a dictionary to represent the election results {name: vote_count}
"""

import random

names = ["Tim from accounting", "David Schwimmer", "Colonel Sanders", "Colonel Mustard", "Santa Clause", "Mrs. Pacman", "Ruth"]
candidates = []
for name in names:
    for x in range(random.randint(1,15)):
        candidates.append(name)

random.shuffle(candidates)

votes = {}

for cand in candidates:
    votes[cand] = votes.get(cand,0)+1

print(votes)