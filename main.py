import turtle
from model import Snake, Apple
from drawer import Drawer

class Launcher:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(500, 500)
        self.screen.bgcolor("black") 
        self.screen.tracer(0)
        
        self.snake = Snake()
        self.apple = Apple()
        self.drawer = Drawer(self.screen)
        
        self.game_active = False
        self.first_start = True
        self.setup_controls()
        
        self.drawer.draw_grid()
        self.drawer.draw_score(self.snake.score) 
        self.drawer.draw_snake(self.snake)       
        self.drawer.show_message("SNAKE GAME", "Tap the field to start\nUse the arrow keys")
        self.screen.update()

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(lambda: self.set_dir("up"), "Up")
        self.screen.onkey(lambda: self.set_dir("down"), "Down")
        self.screen.onkey(lambda: self.set_dir("left"), "Left")
        self.screen.onkey(lambda: self.set_dir("right"), "Right")
        self.screen.onscreenclick(self.handle_click)

    def set_dir(self, d):
        opp = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if d != opp.get(self.snake.direction):
            self.snake.direction = d

    def handle_click(self, x, y):

        if not self.game_active and not self.first_start:
            self.snake.reset()
            self.apple.respawn()
            self.drawer.clear_ui() 
            self.drawer.draw_grid() 
            self.drawer.draw_score(self.snake.score)
            self.game_active = True
            self.loop()

        elif self.first_start:
            self.first_start = False
            self.drawer.clear_ui() 
            self.drawer.draw_grid()
            self.game_active = True
            self.loop()

    def loop(self):
        if self.game_active:
            self.snake.move()
            

            s = self.snake
            if s.position[0] < 0 or s.position[0] >= 20 or \
               s.position[1] < 0 or s.position[1] >= 20 or \
               any(s.position == seg for seg in s.tail):
                self.game_active = False
                self.drawer.show_message("GAME OVER", f"Final Score: {s.score}\nPress for a new game")
                self.screen.update()
                return

            if s.position == self.apple.position:
                s.score += 10
                self.apple.respawn()
                self.drawer.draw_score(s.score) 

            self.drawer.draw_apple(self.apple)
            self.drawer.draw_snake(self.snake)
            self.screen.update()
            

            delay = max(50, 150 - (s.score // 5))
            self.screen.ontimer(self.loop, delay)

if __name__ == "__main__":
    Launcher()
    turtle.mainloop()
