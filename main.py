from get_data import HouseSearch
from form import FormFilling
import time
import os

# defining path of the driver
PATH = os.environ.get("your_driver_path")

# object of the classes
house_search = HouseSearch()
form_filling = FormFilling(path=PATH)

# methods of class, saving all the returning data in a form of list
list_urls = house_search.search_links()

all_address = house_search.search_address()

all_prices = house_search.search_price()

# now looping through each element of all the lists, in a range of length of list
for index in range(len(all_prices)):
    time.sleep(5)
    # filling a google form, for each entry, once all entries been filled we can check responses and click
    # excel icon on forms to generate a spreadsheet of all the data
    form_filling.open_form(url=list_urls[index], cost=all_prices[index], addr=all_address[index])
