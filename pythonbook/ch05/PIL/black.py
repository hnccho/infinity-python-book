#!python

from PIL import Image, ImageDraw

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

for x in range(SIZE):
    for y in range(SIZE):
        d.point((x, y), 0)

image.save('black.jpg')