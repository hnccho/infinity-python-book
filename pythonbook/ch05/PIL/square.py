from PIL import Image, ImageDraw

SIZE = 256

image = Image.new("L", (SIZE, SIZE))
d = ImageDraw.Draw(image)

m = 64

for x in range(SIZE):
    for y in range(SIZE):
        inner = x in range(m, SIZE - m) and y in range(m, SIZE - m)
        d.point((x, y), inner * 255)

image.save('square.jpg')
