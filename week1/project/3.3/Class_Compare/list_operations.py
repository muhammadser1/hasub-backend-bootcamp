class List_op:
    def __init__(self, value):
        self.value = value

    def is_value_in_nested_list(self, nested_list):
        for element in nested_list:
            if isinstance(element, list):
                if self.is_value_in_nested_list(element):
                    return True
            if element == self.value:
                return True
        return False
