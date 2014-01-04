try:
    # Try importing from Pillow
    from PIL import Image, ImageFilter
except:
    # If fails, try again with PIL
    import Image, ImageFilter

chick = Image.open("chick.jpg")

chick.save("병아리.bmp")

s = chick.resize((105, 146))
s.save("조그만 병아리.jpg")

chick.resize((200, 429)).save("홀쭉한 병아리.jpg")

c = chick.copy()
c.thumbnail((100, 100))
c.save("우표딱지 병아리.jpg")

chick.rotate(10).save("기우뚱한 병아리.jpg")

chick.transpose(Image.FLIP_TOP_BOTTOM).save("추락하는 병아리.jpg")

Image.eval(chick, lambda x: x + 64).save("볕에 나온 병아리.jpg")

Image.eval(chick, lambda x: x * 1.4).save("자체발광 병아리.jpg")

Image.eval(chick, lambda x: 256 - x).save("무서운 병아리.jpg")

L = chick.convert("L")
L.save("흑백 병아리.jpg")

Image.eval(L, lambda x: (x > 127) * 255).save("이진 명암 병아리.jpg")

chick.convert("1").save("디더링 병아리.jpg")

chick.filter(ImageFilter.MedianFilter(3)).save("매끈한 병아리.jpg")

chick.filter(ImageFilter.FIND_EDGES).save("엣지 있는 병아리.jpg")

M = 1.0 / 9.0
soft = ImageFilter.Kernel((3, 3), (M,) * 9)
chick.filter(soft).save("부드러운 병아리.jpg")

M = 1.0 / 25
ghost = ImageFilter.Kernel((5, 5), (M,) * 25)
chick.filter(ghost).save("병아리의 유령.jpg")
