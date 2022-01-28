from selenium.webdriver.common.by import By as by
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 7)

    @staticmethod
    def get_element_by(find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'xpath': by.XPATH,
                    'id': by.ID,
                    'name': by.NAME,
                    'class_name': by.CLASS_NAME
                    }
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((
            self.get_element_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((
            self.get_element_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((
            self.get_element_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((
            self.get_element_by(find_by), locator[0])), locator[1])

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((
            self.get_element_by(find_by), locator)), locator_name)

    @staticmethod
    def get_text_from_webelements(elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    @staticmethod
    def get_element_by_text(elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def click_element(self, element):
        element.click()

