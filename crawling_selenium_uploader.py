#selenium
from selenium                           import webdriver
from selenium.webdriver.common.keys     import Keys

#web_driver
from selenium.webdriver.common.by       import By
from selenium.webdriver.chrome.service  import Service
from webdriver_manager.chrome           import ChromeDriverManager

from my_settings                        import (user_agent,
                                                chromedriver_saved_place)
import re,time

#for uploader
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HangOver_refactoring.settings')
django.setup()
from products.models import *


#chromedriver
chromedriver = chromedriver_saved_place
#options
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument(f"User-Agent:{user_agent}")
# options.add_argument("lang=ko_KR")

#generate chrome driver
driver = webdriver.Chrome(service=Service(chromedriver), options=options)

URL_by_Category = {
    1:"https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NQABteRKW-8gtWQgEa5WAFSQnmZblliUmVqSmKOWX5Rim5JanKyWn1RpW5RYkpmXXhyfnF-aV6JWXhIda2sIAEepG8A%3D",
    2:"https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NQABteRKW-8gtWQgEa5WAFSQnmZblliUmVqSmKOWX5Rim5JanKyWn1RpW5RYkpmXXhyfnF-aV6JWXhIda2sEAEeqG8E%3D",
    3 :"https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NQABteRKW-8gtWQgEa5WAFSQnmZblliUmVqSmKOWX5Rim5JanKyWn1RpW5RYkpmXXhyfnF-aV6JWXhIda2sMAEerG8I%3D",
    4 :"https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NQABteRKW-8gtWQgEa5WAFSQnmZblliUmVqSmKOWX5Rim5JanKyWn1RpW5RYkpmXXhyfnF-aV6JWXhIda2sCAEesG8M%3D",
    5 : "https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NQABteRKW-8gtWQgEa5WAFSQnmZblliUmVqSmKOWX5Rim5JanKyWn1RpW5RYkpmXXhyfnF-aV6JWXhIda2sOAEevG8Y%3D",
    6 : "https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NQABteRKW-8gtWQgEa5WAFSQnmZblliUmVqSmKOWX5Rim5JanKyWn1RpW5RYkpmXXhyfnF-aV6JWXhIda2tkAgBjnxv1",
}

Product_list=[]

#FOR문으로 돌리면 크롤링을 막아버림 비비노 사이트에서.. 그래서 일일이 해주는 수밖에 없다.
#나중에 button.click()과 같은 방식을 한번 생각해보는 것도 낫벳 > 실패.. 안됨
key = 1
value = URL_by_Category[key]


#start crwaling
driver.get(value)

#wait for loading 
time.sleep(7)

for i in range(1,350):
    time.sleep(1.5)
    driver.execute_script(f"window.scrollTo(0, {i*800})")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

names = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoVintage__truncate--3QAtw:not(div.wineInfoVintage__vintage--VvWlU)')

explanations = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoVintage__vintage--VvWlU')

images = driver.find_elements(By.CSS_SELECTOR,'div.wineCard__bottleSection--3Bzic div[role="img"]')

origins = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoLocation__regionAndCountry--1nEJz')

prices = driver.find_elements(By.CSS_SELECTOR,'div.addToCart__subText--1pvFt.addToCart__ppcPrice--ydrd5')

ratings = driver.find_elements(By.CSS_SELECTOR,'div._19ZcA')

for index,value in enumerate(names):
    img = images[index].get_attribute("style")[25:-3]
    if len(img) > 50:
        Product_list.append(
            Product(
                name = names[index].text,
                explanation = explanations[index].text,
                img_url = img,
                origin = origins[index].text.split(',')[1].strip(' '),
                price = int(round(float(re.sub(',','',(prices[index].text[23:]))),0)),
                rating = ratings[index].text,
                category_id = key,
            )
        )
    
driver.quit()
print(f"{key} finished!")
    
Product.objects.bulk_create(Product_list)




##for test --------------------------------

# print("-----------------------------------------------------------")
# print("title!")
# print("-----------------------------------------------------------")
# for i,v in enumerate(titles):
#     print(f"{i}.",v.text)


# print("-----------------------------------------------------------")
# print("title!")
# print("-----------------------------------------------------------")
# for i,v in enumerate(descriptions):
#     print(f"{i}.",v.text)


# print("-----------------------------------------------------------")
# print("elems_img!")
# print("-----------------------------------------------------------")
# for i,v in enumerate(images):
#     img = v.get_attribute("style")[25:-3]
#     print(f"{i}.",img,"length : ",len(img))

# print("-----------------------------------------------------------")
# print("origins!")
# print("-----------------------------------------------------------")
# for i,v in enumerate(origins):
#     print(f"{i}.",v.text.split(',')[1].strip(' '))

# print("-----------------------------------------------------------")
# print("prices!")
# print("-----------------------------------------------------------")    
# for i,v in enumerate(prices):
#     print(f"{i}.",int(round(float(re.sub(',','',(v.text[23:]))),0)))

# print("-----------------------------------------------------------")
# print("ratings!")
# print("-----------------------------------------------------------")
# for i,v in enumerate(ratings):
#     print(f"{i}. rating!",v.text)

