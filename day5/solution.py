from string_determiner import StringDeterminer

input = open('day5/input.txt').read().strip().split('\n')

determiner = StringDeterminer()
part_one_count = sum(1 for line in input if determiner.is_nice_day_1(line))
print(f"Part 1: {part_one_count}")

part_two_count = sum(1 for line in input if determiner.is_nice_day_2(line))
print(f"Part 2: {part_two_count}")