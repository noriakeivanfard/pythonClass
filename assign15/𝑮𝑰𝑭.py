import os
import imageio
import numpy as np

images = []
img = os.listdir("images")
for name in sorted(img):
    image = imageio.v2.imread("images/" + name)
    image = np.resize(image, (720, 720, 3))
    images.append(image)
imageio.mimsave("output.gif",images)
