class UserInteraction:
    def __init__(self, tag_counts):
        self.tag_counts = tag_counts

    def print_max(self):
        Keymax = max(zip(self.tag_counts.values(), self.tag_counts.keys()))[1]
        print("\nThe max tag is", Keymax, "with a value of:", self.tag_counts[Keymax])

    def get_input_from_user(self):
        for i, (k, v) in enumerate(self.tag_counts.items()):
            print(i, ".", k, v, end="           ")
            if i % 5 == 4:
                print("\n")
        tag_name = input("Please type the tag number: ")
        return tag_name
