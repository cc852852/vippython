# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/23 18:26
import schedule
import time
def job():
    print('哈哈-------------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)