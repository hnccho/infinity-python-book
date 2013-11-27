import android, twitpic, time

USER = 'pythonlab'
PASS = '********'

pic = '/sdcard/py4fun/images/'\
  + time.strftime('%Y%m%d%H%M%S')\
  + '.jpg'

droid = android.Android()
droid.cameraCapturePicture(pic)
t = twitpic.TwitPicAPI(USER, PASS)
t.upload(pic)
