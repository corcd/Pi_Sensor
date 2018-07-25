from selenium import webdriver
import os
import time

# def screen_trigger():
#     return []

#def face_trigger(trigger):
try:
    trigger = 1  #触发器是否有效，默认有效
    condition = 'true\n'

    print('Service Start')
    while True:
        someone = os.popen('python3 core/Pi_PES.py').read()
        distance = os.popen('python3 core/Pi_PCSR.py').read()

        print(someone)
        print(distance)

        if (someone == condition and distance == condition and trigger == 1):
            print('Ready to Login')
            driver = webdriver.Firefox()
            driver.get('localhost:5000/login')  #打开网址
            driver.maximize_window()  #窗口最大化
            trigger = 0
        elif (someone == condition and distance == condition and trigger == 0):
            print('Logining...')
            pass
        else:
            print('Nobody Here')
            trigger = 1
        print('T=', trigger)
        print('\n')
        print('****************************\n')
        time.sleep(1)
except KeyboardInterrupt:
    print('Service End')
    pass

#face_trigger(trigger)