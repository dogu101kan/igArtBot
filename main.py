import random
from DallE import getImage
from InstagramSharing import posting
from userInfo import username, password
from userInfo import key
from ChatGPTAPI import caption
import time
import schedule
import time

words = [line.rstrip() for line in open('words.txt')]
wordsListLen = len(words)


def main_func():

    content = ""

    for k in range(4):
        content += words[random.randint(0, wordsListLen + 1)] + ", "

    try:
        getImage(caption(content, key) + "detailed, portrait, surrealism")
    except:
        print("Problem about getting image.")

    try:
        posting(username, password, content, key)
    except:
        print("Problem about posting.")

schedule.every(1).minutes.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)