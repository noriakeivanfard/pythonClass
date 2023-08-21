import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

SPEED = 5

class Tir(arcade.Sprite):
    def __init__(self, gamer, a, s):
        super().__init__("img/Tir.png")
        self.center_x = gamer.center_x
        self.center_y = gamer.center_y
        self.speed = s
        self.angle = a
          
    def move(self):
        if self.angle == 90:
            self.center_y += self.speed
        elif self.angle == -90:
            self.center_y -= self.speed

class Space_shooter(arcade.Sprite):
    def __init__(self, game_board, img1="img/player_1.png"):
        super().__init__(img1)
        self.center_y = 70
        self.center_x = game_board.width/2
        self.width = 80
        self.height = 80
        self.speed = 5
        tir = 90
        self.tir = tir
        self.Game_width = game_board.width
        self.Tir_list = []
        self.hearts = []
        
    def update_jon(self, y=25, x = 25):
        for i in range(3):
            new_heart = Heart(x,y)
            self.hearts.append(new_heart)
            x += 30
            
    def move(self):
        if self.change_x == -1:
            if self.center_x > 20:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.Game_width-20:
                self.center_x += self.speed
                
    def fire(self):
        new_bullet = Tir(self, self.tir, SPEED)
        self.Tir_list.append(new_bullet)
        
class Heart(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("img/Heart.png")
        self.center_x = x
        self.center_y = y
        self.width = 50
        self.height = 50

class Space_shoorer2(arcade.Sprite):
    def __init__(self, game, img2="img/player_2.png"):
        super().__init__(img2)
        self.center_x = 300
        self.center_y = game.height/1.1
        self.width = 80
        self.height = 80
        self.speed = 4
        tir = 90
        self.tir = tir
        y = 70
        self.center_y = y
        a = 0
        self.angle = a
        self.Game_width = game.width
        self.Tir_list = []
        self.hearts = []
        
    def update_jon(self, y = 25, x = 25):
        for i in range(3):
            new_heart = Heart(x,y)
            self.hearts.append(new_heart)
            x += 30
        
    def move(self):
        if self.change_x == -1:
            if self.center_x > 20:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.Game_width-20:
                self.center_x += self.speed
                
    def fire(self):
        new_tir = Tir(self, self.tir, SPEED)
        self.Tir_list.append(new_tir)
        
class Heart(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("img/Heart.png")
        self.center_x = x
        self.center_y = y
        self.width = 50
        self.height = 50

class MyGame(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.background = arcade.load_texture("img/background.png")
        self.player_1 = Space_shooter(self)
        self.player_2 = Space_shoorer2(self)
        self.player_1.update_jon()
        self.player_2.update_jon(SCREEN_HEIGHT-25)
        self.s = "s"

    def on_draw(self):
        arcade.start_render()
        self.player_1.draw()
        self.player_2.draw()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        for tir in self.player_1.Tir_list:
            tir.draw()
        for tir in self.player_2.Tir_list:
            tir.draw()
        for heart in self.player_1.hearts:
            heart.draw()
        for heart in self.player_2.hearts:
            heart.draw()
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player_1.change_x = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.player_2.change_x = 0
        
    def on_key_press(self,key, modifiers):
        if self.s == "s":
            self.s = "g"
        
        elif self.s == "g":
            if key == arcade.key.RIGHT:
                self.player_1.change_x = -1
            elif key == arcade.key.LEFT:
                self.player_1.change_x = 1
            elif key == arcade.key.UP:
                self.player_1.fire()

            if key == arcade.key.A:
                self.player_2.change_x = -1
            elif key == arcade.key.D:
                self.player_2.change_x = 1
            elif key == arcade.key.X:
                self.player_2.fire()
            
    def on_update(self, delta_time):
        if self.s == "g":
            self.player_1.move()
            self.player_2.move()

            for tir in self.player_1.Tir_list:
                tir.move()
            for tir in self.player_2.Tir_list:
                tir.move()

            for tir in self.player_1.Tir_list:
                if arcade.check_for_collision(self.player_2, tir):
                    self.player_1.Tir_list.remove(tir)
                    self.player_2.hearts.remove(self.player_2.hearts[0])

            for tir in self.player_2.Tir_list:
                if arcade.check_for_collision(self.player_1, tir):
                    self.player_2.Tir_list.remove(tir)
                    self.player_1.hearts.remove(self.player_1.hearts[0])
                    
        if len(self.player_1.hearts) == 0:
            exit(0)
        elif len(self.player_2.hearts) == 0:
            exit(0)
        
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()

if __name__ == "__main__":
    main() 
