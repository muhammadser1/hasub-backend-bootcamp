import requests
from bs4 import BeautifulSoup


class Url_Scraper:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None

    def fetch_data(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            print("Success to fetch data from the Steam store.")
        else:
            print("Failed to fetch data from the Steam store.")

        return self.response

    def parse_html(self):
        if self.response is None:
            print("Data not fetched")
        else:
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
        return self.soup

    def extract_name_and_description(self): # extract the titles and descriptions
        if self.soup is None:
            print("HTML not parsed.")
            return None
        else:
            new_releases_section = self.soup.find(class_="tab_content", id="tab_newreleases_content")
            if new_releases_section is None:
                print("New releases section not found in HTML.")
                return None
            items_names = new_releases_section.findAll(class_="tab_item_name")  # 30
            target_div_list = new_releases_section.findAll(class_="tab_item_content")
            print(items_names)
            return extract_game_details(items_names, target_div_list)


def extract_game_details(items_names, target_div_list): # this function extracts  details about each gamebased on the provided HTML elements and organizes this information into a dictionary.
    game_content = {}
    for i in range(len(items_names)):
        description = ""
        target_div = target_div_list[i].find('div', class_='tab_item_top_tags')
        target_div = target_div.findAll('span')
        for j in range(len(target_div)):
            description += target_div[j].text
        game_content[items_names[i].text] = {"len": len(target_div), "Info": description}
    return game_content
