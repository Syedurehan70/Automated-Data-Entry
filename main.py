from get_data import HouseSearch
from form import FormFilling
import time
import lxml
import re

PATH = "C:/Users/syed usama rehan/chromedriver_win32/chromedriver.exe"

house_search = HouseSearch()
form_filling = FormFilling(path=PATH)

# methods of class
list_urls = house_search.search_links()
print(len(list_urls))

all_address = house_search.search_address()
print(len(all_address))

all_prices = house_search.search_price()
print(len(all_prices))

for index in range(len(all_prices)):
    time.sleep(5)
    form_filling.open_form(url=list_urls[index], cost=all_prices[index], addr=all_address[index])
