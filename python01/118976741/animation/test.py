import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1],images[2],images[3],images[4],images[5],images[6],images[7]] ,duration=200, loop=0
)
