def volumeDown():
    type(Key.DOWN, KeyModifier.CTRL)

for x in range(20):
    App('iTunes').focus()
    volumeDown()
    sleep(60)

App('iTunes').close()