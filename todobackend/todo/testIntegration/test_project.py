import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class AdminCSSTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.chrome_options = Options()
        cls.chrome_options.add_argument('--headless')
        cls.chrome_options.add_argument('--no-sandbox')
        cls.chrome_options.add_argument('--disable-dev-shm-usage')
        cls.selenium = webdriver.Chrome(options=cls.chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_site_load_or_crash(self):
        print(self)
        urls_to_check = [self.live_server_url,
                         f"{self.live_server_url}/admin/",
                         f"{self.live_server_url}/api/tag/",
                         f"{self.live_server_url}/api/todo/"]

        for url in urls_to_check:
            self.selenium.get(url)
            try:
                body_element = self.selenium.find_element(By.TAG_NAME, "body")
            except NoSuchElementException:
                body_element = None
            self.assertIsNotNone(body_element,
                                 f"Site crashed or failed to load at {url}")
            time.sleep(30)