import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


# driver = webdriver.Firefox()


class WebpageTests(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_title(self):
        self.driver.get(file_uri("counter.html"))
        self.assertEqual(self.driver.title, "Counter")

    def test_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(self.driver.find_element_by_tag_name("h1").text, "1")

    def test_decrease(self):
        self.driver.get(file_uri("counter.html"))
        decrease = self.driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(self.driver.find_element_by_tag_name("h1").text, "-1")

    def test_multiple_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(self.driver.find_element_by_tag_name("h1").text, "3")

    def tearDown(self):
        self.driver.stop_client()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
