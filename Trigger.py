from selenium import webdriver
import os
import time

trigger = 1  #触发器是否有效，默认有效

# def screen_trigger():
#     return []

#def face_trigger(trigger):
try:
    print('开始后台检测')
    while True:
        someone = os.popen('python3 core/Pi_PES.py').read()
        distance = os.popen('python3 core/Pi_PCSR.py').read()

        print(someone, distance)
        # if isinstance(someone, bytes):
        #     s = str(someone, encoding='utf-8')
        # if isinstance(distance1, bytes):
        #     d1 = str(distance1, encoding='utf-8')
        # if isinstance(distance2, bytes):
        #     d2 = str(distance2, encoding='utf-8')

        if someone == "true" & distance == 'true' & trigger == 1:
            print('检测到人体')
            # chromedriver = '/home/pi/Downloads/chromedriver'
            # os.environ['webdriver.chrome.driver'] = chromedriver
            # driver = webdriver.Chrome(chromedriver)  #模拟打开浏览器
            # driver.get('localhost:5000/login')  #打开网址
            # driver.maximize_window()  #窗口最大化
            trigger = 0
        else:
            trigger = 1
        print(trigger)
        time.sleep(2)
except KeyboardInterrupt:
    print('终止后台检测')
    pass

#face_trigger(trigger)