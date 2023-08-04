import os
import imageio

images = []
img = os.listdir("images")
for name in sorted(img):
    images.append(imageio.imread("images/" + name))

imageio.mimsave("output.gif",images) 

