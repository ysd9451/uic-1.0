from bs4 import BeautifulSoup
# import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

course1 = True  # 是否抢第一门课
course2 = True  # 是否抢第二门课
#course3 = True
course1name = 'Corporate Sustainability and Industry Innovation (1002)'  # 第一门课名字
course2name = 'Basketball (Group 5) (1004)'  # 第二门课名字
#course3name = 'Experiential Arts (Appreciation Lecture-Visual Thinking II) (Group 4) (1025)'


def task():
    global course1, course2, course3
    webdriver.DesiredCapabilities.EDGE['pageLoadStrategy'] = 'eager'
    driver = webdriver.Edge('./msedgedriver.exe')

    path = 'https://mis.uic.edu.cn/mis/student/es/eleDetail.do?id=2c9070d97ac93f45017acbd7459b006b'

    driver.get(path)

    # 获取checkbox并勾选
    driver.find_element(By.XPATH, "//*[@id='student']").click()
    # 找到密码输入框并输入密码
    elem = driver.find_element(By.ID, "j_username")
    elem.send_keys('s230026193')  # 填自己账号
    elem = driver.find_element(By.NAME, "j_password")
    elem.send_keys('Yq768140')
    driver.find_element(By.XPATH, "//*[@src='Skins/UIC/login_bt.png']").click()

    while True:
        try:
            driver.find_elements(By.TAG_NAME, "a")[3].click()
            driver.find_elements(By.TAG_NAME, "a")[-10].click()
            break
        except:
            driver.refresh()
            time.sleep(1)
            continue

    try:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Enter')))
        button.click()
        driver.switch_to.alert.accept()
    except Exception:
        print(Exception)

    while True:
        if course1:
            try:
                WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_element(By.XPATH, "//*[contains(text(),'Select Course / Item')]")).click()
                if driver.find_element(By.XPATH,"//*[contains(text(),'{}')]/../td[6]".format(course1name)).text == "Full":
                    course1 = False
                print(1)
                WebDriverWait(driver, 1, 0.2).until(lambda x: x.find_element(By.XPATH,"//*[contains(text(),'{}')]/../td[6]/a[2]".format(course1name))).click()

                driver.switch_to.alert.accept()

                WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_element(By.XPATH, '//*[@id="show_message_colse_button"]')).click()

                course1 = False
                print('success course1')


            except:
                driver.back()
                print("fail course1")
                time.sleep(1)

        if course2 and course1:
            continue

        if course2:
            try:
                WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_elements(By.XPATH, "//*[contains(text(),'Select Course / Item')]"))[0].click()

                WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_element(By.XPATH,"//*[contains(text(),'{}')]/../td[6]/a[2]".format(course2name))).click()

                driver.switch_to.alert.accept()

                WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_element(By.XPATH, '//*[@id="show_message_colse_button"]')).click()

                course2 = False
                print('success course2')


            except:
                driver.back()
                print('fail course2')
    time.sleep(320)

'''
        if course3 and course2:
            continue

        if course3:
            try:
                WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_element(By.XPATH, "//*[contains(text(),'Select Course / Item')]")).click()
                if driver.find_element(By.XPATH,"//*[contains(text(),'{}')]/../td[6]".format(course1name)).text == "Full":
                    course1 = False
                print(1)
                WebDriverWait(driver, 1, 0.2).until(lambda x: x.find_element(By.XPATH,"//*[contains(text(),'{}')]/../td[6]/a[2]".format(course1name))).click()

                driver.switch_to.alert.accept()

                WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_element(By.XPATH, '//*[@id="show_message_colse_button"]')).click()

                course3 = False
                print('success course3')


            except:
                driver.back()
                print("fail course3")
                time.sleep(1)
'''



if __name__ == '__main__':
    task()

    # sched_time = datetime.datetime(2021, 8, 8, 14, 00, 00)
    # loopflag = 0
    # # task()
    # while True:
    #     loopflag=1
    #     now = datetime.datetime.now()
    #     print(now)
    #     print(sched_time)
    #     if sched_time < now < (sched_time + datetime.timedelta(seconds=1)):
    #         loopflag = 1
    #     time.sleep(1)
    #     if loopflag == 1:
    #         task()  # 此处为你自己想定时执行的功能函数
    #         break
    #     loopflag = 0
