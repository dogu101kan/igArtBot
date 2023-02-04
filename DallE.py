import openai
import urllib.request

from userInfo import key


openai.api_key = key
openai.Model.list()


def download_image(url):
        name = 0
        fullname = str(name)+".jpg"
        urllib.request.urlretrieve(url,fullname)   


def getImage(content):
    response = openai.Image.create(
        prompt = content, 
        n = 1,
        size = "1024x1024"
    )

    download_image(response.data[0].url)