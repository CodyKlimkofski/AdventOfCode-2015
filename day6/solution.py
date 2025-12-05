from light_controller import LightController

input = open('day6/input.txt').read().strip().split('\n')
controller = LightController()

for instruction in input:
    controller.apply_instruction_day_1(instruction)

print('Part 1: ', sum(light for row in controller.grid for light in row))

controller.turn_off_grid()

for instruction in input:
    controller.apply_instruction_day_2(instruction)

print('Part 2: ', sum(light for row in controller.grid for light in row))