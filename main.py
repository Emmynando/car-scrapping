import csv
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class CarProductScrapper:

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        self.driver.maximize_window()
        self.driver.get('https://my.caredge.com/buy?inventoryType=used&priceRange=-16001&sortBy=dist&sortOrder=asc&start=0')
        time.sleep(10)

    def get_product_title(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='vehicle-card_detailsSection__o1SvU']/span/p")
        return [content_title.text for content_title in elements]

    def get_product_price(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='vehicle-card_priceSection__knSHH']//h2")
        return [content_price.text for content_price in elements]

    def get_product_link(self):
        elements = self.driver.find_elements(By.XPATH, "//section[@class='vehicle-card_vehicleCardContainer___2DV3']/a")
        return [element.get_attribute("href") for element in elements]

    def close_browser(self):
        time.sleep(5)
        self.driver.close()


def write_car_data_to_csv(file_name, car_data):
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Car Name", "Car Price", "Car Link"])
        writer.writerows(car_data)
        print(f">> Information about the car product is stored in {file_name}")


if __name__ == '__main__':
    # I have my driver in the current working directory i.e. `Path.cwd()` this
    # will probably be different for you
    service = Service(str(Path.cwd()))

    # I'm using firefox, change this to the correct driver
    browser_driver = webdriver.Firefox(service=service)

    car_scrapper = CarProductScrapper(driver=browser_driver)
    car_scrapper.open_browser()
    product_titles = car_scrapper.get_product_title()
    product_prices = car_scrapper.get_product_price()
    product_links = car_scrapper.get_product_link()
    car_scrapper.close_browser()

    zipped_data = zip(product_titles, product_prices, product_links)
    write_car_data_to_csv("products.csv", zipped_data)





