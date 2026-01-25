import random

class Snake:
    def __init__(self, grid_width=20, grid_height=20):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.reset()

    def reset(self):
        self.position = [10, 10]
        self.tail = []
        self.direction = "right"
        self.score = 0

    def move(self):
        self.tail.append(list(self.position))
        
        if self.direction == "up": 
            self.position[1] -= 1
        elif self.direction == "down": 
            self.position[1] += 1
        elif self.direction == "left": 
            self.position[0] -= 1
        elif self.direction == "right": 
            self.position[0] += 1
        
        if len(self.tail) > self.score // 10:
            self.tail.pop(0)

class Apple:
    def __init__(self, grid_range=20):
        self.grid_range = grid_range
        self.respawn()

    def respawn(self):
        self.position = [random.randint(0, self.grid_range-1), 
                         random.randint(0, self.grid_range-1)]
