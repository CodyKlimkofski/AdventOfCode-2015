from elevator import Elevator

input = open("day1/input.txt").read().strip()
elevator = Elevator()
print("Day 1 Part 1 answer: ", elevator.process_instructions(input))
print("Day 1 Part 2 answer: ", elevator.find_basement(input))