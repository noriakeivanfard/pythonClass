import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Sunny Forest')
arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE) 
arcade.start_render()


#Drow Ground
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH,SCREEN_HEIGHT / 4,0,arcade.color.EMERALD)

#Drow Sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and dow
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
  
# Diagonal ray
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

Column_spacing = 20
Row_spacing = 20
Left_margin = 90
Bottom_margin = 200

#Drow tree
for row in range(3):
    for column in range(3):
        x = column * Column_spacing + Left_margin
        y = row * Row_spacing + Bottom_margin 
    arcade.draw_triangle_filled(x + 40, y,x, y - 100,x + 80, y - 100,arcade.color.DARK_GREEN)
 
arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, 100, 53,arcade.color.DARK_BROWN)

# Draw sea
arcade.draw_ellipse_filled(SCREEN_WIDTH-300, 80, 150, 90, arcade.color.UNITED_NATIONS_BLUE, 180, -1)

#Draw rainbow 
arcade.draw_parabola_filled(100, 80, 410, 240, arcade.color.CARMINE_RED ,0)
arcade.draw_parabola_filled(125, 80, 380, 220, arcade.color.SAE ,0)
arcade.draw_parabola_filled(150, 80, 350, 200, arcade.color.AMBER ,0)
arcade.draw_parabola_filled(175, 80, 320, 180, arcade.color.AO,0)
arcade.draw_parabola_filled(200, 80, 290, 160, arcade.color.BALL_BLUE ,0)
arcade.draw_parabola_filled(225, 80, 260, 140, arcade.color.VIOLET ,0)

arcade.finish_render()
arcade.run() 
