import matplotlib.pyplot as plt


class GraphPlotter:
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c

    def plot_asteroid_data(self, data): ##Printing only a fraction (1/10) of the total length of the list because displaying all values on the graph would result in overcrowding and reduce readability.
        """Plot various graphs related to asteroid data.

        Args:
            data (list): A list of dictionaries containing asteroid data.
        """
        min_diamete = []
        velocity = []
        miss_distance = []
        max_diameter = []
        danger=[]
        name=[]
        total_data = len(data)
        quarter_data = data[:total_data // 10]
        for asteroid in quarter_data:
            min_diamete.append(asteroid["est diameter min"])
            velocity.append(asteroid["relative_velocity"])

            miss_distance.append(asteroid["miss_distance"])
            max_diameter.append(asteroid["est diameter max"])

            danger.append(self.calculate_the_danger(asteroid))
            name.append(asteroid["name"])
        self.plot_graph(min_diamete, velocity, "min_diamete vs velocity", "est diameter min", "relative_velocity")
        self.plot_graph(miss_distance, max_diameter, "miss_distance vs max_diameter", "miss_distance", "max_diameter")
        self.plot_graph(name,danger,"danger index of each asteroid","name","danger")
    def calculate_the_danger(self, asteroid):
        """Calculate the danger index of an asteroid

        Args:
            asteroid : A dictionary containing asteroid data.

        Returns:
            float: The calculated danger index of the asteroid.
        """
        avg_diameter = (float(asteroid['est diameter min']) + float(asteroid['est diameter max'])) / 2
        relative_speed = float(asteroid['relative_velocity'])
        miss_distance = float(asteroid['miss_distance'])
        return self.a * avg_diameter + self.b * relative_speed / self.c * miss_distance

    def plot_graph(self, x_axis, y_axis, title, x_title, y_title):
        """Plot a graph.

        Args:
            x_axis (list): The x-axis data.
            y_axis (list): The y-axis data.
            title (str): The title of the graph.
            x_title (str): The label for the x-axis.
            y_title (str): The label for the y-axis.
        """
        plt.scatter(x_axis, y_axis)
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        plt.title(title)
        plt.show()
