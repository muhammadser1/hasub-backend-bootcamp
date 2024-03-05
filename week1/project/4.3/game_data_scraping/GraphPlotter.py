from matplotlib import pyplot as plt


class GraphPlotter:
    def __init__(self, tag_counts):
        self.tag_counts = tag_counts

    def convert_to_lists(self):
        x_axis = list(self.tag_counts.keys())
        y_axis = list(self.tag_counts.values())
        return x_axis, y_axis

    def plot(self, input=-1):
        x_axis, y_axis = self.convert_to_lists()
        bars = plt.bar(x_axis, y_axis)
        plt.xlabel('Tags')
        plt.ylabel('Count')
        plt.title('Tag Counts')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        if input != -1:
            bars[input].set_color('red')

        plt.show()
