from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'

    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_class_name('trollface').click()

    mew_window = browser.window_handles[1]
    browser.switch_to.window(mew_window)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    input1 = browser.find_element_by_name('text').send_keys(y)
    button2 = browser.find_element_by_css_selector('.btn.btn-primary').click()

    alert = browser.switch_to.alert.text
    print(alert)


finally:
    browser.quit()
