from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element_by_id('treasure')
    x = picture.get_attribute('valuex')
    y = calc(int(x))
    inp = browser.find_element_by_tag_name('input')
    inp.send_keys(y)

    button1 = browser.find_element_by_id('robotCheckbox')
    button1.click()
    button2 = browser.find_element_by_id('robotsRule')
    button2.click()
    button3 = browser.find_element_by_tag_name('button')
    button3.click()
finally:
    time.sleep(10)
    browser.quit()
