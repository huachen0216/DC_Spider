# coding: utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

elem = driver.find_element_by_xpath('//*[@id="kw"]')
elem.send_keys("python selenium", Keys.ENTER)

print(driver.page_source)
