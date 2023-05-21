import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PATH ='C:\Program Files (x86)\chromedriver.exe'

# service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.maximize_window()
# driver.get('https://my.caredge.com/buy?inventoryType=used&priceRange=-16001&sortBy=dist&sortOrder=asc&start=0')
# time.sleep(5)
# title = driver.find_element(By.CLASS_NAME, "vehicle-card_detailsSection__o1SvU")
# title = driver.find_elements(By.XPATH, "//div[@class='vehicle-card_detailsSection__o1SvU']")
# content = "".join([element.text for element in title])
# print(content)

# time.sleep(5)
# driver.close()


class CarProductScrapper:
    def __init__(self):
        self.car_title = []
        self.car_price = []
        self. car_link = []
    

    def open_browser(self):
        self.service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service_obj)
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
    car = CarProductScrapper()
    car.open_browser()
    product_title = car.get_product_title()
    product_price = car.get_product_price()
    product_link = car.get_product_link()
    car.product_file(product_title, product_price, product_link)





