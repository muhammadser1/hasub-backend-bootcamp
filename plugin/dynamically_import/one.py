class Plugin:
    def __init__(self, *args):
        print("Plugin 1 ", args)

    def execute(self, a, b):
        print(a + b)
