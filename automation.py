#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          Automation Bot Data Entry                            # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Chromedriver Setup:                                                                   #
# Verify chromedriver path below: C:/path/to/chromedriver.exe                           #
# if not get latest stable Chromedriver: https://sites.google.com/chromium.org/driver   #
# Update Chrome Browser to latest: chrome://settings/help                               #
# On Windows add chromedriver path to Environmental Variables/System Variables          #
#                                                                                       #
# Launch Instructions:                                                                  #
# Rename project folder to your preference: automation-bot-data-entry                   #
# Change path to project folder: cd automation-bot-data-entry                           #
# Create virtual environment: virtualenv venv                                           #
# Activate virtual enviornment: venv\scripts\activate                                   #
# Batch install all requirements: pip install -r requirements.txt                       #
# Launch by clicking run button in top right in VSCode or: py -3 automation.py          #
#########################################################################################

import time
from selenium import webdriver


chrome_browser = webdriver.Chrome(
    executable_path='C:/path/to/chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('Data Entry Text 123456789')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'Data Entry Text 123456789' in output_message.text


# Other Automation Operations
# driver.get('http://www.google.com/')
# time.sleep(5)
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()
