import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class AdminCSSTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Use the appropriate webdriver

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_site_load_or_crash(self):
        urls_to_check = [self.live_server_url,
                         f"{self.live_server_url}/admin/",
                         f"{self.live_server_url}/tag/"]

        for url in urls_to_check:
            self.selenium.get(url)
            try:
                body_element = self.selenium.find_element(By.TAG_NAME, "body")
            except NoSuchElementException:
                body_element = None
            self.assertIsNotNone(body_element,
                                 f"Site crashed or failed to load at {url}")

            time.sleep(30)
