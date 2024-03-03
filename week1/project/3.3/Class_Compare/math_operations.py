class Math_op:
    def __init__(self, value):
        self.value = value

    def equal(self, compare_to):
        return self.value == compare_to

    def greater_than(self, compare_to):
        return self.value > compare_to

    def smaller_than(self, compare_to):
        return self.value < compare_to

    def smaller_equal_than(self, compare_to):
        return self.value <= compare_to

    def greater_equal_than(self, compare_to):
        return self.value >= compare_to
