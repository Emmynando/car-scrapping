import csv
from enum import StrEnum, auto
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class BrowserType(StrEnum):
    CHROME = auto()
    FIREFOX = auto()
    EDGE = auto()
    SAFARI = auto()


class CarProductScrapper:

    # Class variables are available to the whole class.
    # Class variables beginning with an `_` are private by convention.
    _browser_to_driver_mapper = {
        BrowserType.CHROME: webdriver.Chrome,
        BrowserType.EDGE: webdriver.Edge,
        BrowserType.SAFARI: webdriver.Safari,
        BrowserType.FIREFOX: webdriver.Firefox,
    }

    def __init__(self, service_path: Path, browser_type: BrowserType):
        self.service = Service(str(service_path))
        # The following line is a little complicated, so I'm going to go through it,
        # we have defined `_browser_to_driver_mapper` above which maps the different
        # types of browsers to the required webdriver. We get the driver from the
        # dictionary and call it with `self._service`.
        self.driver = self._browser_to_driver_mapper[browser_type](service=self.service)

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
    # `browser_type` and `service_path` vary depending on your setup.
    car = CarProductScrapper(service_path=Path.cwd(), browser_type=BrowserType.FIREFOX)
    car.open_browser()
    product_titles = car.get_product_title()
    product_prices = car.get_product_price()
    product_links = car.get_product_link()
    car.close_browser()

    zipped_data = zip(product_titles, product_prices, product_links)
    write_car_data_to_csv("products.csv", zipped_data)





