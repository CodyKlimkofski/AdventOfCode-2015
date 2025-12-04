class HomeVisitor:
    def __init__(self):
        self.homes_visited = {(0, 0): 1}
        self.movers = {'Santa': (0, 0), 'Robo': (0, 0)}
        self.move_count = 0

    def visit_day_1(self, direction):
        mover = self.movers['Santa']
        mover = self._move(mover, direction)
        self.movers['Santa'] = mover

        if mover not in self.homes_visited:
            self.homes_visited[mover] = 1

    def visit_day_2(self, direction):
        if self.move_count % 2 == 0:
            self.movers['Santa'] = self._move(self.movers['Santa'], direction)
        else:
            self.movers['Robo'] = self._move(self.movers['Robo'], direction)
        self.move_count += 1

        for mover in self.movers.values():
            if mover not in self.homes_visited:
                self.homes_visited[mover] = 1

    def _move(self, mover, direction):
        if direction == '^':
            mover = (mover[0], mover[1] + 1)
        elif direction == 'v':
            mover = (mover[0], mover[1] - 1)
        elif direction == '>':
            mover = (mover[0] + 1, mover[1])
        elif direction == '<':
            mover = (mover[0] - 1, mover[1])
        return mover

    def clear_visits(self):
        self.homes_visited = {(0, 0): 1}
        self.movers = {'Santa': (0, 0), 'Robo': (0, 0)}
        self.move_count = 0