import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Routing_from_list(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        print('Сheck the bookmakers full review routing from  list section')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://winners.net/")

        time.sleep(2)

        comparis = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/header/div[2]/a[3]').click()

        listButton = driver.find_element_by_xpath(
            '//*[@id="MainContent"]/div[1]/div[1]/button[1]').click()

        fullReview = driver.find_element_by_xpath(
            '//*[@id="MainContent"]/div[2]/div[2]/div[1]/a[1]').click()

        driver.back()
        time.sleep(3)

        if driver.find_elements_by_xpath("//*[@id='MainContent']/div[2]/div[1]/div[3]").__contains__('Score'):

            print('The user should return to the page with the  open  list section ')

        else:
            print('The user is returned to the page with the selected comparison section')

    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()
