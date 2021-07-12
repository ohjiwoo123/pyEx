import time
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame("iframeResult") # 프레임 전환

elem = browser.find_element_by_xpath('//*[@id="male"]') # 성공

elem.click()

browser.switch_to.default_content() # 상위로 빠져 나옴

elem = browser.find_element_by_xpath('//*[@id="male"]') # 실패

time.sleep(5) #5초 대기 

browser.quit()

