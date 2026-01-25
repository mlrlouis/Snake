import turtle

class Drawer:
    def __init__(self, screen):
        self.screen = screen
        self.grid_size = 20  
        self.offset = 190

        self.snake_pen = self.create_pen()
        self.snake_pen.shape("square") 
        self.apple_pen = self.create_pen()
        self.apple_pen.shape("circle")
        
        self.ui_pen = self.create_pen()
        

        self.score_pen = self.create_pen()
        self.score_pen.color("white")
        self.score_pen.goto(0, 210) 

    def create_pen(self):
        p = turtle.Turtle()
        p.hideturtle()
        p.penup()
        p.speed(0)
        return p

    def draw_grid(self):
        self.ui_pen.clear()
        self.ui_pen.color("grey") 
        for i in range(-200, 201, self.grid_size):
            self.ui_pen.goto(i, -200)
            self.ui_pen.pendown()
            self.ui_pen.goto(i, 200)
            self.ui_pen.penup()
            
            self.ui_pen.goto(-200, i)
            self.ui_pen.pendown()
            self.ui_pen.goto(200, i)
            self.ui_pen.penup()

    def draw_snake(self, snake):
        self.snake_pen.clear()
        
        # tail
        for pos in snake.tail:
            self.snake_pen.goto(-self.offset + pos[0]*20, self.offset - pos[1]*20)
            self.snake_pen.color("green")
            self.snake_pen.stamp()
        
        # head
        self.snake_pen.goto(-self.offset + snake.position[0]*20, self.offset - snake.position[1]*20)
        self.snake_pen.color("darkgreen")
        self.snake_pen.stamp()

    def draw_apple(self, apple):
        self.apple_pen.clear()
        self.apple_pen.goto(-self.offset + apple.position[0]*20, self.offset - apple.position[1]*20)
        self.apple_pen.color("red")
        self.apple_pen.stamp()

    def draw_score(self, score):
        self.score_pen.clear()
        self.score_pen.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

    def show_message(self, title, subtitle=""):
        self.ui_pen.clear()
        self.ui_pen.color("white")
        self.ui_pen.goto(0, 50)
        self.ui_pen.write(title, align="center", font=("Arial", 30, "bold"))
        self.ui_pen.goto(0, -20)
        self.ui_pen.write(subtitle, align="center", font=("Arial", 14, "normal"))
    
    def clear_ui(self):
        self.ui_pen.clear()