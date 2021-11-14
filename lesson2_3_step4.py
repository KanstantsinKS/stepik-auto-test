from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'

    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('.btn').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    input1 = browser.find_element_by_name('text').send_keys(y)
    button2 = browser.find_element_by_css_selector('.btn.btn-primary').click()

    alert = browser.switch_to.alert.text
    print(alert)

finally:
    time.sleep(3)
    browser.quit()
