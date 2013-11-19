teamstandings = [('LG', 63, 44, 0),
    ('삼성', 61, 44, 2),
    ('두산', 60, 46, 2),
    ('넥센', 58, 48, 2),
    ('롯데', 53, 50, 3),
    ('SK', 51, 50, 2),
    ('KIA', 46, 55, 2),
    ('NC', 45, 59, 4),
    ('한화', 31, 72, 1),]

for ts in teamstandings:
    team, win, lost, draw = ts
    games = win + lost + draw
    winrate = float(win) / (win + lost)
    format = '%s 팀은 총 %d 경기 중 %d 승으로 승률은 %.3f입니다.'
    print(format % (team, games, win, winrate))
    
