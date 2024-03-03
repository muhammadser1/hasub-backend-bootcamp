class Dict_op:
    def __init__(self, value):
        self.value = value

    def is_key_in_dic(self, dic):
        for k in dic.keys():
            if isinstance(dic[k], dict):
                if self.is_key_in_dic(dic[k]):
                    return True
            if k == self.value:
                return True
        return False

    def is_value_in_dic(self, dic):
        for v in dic.values():
            if isinstance(v, dict):
                if self.is_value_in_dic(v):
                    return True
            if self.value == v:
                return True
        return False
