# ADD CLASS:
# 1. load db
# 2. check if id in db
# 3. if yes return ?
# 4. if no add
# 5. save to db

def check_class_exist(db_dict, class_id):
    if class_id in db_dict:
        return False
    return True


def tests_add():
    result = check_class_exist({}, 123)
    assert type(result) == type(True)
    assert check_class_exist({123: 1}, 123) == False
    assert check_class_exist({123: 1}, 456) == True
