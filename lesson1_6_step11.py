from selenium import webdriver
import time

try:
    #link = "http://suninjuly.github.io/registration1.html" # ссылка для успешного прохождения
    link = "http://suninjuly.github.io/registration2.html" # ссылка для падения теста

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('div.first_block div.first_class input').send_keys('Ivan')
    input2 = browser.find_element_by_css_selector('div.first_block div.second_class input').send_keys('Petrov')
    input3 = browser.find_element_by_css_selector('div.first_block div.third_class input').send_keys('petrpetrov@gooogle.com')
    button = browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name("h1").text
    assert 'Congratulations!' in welcome_text

finally:
    time.sleep(3)
    browser.quit()
