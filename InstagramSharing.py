from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from ChatGPTAPI import caption



def posting(username, password, content, key):
    
    driver = webdriver.Chrome(executable_path=os.getcwd() + "/Drivers/chromedriver.exe")
    driver.get("https://www.instagram.com")
    driver.set_window_size(800, 600)

    notificationCloseButton = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
    notificationSaveAccButton = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button'
    posting1 = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div/div[1]/div/div'
    posting2 = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input'
    posting3Forward = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'
    posting4Forward = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'
    posting5TextArea = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea'
    posting6Share = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button'
    postingDone = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span'
    closeSection = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/svg'

    time.sleep(5)

    usernameInput = driver.find_element("name", "username")
    passwordInput = driver.find_element("name", "password")


    usernameInput.send_keys(username)
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.ENTER)
    time.sleep(10)

    try:
        driver.find_element('xpath', notificationCloseButton).click()
        time.sleep(10)
    except:
        driver.find_element('xpath', notificationSaveAccButton).click()
        time.sleep(10)
        driver.find_element('xpath', notificationCloseButton).click()
        time.sleep(10)

    driver.find_element('xpath', posting1).click()
    time.sleep(10)
    driver.find_element('xpath', posting2).send_keys(os.getcwd() + "/0.jpg")
    time.sleep(2)
    driver.find_element('xpath', posting3Forward).click()
    time.sleep(1)
    driver.find_element('xpath', posting4Forward).click()
    time.sleep(1)
    prompt = caption(content, key)
    print(prompt)
    driver.find_element('xpath', posting5TextArea).send_keys(prompt)
    time.sleep(1)
    driver.find_element('xpath', posting6Share).click()
    time.sleep(60)
    
    counter = 0
    while counter < 20:

        try:
            driver.find_element('xpath', postingDone)
            break
        except:
            if counter !=9:
                print("Not done yet.")
                time.sleep(10)
            else:
                print("Posting Error.")
            counter +=1

    counter = 0

    driver.quit()
