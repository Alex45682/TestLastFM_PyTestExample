from base.base_page import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils


class HomepageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.recent_artists = ("//section[@id='recent-tracks-section']//td[@class='chartlist-artist']/a",
                               'Recent artists')
        self.fav_artists = ("//div[@class='grid-items-item-details']//a", "Top artists list")
        self.header_tabs = ("//div[@class='header-info-primary-col1']//a[contains(text(), '%s')]",
                            "Header Navigation tabs")
        self.loved_tracks_title = ("//h1[@class = 'content-top-header' and contains(text(), '%s')]",
                                   "Loved Tracks title")
        self.loved_artists = ("//td[@class='chartlist-artist']", "Loved artists list")

    def get_element(self, find_by: str, locator) -> List[WebElement]:
        return self.are_visible(find_by, locator)

    def get_element_text(self, find_by: str, locator, return_as_str=False):
        nav_links = self.get_element(find_by, locator)
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text) if return_as_str else nav_links_text


