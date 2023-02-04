"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

dc_url = 'https://discord.com/login?redirect_to=%2Fchannels%2F1069576324177465444%2F1069576324177465447'


driver = webdriver.Chrome(executable_path="C:/Users/doguk/Drivers/chromedriver.exe")
driver.get(dc_url)


mail = '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input'
password = driver.find_element("name", "password")
#textArea = '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[3]/div/div[2]/div/span/span/span'

time.sleep(10)

driver.find_element('xpath', mail).send_keys("dogukan_gazel@windowslive.com")
time.sleep(1)
password.send_keys("gazel123")
password.send_keys(Keys.ENTER)
time.sleep(10)

driver.find_element(By.CLASS_NAME, "slateTextArea-27tjG0").send_keys("/imagine ", Keys.ENTER)
#driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[3]/div/div[2]').send_keys("/imagine ", Keys.ENTER)
#driver.find_element('xpath', textArea).send_keys("/imagine")
# driver.find_element('xpath', textArea).send_keys(Keys.ENTER)
# time.sleep(2)
# driver.find_element('xpath', textArea).send_keys("house, car")
time.sleep(50)

"""

