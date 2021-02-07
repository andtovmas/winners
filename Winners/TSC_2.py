import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Add_Bookmakers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        print('Add bookmakers in comparison chart with "bonus comparison"')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://winners.net/")

        time.sleep(2)

        compar = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/header/div[2]/a[3]').click()

        addCompar = driver.find_element_by_xpath(
            '//*[@id="MainContent"]/div[2]/div[2]/div/div[1]/div[4]').click()
        fullReview = driver.find_element_by_xpath(
            '//*[@id="MainContent"]/div[2]/div[2]/div/div[2]/a[1]').click()

        driver.implicitly_wait(15)
        bonusCompar = driver.find_element_by_xpath(
            '/html/body/div/div/main/div[3]/div[1]/div[4]/a').click()

        # check the expected result

        if driver.find_elements_by_xpath("//*[@id='MainContent']/div[2]/div[1]/div[1]/div[2]/div").__contains__('Betway'):

            print(
                'The bookmaker must be added to the comparison chat where bookmakers have already been added')

        else:
            print('A new bookmaker is added but the previous one is deleted')

    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()
