#!python

from PIL import Image, ImageDraw

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

width = 4

for x in range(SIZE):
    for y in range(SIZE):
        d.point((x, y), (x / width % 6 != 0) * 255)

image.save('stripe.jpg')
