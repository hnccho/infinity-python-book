MAX_STRAWBERRY = 3
STRAWBERRY_COUNTER = 0

def plant(crop, reg=SCREEN):
    plot = "farmplot.png" 
    if not reg.exists(plot):
        result = False
    else:
        click(plot)
        wait(Pattern("pick a crop.png").similar(0.80), 10)
        click(crop)
        click(plot)
        wait("stop button.png", 10)
        click("stop button.png")
        result = True
    return result

def harvest(crop, reg=SCREEN):
    if not reg.exists(crop):
        result = False
    else:
        position = reg.find(crop)
        hover(position)
        if position.nearby().exists(Pattern("sickle.png").similar(0.50)):
            click(position)
            sleep(3)
            gather(position.nearby(), Pattern("dropped goods.png").similar(0.60))
            gather(position.nearby(), Pattern("dropped star.png").similar(0.60))
            result = True
        else:
            result = False
    return result

def gather(reg, item):
	m = reg.exists(item)
	if m != None:
		hover(m.getTarget())

def growStrawberry(event):
    global STRAWBERRY_COUNTER
    print('growStrawberry start')
    reg = SCREEN if event == None else event.region
    if exists("grown strawberry.png") and harvest("grown strawberry.png", reg):
        STRAWBERRY_COUNTER = STRAWBERRY_COUNTER - 1
        if STRAWBERRY_COUNTER < 0:
            STRAWBERRY_COUNTER = 0
    if STRAWBERRY_COUNTER < MAX_STRAWBERRY and plant("strawberry seed.png"):
        STRAWBERRY_COUNTER = STRAWBERRY_COUNTER + 1
    print(STRAWBERRY_COUNTER)
    print('growStrawberry end')
    
onChange(growStrawberry)
observe(600)
