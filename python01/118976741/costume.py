import sys
from PIL import Image
images=[]
for arg in sys.argv:
    image=Image.open(arg)
    images.append(image)

immage[0].save(
     "costume.gif",save_all=True ,append_images=[images[1]],duration=200,loop=0
)
