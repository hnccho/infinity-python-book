import android, time

a = android.Android()

def pic():
  return '/sdcard/py4fun/images/'\
    +time.strftime('%Y%m%d%H%M%S')\
    +'.jpg'

def say(it):
  a.ttsSpeak(it)
  a.makeToast(it)

food = 'Keeeemcheeeee!'

for i in range(3):
  for j in range(3,0,-1):
    say(str(j))
    time.sleep(3)
  say(food)
  a.cameraCapturePicture(pic())
