import random

reg = Region(find("window.png"))

cell = {
    'unknown': [
        Pattern("cell_unknown_1.png").similar(0.98),
        Pattern("cell_unknown_2.png").similar(0.98),
        Pattern("cell_unknown_3.png").similar(0.98),
        ],
    'question': Pattern("cell_question.png").similar(0.90),
    'exploded': Pattern("cell_exploded.png").similar(0.90)}

patterns = [
    Pattern("pattern_1of9_nw1.png").similar(0.97).targetOffset(-14,-14),
    Pattern("pattern_1of9_ne1.png").similar(0.97).targetOffset(14,-14),
    Pattern("pattern_1of9_ne2.png").similar(0.97).targetOffset(14,-14),
    Pattern("pattern_1of9_sw1.png").similar(0.97).targetOffset(-14,14),
    Pattern("pattern_1of9_se1.png").similar(0.97).targetOffset(14,14),
    Pattern("pattern_1of9_se2.png").similar(0.97).targetOffset(14,14),
    Pattern("pattern_121_e1.png").similar(0.97).targetOffset(9,-18),
    Pattern("pattern_121_e2.png").similar(0.97).targetOffset(9,-18),
    Pattern("pattern_121_e3.png").similar(0.97).targetOffset(9,18),
    Pattern("pattern_121_e4.png").similar(0.97).targetOffset(9,18),
    Pattern("pattern_121_s1.png").similar(0.97).targetOffset(20,10),
    Pattern("pattern_121_s2.png").similar(0.97).targetOffset(-16,11),
    ]
    
def unknownCellExists():
    result = False
    for cu in cell['unknown']:
        if reg.exists(cu):
            result = True
    return result

while unknownCellExists():
    for pattern in patterns:
        while reg.exists(pattern):
            print(pattern)
            rightClick(reg.find(pattern))
            if reg.exists(cell['question']):
                q = reg.find(cell['question'])
                rightClick(q)
                rightClick(q)
    if unknownCellExists():
        click(random.choice(cell['unknown']))
    if exists(cell['exploded']):
        break