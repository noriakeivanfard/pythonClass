import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "happy Face"

# Open window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BISQUE)

arcade.start_render()

# Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
arcade.draw_circle_outline(x,y,radius, arcade.color.BLACK)


# Draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw hat
arcade.draw_parabola_filled(350, 320, 200, 150, arcade.color.BANGLADESH_GREEN ,0)
arcade.draw_ellipse_filled(SCREEN_HEIGHT-350, 480, 200, 20, arcade.color.BANGLADESH_GREEN, 180, -1)

# Drow nose
arcade.draw_arc_outline(300, 280, 50, 36,arcade.color.BLACK, 50, 250)

# Draw the smile
x = 300
y = 240
width = 180
height = 150
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height,
                       arcade.color.BLACK, 
                       start_angle, end_angle, 10)

arcade.finish_render()
arcade.run()
