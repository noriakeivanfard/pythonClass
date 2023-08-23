import arcade
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Ball(arcade.Sprite):
    def __init__(self, game, img2="images/disc.png"):
        super().__init__(img2)
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.radius = 20
        self.change_x = random.choice([1,-1])
        self.change_y = random.choice([1,-1])
        self.speed = 4
        self.width = self.radius * 2
        self.height = self.radius * 2
    
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        
class Rocket(arcade.Sprite):
    def __init__(self, game, img2="images/blue_rocket.png"):
        super().__init__(img2)
        self.center_y = 70
        self.center_x = SCREEN_WIDTH-200
        self.width = 80
        self.height = 5
        self.score = 0
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.score = 0
        
class Rocket2(arcade.Sprite):
    def __init__(self, game, img3="images/red_rocket.png"):
        super().__init__(img3) 
        self.center_y = 540 
        self.center_x = SCREEN_WIDTH-200
        self.width = 80
        self.height = 5
        self.speed = 3
        self.score = 0
        
    def move(self,ball,game):
        
            if self.center_x > ball.center_x:
                self.change_x = -1

            if self.center_x < ball.center_x:
                self.change_x = +1

            self.center_x += self.change_x * self.speed

            if self.center_x < 60:
                self.center_x = 60

            if self.center_x > game.width - 60:
                self.center_x = game.width - 60
                
class MyGame(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.background = arcade.load_texture("images/background.png")
        self.ball = Ball(self)
        self.player_1 = Rocket(self)
        self.player_2 = Rocket2(self)
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.ball.draw()
        self.player_1.draw()
        self.player_2.draw()
        arcade.draw_text("Score: ", 25, 570,font_size=15)
        arcade.draw_text(self.player_1.score, 90, 570,font_size=15)
        
        arcade.draw_text("Score: ", 300, 15,font_size=15)
        arcade.draw_text(self.player_2.score, 370, 15,font_size=15)
            
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.player_1.width < x < self.width-self.player_1.width:
            self.player_1.center_x = x 
            
    def on_update(self, delta_time):
        self.ball.move()
        self.player_2.move(self.ball,self)

        if self.ball.center_x < 30 or self.ball.center_x > self.width - 20:
            self.ball.change_x *= -1
        
        if arcade.check_for_collision(self.player_1, self.ball) or arcade.check_for_collision(self.player_2, self.ball):
            self.ball.change_y *= -1

        if self.ball.center_y < 0:
            self.player_1.score += 1
            del self.ball
            self.ball = Ball(self)
            self.ball.speed += 1

        if self.ball.center_y > self.height:
            self.player_2.score += 1
            del self.ball
            self.ball = Ball(self)
            self.ball.speed += 1

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()

if __name__ == "__main__":
    main() 
