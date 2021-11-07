from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    inp = browser.find_element_by_class_name('form-control')
    inp.send_keys(y)

    button1 = browser.find_element_by_class_name('form-check-input')
    button1.click()
    button2 = browser.find_element_by_id('robotsRule')
    button2.click()
    button3 = browser.find_element_by_xpath(
        '/html/body/div[1]/form/button'
        )
    button3.click()
finally:
    time.sleep(10)
    browser.quit()
