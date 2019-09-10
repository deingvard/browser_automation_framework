from pages.trial_page import TrialPage
from pages.training_group_page import TrainingGroupPage


# Trial Page
def test_trial_page(chrome_browser):
    trial_page = TrialPage(driver=chrome_browser)
    trial_page.go()
    trial_page.stone_input.input_text("rock")
    trial_page.stone_button.click()
    print("1-st test done")


# Training Grounds
def test_training_page(chrome_browser):
    trng_page = TrainingGroupPage(driver=chrome_browser)
    trng_page.go()
    assert trng_page.button1.text == 'Button1', "Unexpected button1 text"
    trng_page.button1.click()
    print("2-d test done")
    chrome_browser.quit()

