#!/usr/bin/env python

from PIL import Image, ImageDraw
import random

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

for x in range(SIZE):
    for y in range(SIZE):
        d.point((x, y), random.choice([0, 255]))

image.save('noise.jpg')
