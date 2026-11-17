candidates = {
    "Candidate A": 85,
    "Candidate B": 92,
    "Candidate C": 78
}

top_candidate = max(candidates, key=candidates.get)

highest_score = candidates[top_candidate]

average_score = sum(candidates.values()) / len(candidates)

print("Top Candidate:", top_candidate)
print("Highest Score:", highest_score)
print("Average Score:", average_score)