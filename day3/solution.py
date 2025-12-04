from home_visitor import HomeVisitor

input = open('day3/input.txt').read().strip()

visitor = HomeVisitor()

for direction in input:
    visitor.visit_day_1(direction)

print(len(visitor.homes_visited))
visitor.clear_visits()

for direction in input:
    visitor.visit_day_2(direction)
print(len(visitor.homes_visited))