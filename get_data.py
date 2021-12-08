from bs4 import BeautifulSoup
import requests
import time
import os

# so we have to search a room in a specific location with specific requirements, all the specifications will
# be added in URL, and than we can copy that URL here
ZILLOW_URL = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%" \
             "22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.551775" \
             "35009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.85" \
             "1235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5" \
             "D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba" \
             "%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22" \
             "%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22" \
             "fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22" \
             "value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7" \
             "D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# your system's user_agent
header = {
    "User-Agent": os.environ.get("user_agent"),
    "Accept-Language": "en-US,en;q=0.9,ur;q=0.8",
}


class HouseSearch:
    def __init__(self):

        # if the zillow.txt is empty making a req to live web and creating a file, if not empty than reading from it.
        try:
            # now reading the data from txt file we've generated above
            with open(file="zillow.txt", mode="r", encoding="utf-8") as zt:
                self.content = zt.read()

        except FileNotFoundError:
            # requesting a live data from zillow web, than saving it in txt file, so we don't have to make requests
            # during testing
            response = requests.get(url=ZILLOW_URL, headers=header)
            web_content = response.text
            with open(file="zillow.txt", mode="w", encoding="utf-8") as zt:
                zt.write(web_content)
            time.sleep(2)
            with open(file="zillow.txt", mode="r", encoding="utf-8") as zt:
                self.gen_content = zt.read()

            self.soup = BeautifulSoup(self.gen_content, "lxml")
        else:
            self.soup = BeautifulSoup(self.content, "lxml")

    def search_links(self):

        # extracting the links of all the search results, and saving it in list_links
        self.search_link_results = self.soup.find(name='ul', class_="photo-cards photo-cards_wow photo-cards_short")
        list_links = [a["href"] for a in self.search_link_results.find_all("a", tabindex="0")]
        time.sleep(3)

        # Some links are broken so we have to add part of the url to them
        #   e.g. '/b/1450-castro-st-san-francisco-ca-5YVg2f/'
        #        should be 'https://www.zillow.com/b/1450-castro-st-san-francisco-ca-5YVg2f/'
        for index in range(len(list_links)):
            # if url is not starting with http then concatinate the partial url
            if not list_links[index].startswith("http"):
                list_links[index] = 'https://www.zillow.com' + list_links[index]
        return list_links

    def search_address(self):
        # extracting the addresses of all the search results
        addresses = self.search_link_results.find_all(name="address", class_="list-card-addr")
        list_address = [addr.text for addr in addresses]
        return list_address

    def search_price(self):
        # extracting prizes of all the search results, splitting it in order to get the prize only
        prices = self.search_link_results.find_all(class_="list-card-price")
        list_price = [price.text.split("/")[0] for price in prices]
        only_price = [p.split("+")[0] for p in list_price]
        return only_price