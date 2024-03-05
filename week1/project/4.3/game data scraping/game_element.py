import plot_tags
import json

from bs4 import BeautifulSoup

def fill_names_details(game_content,soup):
    items_names = soup.findAll(class_="tab_item_name")
    target_div_list = soup.findAll(class_="tab_item_content")
    for i in range(len(items_names)):
        description=""
        target_div = target_div_list[i].find('div', class_='tab_item_top_tags')
        target_div = target_div.findAll('span')
        for j in range(len(target_div)):
            description+=target_div[j].text
        game_content[items_names[i].text] = {"len":len(target_div),"Info":description}
def print_vedio_game(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    for game_name, game_info in data.items():
        print("Game: ",game_name,"    ","Info: ",game_info["Info"],"\n")

def html_extract_game(response): ## main of game_element
    game_content = {}
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find(class_="tab_content", id="tab_newreleases_content")
    fill_names_details(game_content,soup)
    file_path = "data.json"
    with open(file_path, 'w') as json_file:
        json.dump(game_content, json_file, indent=4)
    print_vedio_game(file_path)
    plot_tags.main()
