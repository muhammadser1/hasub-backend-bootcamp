class Plugin:
    def __init__(self, *args):
        print("Plugin 2 ", args)

    def execute(self, a, b):
        print(a - b)
