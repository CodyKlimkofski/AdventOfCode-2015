file = open("day2/input.txt").read().strip()
from wrapping_paper_estimator import WrappingPaperEstimator

estimator = WrappingPaperEstimator()
total_paper = 0
total_ribbon = 0
for line in file.splitlines():
    total_paper += estimator.estimate_wrapping_paper(line)
    total_ribbon += estimator.estimate_ribbon_length(line)

print("Day 2 Part 1 answer: ", total_paper)
print("Day 2 Part 2 answer: ", total_ribbon)