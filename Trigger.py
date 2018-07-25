from selenium import webdriver
import os
import time

trigger = 1  #触发器是否有效，默认有效


def screen_trigger():
    return []


def face_trigger(trigger):
    try:
        while True:
            someone = os.popen('python3 core/Pi_PES.py').read()
            distance1 = os.popen('python3 core/Pi_PCSR.py').read()
            time.sleep(1)
            distance2 = os.popen('python3 core/Pi_PCSR.py').read()

            # if isinstance(someone, bytes):
            #     s = str(someone, encoding='utf-8')
            # if isinstance(distance1, bytes):
            #     d1 = str(distance1, encoding='utf-8')
            # if isinstance(distance2, bytes):
            #     d2 = str(distance2, encoding='utf-8')

            if someone == 'true' & distance1 < 100 & distance1 > 30 & distance2 < 100 & distance2 > 30 & trigger == 1:
                chromedriver = "/home/pi/Downloads/chromedriver"
                os.environ["webdriver.chrome.driver"] = chromedriver
                driver = webdriver.Chrome(chromedriver)  #模拟打开浏览器
                driver.get("https://www.baidu.com/")  #打开网址
                driver.maximize_window()  #窗口最大化
                trigger = 0
            else:
                trigger = 1
        time.sleep(2)
    except KeyboardInterrupt:
        return []

face_trigger(trigger)