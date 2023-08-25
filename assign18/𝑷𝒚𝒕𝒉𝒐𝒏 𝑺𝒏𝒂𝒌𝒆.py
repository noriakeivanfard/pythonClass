import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Circle_red(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("image/Circle_red.png")
        self.width = 20
        self.height = 20
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)

class Circle(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("image/Circle_1.png")
        self.width = 34
        self.height = 34
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(10, w - 10)
        self.center_y = random.randint(10, h - 10)

        
class Circle_green(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("image/Circle_green.png")
        self.width = 20
        self.height = 20
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(10, w - 10)
        self.center_y = random.randint(10, h - 10)
                
class Circle_blue(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("image/Circle_blue.png")
        self.width = 20
        self.height = 20
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)
        
class Circle_yellow(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("image/Circle_yellow.png")
        self.width = 20
        self.height = 20
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(20, w - 20)
        self.center_y = random.randint(20, h - 20)
       
class Circle_purple(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__("image/Circle_purple.png")
        self.width = 20
        self.height = 20
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(10, w - 10)
        self.center_y = random.randint(10, h - 10)
        
class Snake(arcade.Sprite):
    def __init__(self,Game):
        super().__init__()
        self.width = 50
        self.height = 50
        self.radians = 10
        self.center_x = Game.width // 2
        self.center_y = Game.height // 2
        self.color = arcade.color.BLACK
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radians,self.color)
        arcade.draw_text("Score:", 350, 25, arcade.color.BLACK, 20)
        arcade.draw_text(self.score, 430, 23, arcade.color.BLACK, 20)

        body = 1
        for i in self.body:
            if body % 2 == 0:
                arcade.draw_circle_filled(i["a"], i["b"],self.radians , arcade.color.ANDROID_GREEN)
                body+=1
            else:
                arcade.draw_circle_filled(i["a"], i["b"],self.radians , arcade.color.AO)
                body+=1
                
    def move(self):
        self.body.append({"a":self.center_x,"b":self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def circle_red(self):
        self.score += 1

    def circle(self):
        self.score -= 1

    def circle_green(self):
        self.score += 2       
        
    def circle_blue(self):
        self.score += 1
        
    def circle_yellow(self):
        self.score += 1
        
    def circle_purple(self):
        self.score += 1
            
class MyGame(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.background = arcade.load_texture("image/background.png")
        self.snake = Snake(self)
        self.circle_red= Circle_red(self.width,self.height)
        self.circle = Circle(self.width,self.height)
        self.circle_green = Circle_green(self.width,self.height)
        self.circle_blue = Circle_blue(self.width,self.height)
        self.circle_yellow = Circle_yellow(self.width,self.height)
        self.circle_purple = Circle_purple(self.width,self.height)
        self.body = 1
        self.s = "s"
 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        if self.s == "s":
            self.snake.draw()
            self.circle_red.draw()    
            self.circle.draw()
            self.circle_green.draw()
            self.circle_blue.draw()
            self.circle_yellow.draw()
            self.circle_purple.draw()
        elif self.s == "o":
            arcade.draw_text("Game Over :(", self.width/3, self.height/2, color=arcade.color.BLACK, font_size=25, bold=True)

        arcade.finish_render()

    def on_update(self, delta_time):
        if self.s == "s":
            self.snake.move()
            
            if self.snake.center_x < 2 or self.snake.center_y < 2 or self.snake.center_x > 498 or self.snake.center_y > 498:
                self.s = "o"

            for i in self.snake.body[1:]:
                if self.snake.body[0] == i:
                    self.s = "o"

            if arcade.check_for_collision(self.snake, self.circle_red):
                del self.circle_red
                self.snake.circle_red()
                self.circle_red = Circle_red(self.width,self.height)

            elif arcade.check_for_collision(self.snake, self.circle):
                if len(self.snake.body) == 1 or len(self.snake.body) == 0:
                    self.s = "o"

                del self.circle
                self.snake.circle()
                self.circle = Circle(self.width,self.height)
                    
            elif arcade.check_for_collision(self.snake, self.circle_green):
                del self.circle_green
                self.snake.circle_green()
                self.circle_green = Circle_green(self.width,self.height)
                
            elif arcade.check_for_collision(self.snake, self.circle_blue):
                del self.circle_blue
                self.snake.circle_blue()
                self.circle_blue = Circle_blue(self.width,self.height)
                
            elif arcade.check_for_collision(self.snake, self.circle_yellow):
                del self.circle_yellow
                self.snake.circle_yellow()
                self.circle_yellow = Circle_yellow(self.width,self.height)
                
            elif arcade.check_for_collision(self.snake, self.circle_purple):
                del self.circle_purple
                self.snake.circle_purple()
                self.circle_purple = Circle_purple(self.width,self.height)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()

if __name__ == "__main__":
    main() 
