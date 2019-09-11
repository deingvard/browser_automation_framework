from selenium.webdriver.common.by import By

from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator


class ShopByPage(BasePage):
    url = 'https://shop.by'

    @property
    def computers_button(self):
        locator = Locator(By.CSS_SELECTOR, "span[title='Компьютеры']")
        return BaseElement(self.driver, locator=locator)

    @property
    def laptops_button(self):
        locator = Locator(By.CSS_SELECTOR, "a[title='Ноутбуки']")
        return BaseElement(self.driver, locator=locator)

    @property
    def show_button_for_laptops(self):
        locator = Locator(By.XPATH, "//*[@id='Attr_prof_1000']//span[contains(text(), 'Показать')]")
        return BaseElement(self.driver, locator=locator)

    @property
    def set_option_lenovo(self):
        locator = Locator(By.XPATH, '//label[text()="Lenovo"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def set_option_dell(self):
        locator = Locator(By.XPATH, '//label[text()="Dell"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def set_option_hp(self):
        locator = Locator(By.XPATH, '//label[text()="HP"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def set_price_before(self):
        locator = Locator(By.XPATH, '//input[@name="price_before"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def set_price_after(self):
        locator = Locator(By.XPATH, '//input[@name="price_after"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def set_diagonal_min(self):
        locator = Locator(By.XPATH, '//input[@name="price_after"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def set_diagonal_max(self):
        locator = Locator(By.XPATH, '//input[@name="price_after"]')
        return BaseElement(self.driver, locator=locator)

    @property
    def show_button_for_diagonal(self):
        locator = Locator(By.XPATH, '(.//*[@data-idgroup="prof_5828"])[1]')
        return BaseElement(self.driver, locator=locator)
