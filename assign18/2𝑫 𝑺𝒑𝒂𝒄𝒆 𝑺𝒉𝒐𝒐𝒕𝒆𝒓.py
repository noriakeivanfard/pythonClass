import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class MyGame(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w, h)
        arcade.load_texture("img/background.png")

    def on_draw(self):
        arcade.start_render()

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()

if __name__ == "__main__":
    main() 
