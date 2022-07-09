#selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#웹 드라이버관련
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#chromedriver
chromedriver = '/Users/kimyoungbin/coding/jupyter_high_cralwing_inflearn/chromedriver'
#options
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
options.add_argument(f"User-Agent:{user_agent}")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(service=Service(chromedriver), options=options)
driver.get('https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NTBQS660DQ1WSwYSLmoFQNn0NNuyxKLM1JLEHLX8ohRbtfykSlu1YtvkRABJgRN3')

time.sleep(3)
# elem = driver.find_element(By.CSS_SELECTOR,'div.navigationItem__navigationItem--3oq_b span')
for i in range(1,10):
    time.sleep(1)
    # driver.execute_script(f"window.scrollTo(0, {i*401.5})")
    driver.execute_script(f"window.scrollTo(0, {i*800})")

time.sleep(5)
elems = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoVintage__truncate--3QAtw')
print("title : ",len(elems))

elems_img = driver.find_elements(By.CSS_SELECTOR,'div.wineCard__bottleSection--3Bzic div[role="img"]')


origins = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoLocation__regionAndCountry--1nEJz')
prices = driver.find_elements(By.CSS_SELECTOR,
                              'div.addToCart__subText--1pvFt.addToCart__ppcPrice--ydrd5')


print("img_src: ",len(elems_img))
for i,v in enumerate(elems_img):
    print(f"{i}.",v.get_attribute("style")[25:-3])
    # print(i.get_attribute("src"))

for i,v in enumerate(elems):
    print(f"{i}.",v.text)
    
for i,v in enumerate(origins):
    print(f"{i}.",v.text)
    
for i,v in enumerate(prices):
    print(f"{i}.",v.text)

# print(elems[78].text)
# print(elems_img[39].get_attribute("style"))


# print(elems[102].text)
# print(elems_img[51].get_attribute("style"))


# print(elems[90].text)
# print(elems_img[45].get_attribute("style"))


# print(elems[394].text)
# print(elems_img[197].get_attribute("style"))

time.sleep(1000)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(5)

# elems = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoVintage__truncate--3QAtw')
# print(len(elems))

# elems_img = driver.find_elements(By.XPATH,"//div[@role='img']")
# print(len(elems_img))

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(5)

# elems = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoVintage__truncate--3QAtw')
# print(len(elems))

# elems_img = driver.find_elements(By.XPATH,"//div[@role='img']")
# print(len(elems_img))

time.sleep(1000)

# elems = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoVintage__truncate--3QAtw')

# print(len(elems))

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# time.sleep(10)

# elems = driver.find_elements(By.CSS_SELECTOR,'div.wineInfoVintage__truncate--3QAtw')

# print(len(elems))

# for elem in elems:
#     print(elem.text)



