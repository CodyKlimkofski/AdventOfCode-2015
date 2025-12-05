class LightController:
    def __init__(self, size=1000):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def parse_instruction(self, instruction):
        parts = instruction.split()
        if parts[0] == "toggle":
            action = "toggle"
            start_coords = tuple(map(int, parts[1].split(',')))
            end_coords = tuple(map(int, parts[3].split(',')))
        else:
            action = parts[1]
            start_coords = tuple(map(int, parts[2].split(',')))
            end_coords = tuple(map(int, parts[4].split(',')))
        return action, start_coords, end_coords
    
    def apply_instruction_day_1(self, instruction):
        action, (x1, y1), (x2, y2) = self.parse_instruction(instruction)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == "on":
                    self.grid[x][y] = 1
                elif action == "off":
                    self.grid[x][y] = 0
                elif action == "toggle":
                    if self.grid[x][y] == 0:
                        self.grid[x][y] = 1
                    else:
                        self.grid[x][y] = 0

    def apply_instruction_day_2(self, instruction):
        action, (x1, y1), (x2, y2) = self.parse_instruction(instruction)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == "on":
                    self.grid[x][y] += 1
                elif action == "off":
                    self.grid[x][y] = max(0, self.grid[x][y] - 1)
                elif action == "toggle":
                    self.grid[x][y] += 2

    def turn_off_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = 0
