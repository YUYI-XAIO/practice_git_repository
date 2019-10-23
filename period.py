# -*- coding: utf-8 -*-
import datetime
import time

print('預設：' + str(datetime.datetime.now()))
print('西元年月日：' + str(time.strftime("%Y-%m-%d", time.localtime())))
print('時分秒：' + str(time.strftime("%H:%M:%S", time.localtime())))
print('明天：' + str(datetime.date.today() + datetime.timedelta(days=1)))
print('前天：' + str(datetime.date.today() - datetime.timedelta(days=2)))
delete = datetime.datetime.now() - datetime.timedelta(hours=1)
add = datetime.datetime.now() + datetime.timedelta(hours=1)
print('前一個小時：' + str(delete.strftime("%H:%S:%M")))
print('下一個小時：'+ str(add.strftime("%H:%S:%M")))



