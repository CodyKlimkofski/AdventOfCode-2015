class Elevator:
    def __init__(self):
        self.floor = 0

    def process_instructions(self, instructions):
        for instruction in instructions:
            if instruction == '(':
                self.floor += 1
            elif instruction == ')':
                self.floor -= 1
        
        answer = self.floor
        self.floor = 0
        return answer
    
    def find_basement(self, instructions):
        self.floor = 0
        for index, instruction in enumerate(instructions):
            if instruction == '(':
                self.floor += 1
            elif instruction == ')':
                self.floor -= 1
            
            if self.floor == -1:
                answer = index + 1
                self.floor = 0
                return answer
        
        self.floor = 0
        return -1