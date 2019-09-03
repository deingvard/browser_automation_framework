from selenium import webdriver

from pages.training_group_page import TrainingGroupPage
from pages.trial_page import TrialPage

# Test Setup
browser = webdriver.Chrome(executable_path='/Users/admin/Downloads/chromedriver')

# Trial Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()

# input()

# Training Grounds
trng_page = TrainingGroupPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1', "Unexpected button1 text"
trng_page.button1.click()

# input()

browser.quit()
