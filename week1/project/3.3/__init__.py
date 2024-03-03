from Class_Compare.math_operations import *
from Class_Compare.list_operations import *
from Class_Compare.dict_operations import *

def math_operation():
    print("###################################################")
    print("Equal:")
    print("3 Equal 3:   ", Math_op(3).equal(3))
    print("3 Equal 1:   ", Math_op(3).equal(1))
    print("\nGreater:")
    print(" 5 Greater_than  3 ", Math_op(5).greater_than(3))
    print(" 5 Greater_than: 10 ", Math_op(5).greater_than(10))
    print("\nSmaller:")
    print(" 5 Smaller than: 3  ", Math_op(5).smaller_than(3))
    print(" 5 Smaller than: 10 ", Math_op(5).smaller_than(10))
def list_operation():
    print("List:")
    list = [1, 2, 3, 4, 5, 6, 'a']
    print("Search 5 in this list: ", list, "   ", List_op(5).is_value_in_nested_list(list))
    print("Search 10 in this list: ", list, "   ", List_op(10).is_value_in_nested_list(list))
    print("###################################################")
    print("\nNested List:")
    nested_list = [1, [1, 2], [1, 2, 3]]
    print("Search 3 in this list: ", nested_list, "   ", List_op(3).is_value_in_nested_list(nested_list))
    print("Search 4 in this list: ", nested_list, "   ", List_op(4).is_value_in_nested_list(nested_list))
    print("Search 1 in this list: ", nested_list, "   ", List_op(1).is_value_in_nested_list(nested_list))
    print("Search [1,2] in this list: ", nested_list, "   ", List_op([1, 2]).is_value_in_nested_list(nested_list))
def dict_operation():
    print("\nDictionary:")
    my_dict = {
        'a': 1,
        'b': {'c': 2, 'd': 3},
        'e': {'f': {'g': 4, 'h': 5}}
    }
    print("Search key=1 in this dict: ", my_dict, "   ", Dict_op(1).is_key_in_dic(my_dict))
    print("Search key='a' in this dict: ", my_dict, "   ", Dict_op('a').is_key_in_dic(my_dict))
    print("Search key='g' in this dict: ", my_dict, "   ", Dict_op('g').is_key_in_dic(my_dict))
    print("\n")
    print("Search value=1 in this dict: ", my_dict, "   ", Dict_op(1).is_value_in_dic(my_dict))
    print("Search value=4 in this dict: ", my_dict, "   ", Dict_op(4).is_value_in_dic(my_dict))
    print("Search value=6 in this dict: ", my_dict, "   ", Dict_op(6).is_value_in_dic(my_dict))
    print("Search value={'g': 4, 'h': 5} in this dict: ", my_dict, "   ", Dict_op({'g': 4, 'h': 5}).is_value_in_dic(my_dict))
if __name__ == "__main__":
    math_operation()
    print("###################################################")
    list_operation()
    print("###################################################")
    dict_operation()
    print("###################################################")
