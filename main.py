import csv, os

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


class CarProductScrapper():
    def __str__(self):
        self.car_title = None
        self.car_price = None
        self.car_link = None
    

    def open_browser(self):
        self.service_obj = Service("C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service_obj)
        self.driver.maximize_window()
        self.driver.get('https://my.caredge.com/buy?inventoryType=used&priceRange=-16001&sortBy=dist&sortOrder=asc&start=0')
        time.sleep(10)
    
    def get_product_title(self):
        car_title =[]
        # self.title = self.driver.find_elements(By.CLASS_NAME, "vehicle-card_detailsSection__o1SvU")
        self.title = self.driver.find_elements(By.XPATH, "//div[@class='vehicle-card_detailsSection__o1SvU']/span/p")
        for content_title in self.title:
        # content_title = "".join([str(element.text) for element in self.title])
            car_title.append(content_title.text)
            yield(car_title)
    

        # time.sleep(5)
    # def get_product_price(self):
    #     car_price =[]
    #     self.price = self.driver.find_elements(By.XPATH, "//div[@class='vehicle-card_priceSection__knSHH']//h2")
    #     for content_price in self.price:
        # content_price = "".join([element.text for element in self.price])
            # car_price.append(content_price.text)
            # yield(car_price)

    #     time.sleep(5)
    
    # def get_product_link(self):
    #     car_link =[]
    #     self.link = self.driver.find_elements(By.XPATH, "//section[@class='vehicle-card_vehicleCardContainer___2DV3']/a")
    #     for x in self.link:
    #         car_link.append(x.get_attribute('href'))
    #         yield(car_link)

        time.sleep(5)
        self.driver.close()
    
    # def product_file(self, car_title, car_price, car_link):
    #     filename = 'products.csv'
    #     file = open(filename, "w", newline='')
    #     reader = csv.writer(file, delimiter='\t')
    #     reader.writerow(['Car Name', 'Car Price', 'Car Link'])
    #     for row in zip(car_title, car_price, car_link):
    #         reader.writerows(row)
        # reader.writerows(zip([car_title, car_price, car_link]))
        # file.close()

        # message = f">> Information about the car product is stored in {filename}\n"
        # print(message)

        # os.startfile(filename)



if __name__ == '__main__':
    car = CarProductScrapper()
    car.open_browser()
    product_title = car.get_product_title()
    # print(product_title)
    # product_price = car.get_product_price()
    # product_link = car.get_product_link()
    # car.product_file(product_title, product_price, product_link)



            # x.get_attribute('href')
            # car_link.append[x]
            # print(type(x))
            # print(x.get_attribute('href'))
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "Used"))
#     )
#     element.click()
# except:
#     driver.quit()
# search.send_keys(Keys.RETURN)



