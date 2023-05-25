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

        self.car_title = []
        self.car_price = []
        self.car_link = []

    def open_browser(self):
        self.driver.maximize_window()
        self.driver.get('https://my.caredge.com/buy?inventoryType=used&priceRange=-16001&sortBy=dist&sortOrder=asc&start=0')
        time.sleep(10)

    def get_product_title(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='vehicle-card_detailsSection__o1SvU']/span/p")
        for content_title in elements:
            if content_title.text in self.car_title:
                continue
            self.car_title.append(content_title.text)
        return self.car_title

    def get_product_price(self):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='vehicle-card_priceSection__knSHH']//h2")
        for content_price in elements:
            if content_price.text in self.car_price:
                continue
            self.car_price.append(content_price.text)
        return self.car_price

    def get_product_link(self):
        self.link = self.driver.find_elements(By.XPATH, "//section[@class='vehicle-card_vehicleCardContainer___2DV3']/a")
        for x in self.link:
            if x in self.car_link:
                continue
            self.car_link.append(x.get_attribute('href'))
        time.sleep(5)
        self.driver.close()
        return self.car_link

    def product_file(self, car_title, car_price, car_link):
        filename = 'products.csv'
        with open(filename, "w", newline='') as file:
            file = open(filename, "w")
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(['Car Name', 'Car Price', 'Car Link'])
            writer.writerows(zip([car_title, car_price, car_link]))
            file.close()

            message = f">> Information about the car product is stored in {filename}\n"
            print(message)


if __name__ == '__main__':
    # `browser_type` and `service_path` vary depending on your setup.
    car = CarProductScrapper(service_path=Path.cwd(), browser_type=BrowserType.FIREFOX)
    car.open_browser()
    product_title = car.get_product_title()
    product_price = car.get_product_price()
    product_link = car.get_product_link()
    car.product_file(product_title, product_price, product_link)





