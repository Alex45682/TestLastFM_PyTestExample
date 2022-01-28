import pytest
from tests.main_page_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestMainPage:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.homepage_nav = HomepageNav(self.driver)

    def test_01_check_top_artists(self):
        text = self.homepage_nav.get_element_text('xpath', self.homepage_nav.fav_artists)
        for artist in ['The Hardkiss', 'Grimes', 'Aurora', 'Lana Del Rey', 'Infected Mushroom']:
            assert artist in text, "You haven't listened to the artist {} for a long time".format(artist)

    def test_02_check_top_recent_artist_length(self):
        text_len = self.homepage_nav.get_element_text('xpath', self.homepage_nav.recent_artists).__len__()
        expected_length = 50
        assert text_len == expected_length, \
            "Actual length of recent artists {} is not equal to expected {}".format(text_len, expected_length)

    def test_03_navigate_loved_tracks_page(self):
        text = "Loved Tracks"
        loved_button = self.homepage_nav.is_present('xpath', self.homepage_nav.header_tabs[0] % text)
        self.homepage_nav.click_element(loved_button)
        self.homepage_nav.is_visible('xpath', self.homepage_nav.loved_tracks_title[0] % text)

    def test_04_check_loved_tracks(self):
        text = "Loved Tracks"
        loved_button = self.homepage_nav.is_present('xpath', self.homepage_nav.header_tabs[0] % text)
        self.homepage_nav.click_element(loved_button)
        self.homepage_nav.is_visible('xpath', self.homepage_nav.loved_tracks_title[0] % text)
        loved_artists = self.homepage_nav.get_element_text('xpath', self.homepage_nav.loved_artists)
        for artist in ["Foo Fighters", "Cream", "a-ha", "Coldplay", "Moby", "Talking Heads", "The Smiths"]:
            assert artist in loved_artists, \
                "Artist {} is not presents in loved artists list {}".format(artist, loved_artists)
