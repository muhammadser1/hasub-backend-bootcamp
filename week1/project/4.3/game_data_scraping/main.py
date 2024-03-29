from Url_Scraper import *
from GameDetails import *
from GraphPlotter import *
from User_interaction import *

if __name__ == "__main__":
    # fetches and parses HTML content from the Steam website, and then extracts the names and descriptions of new releases from the parsed HTML
    steam_url = Url_Scraper("https://store.steampowered.com/")
    steam_url.fetch_data()
    steam_url.parse_html()
    game_details_dict = steam_url.extract_name_and_description()

    # populates it with game details, prints the details of the games, and generates tag counts from the game descriptions.
    game_details = GameDetails(game_details_dict)
    game_details.fill_names_details()
    game_details.print_details()
    tag_counts = game_details.generate_tag_counts()

    graph_plotter = GraphPlotter(tag_counts)

    user = UserInteraction(tag_counts)
    tag_name = user.get_input_from_user()
    user.print_max()

    graph_plotter.plot(int(tag_name))
