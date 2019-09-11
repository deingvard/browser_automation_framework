from pages.trial_page import TrialPage
from pages.training_group_page import TrainingGroupPage
from pages.shop_by_page import ShopByPage


# Trial Page
def test_trial_page(chrome_browser):
    trial_page = TrialPage(driver=chrome_browser)
    trial_page.go()
    trial_page.stone_input.input_text("rock")
    trial_page.stone_button.click()
    print("1-st test done")


# Training Grounds
def test_training_page(app):
    trng_page = TrainingGroupPage(driver=app)
    trng_page.go()
    assert trng_page.button1.text == 'Button1', "Unexpected button1 text"
    trng_page.button1.click()
    print("2-d test done")


# Training Grounds
def test_shop_by_page(app):
    shop_by_page = ShopByPage(driver=app)
    shop_by_page.go()
    shop_by_page.computers_button.click()
    shop_by_page.laptops_button.click()

    # Set price
    shop_by_page.set_price_before.input_text("750")
    shop_by_page.set_price_after.input_text("1500")

    # Set laptop
    shop_by_page.show_button_for_laptops.click()
    shop_by_page.set_option_dell.click()
    shop_by_page.set_option_lenovo.click()
    shop_by_page.set_option_hp.click()
    # app.quit()
    # time.sleep(3)
    #
    # # Set diagonal
    # time.sleep(10)

    # shop_by_page.show_button_for_diagonal.scroll_to_elem()
    # shop_by_page.show_button_for_diagonal.click()
