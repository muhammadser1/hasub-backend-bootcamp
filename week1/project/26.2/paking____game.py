class Small_Item:
    def __init__(self, origin, weight):
        self.origin = origin
        self.weight = weight
class Passport(Small_Item):
    def __init__(self):
        super().__init__("USA", 1)
        self.color = "blue"
        self.price = 50
        self.name = "Passport"
class Sun_Glasses(Small_Item):
    def __init__(self):
        super().__init__("italy", 10)
        self.color = "black"
        self.have_Case = "yes"
        self.name = "Sun_Glasses"
class Sneakers(Small_Item):
    def __init__(self):
        super().__init__("Spain", 14)
        self.brand = "NewBalance"
        self.new = "false"
        self.name = "Sneakers"
#######################################################
class Electronics():
    def __init__(self, brand, weight):
        self.brand = brand
        self.weight = weight
class UniversalCharger(Electronics):
    def __init__(self):
        super().__init__("Lenovo", 12)
        self.size = "Medium"
        self.color = "black"
        self.price = 50
        self.name = "Universal_Charger"
class Compass(Electronics):
    def __init__(self):
        super().__init__("Samsung", 4)
        self.accuracy = "high"
        self.materials = ["iron","plastic"]
        self.price = 50
        self.name = "compass"
class Smartphone(Electronics):
    def __init__(self):
        super().__init__("Apple", 30)
        self.system =  "iOS"
        self.Storage = "128gb"
        self.display = "AMOLED"
        self.camera = "Dual lens"
        self.materials =[ "lithium", "plastic"]
        self.name = "Smartphone"
class Smartwatch(Electronics):
    def __init__(self):
        super().__init__("Samsung", 44)
        self.battery = "3_days"
        self.fitness = "Heart Rate Monitor"
        self.display = "Touchscreen"
        self.connectivity = "Bluetooth"
        self.name = "Smartwatch"
class Laptop(Electronics):
    def __init__(self):
        super().__init__("DELL", 60)
        self.processor = "Intel i7"
        self.ram = "16 GB"
        self.storage = "512 GB SSD"
        self.graphics = "NVIDIA GeForce4"
        self.name = "Laptop"
#######################################################
class Bag:
    def __init__(self):
        self.Small_item=[Passport(),Sun_Glasses(),Sneakers()]
        self.Electronics = [UniversalCharger(), Compass(), Smartphone(), Smartwatch(), Laptop()]
        self.weight=0
        self.count=0
        self.my_item_small_items=[]
        self.my_item_electronics = []
    def add_items(self, is_small_item, index):
        if self.count < 6 and self.weight <= 80:
            if is_small_item == 1:
                list = self.Small_item
            else:
                list = self.Electronics
            if len(list)!=0:
                item = list[index - 1]
                if self.weight + item.weight > 80:
                    result = "Sorry, you can't add this item due to its weight exceeding the limit"
                    print(result)
                    print("Try Again \n")
                    return "Try Again "
                else:
                    result = " added successfully."
                    if is_small_item == 1:
                        self.my_item_small_items.append(item)
                    else:
                        self.my_item_electronics.append(item)
                    self.weight += item.weight
                    list.remove(item)
                    self.count += 1
                    print(item.name+result)
                    return result
            else:
                result = "the list is empty"
        else:
            result = "you cant add more items"
        print(result)
        return result

    def remove_item(self, is_small_item, item):
        if is_small_item == 1:
            list = self.Small_item
            list2=self.my_item_small_items
        else:
            list = self.Electronics
            list2 = self.my_item_electronics

        list.append(item)
        bag.count-=1
        bag.weight-=item.weight
        list2.remove(item)
        result=" removed successfully."
        print(item.name+result)
        return result
def check_input(range1, range2):  # range1 =< get input number <= range2
    flag=1
    while flag==1:
        get_input = input("")
        if get_input.isdigit() == 1:
            get_input = (int)(get_input)
            if get_input >= range1 and get_input <= range2:
                flag=0
        if flag==1:
            print("Invalid  input.\n")
    return get_input
def add_item_choice(bag):
    flag = 1
    while flag:
        print("1. Small_item")
        print("2. Electronics")
        print("3.Back")
        value_input = check_input(1, 3)
        if value_input == 1:
            list=bag.Small_item

        if value_input ==2:
            list = bag.Electronics
        if value_input ==3:
            break
        for i in range(len(list)):
            print(str(i+1)+". "+list[i].name, " the weight is:", list[i].weight, end="      ")
        print("\n")

        if value_input == 1:
            get_item_index = check_input(1, len(bag.Small_item))
            result=bag.add_items(1, get_item_index)
        if value_input == 2:
            get_elect_index = check_input(1, len(bag.Electronics))
            result=bag.add_items(2, get_elect_index)

        if result==" added successfully.":

            flag=0
def remove_item_choice(bag):
    flag = 1
    while flag:
        print("Which kind of item you want to remove in your list?")
        print("1. Small_item")
        print("2. Electronics")
        print("3.Back")
        value_input = check_input(1, 3)
        if value_input == 1:
            list=bag.my_item_small_items
            for i in range(len(list)):
                print(str(i + 1) + ". " + list[i].name, " the weight is:", list[i].weight, end="      ")
            print("\n")
            get_item_index = check_input(1, len(list))
            bag.remove_item(1,list[get_item_index-1])
        if value_input ==2:
            list=bag.my_item_electronics
            for i in range(len(bag.my_item_electronics)):
                print(str(i + 1) + ". " + list[i].name, " the weight is:", list[i].weight, end="      ")
            print("\n")
            get_item_index = check_input(1, len(list))
            bag.remove_item(2,list[get_item_index-1])
        if value_input ==3:
            break
if __name__ == "__main__":
    bag= Bag()
    count = 0
    weight = 0
    while bag.count < 6:
            print("You can pick " + str(6 - bag.count) + " more items.")
            print("You can pick up to " + str(80 - bag.weight) + " more units.\n")
            print("Do you want to add an item?")
            print("1. yes,add item")
            print("2. no,remove item")
            add_remove_input=check_input(1,2)
            if add_remove_input == 1:
                add_item_choice(bag)
            if add_remove_input == 2:
                remove_item_choice(bag)

    print("the game is finished")
    list=bag.my_item_small_items
    list2=bag.my_item_electronics
    print("small_items:")
    for i in list:
        print(i.name)
    print("electronics_items:")
    for i in list2:
        print(i.name)
## The code is lengthy because it incorporates checks for each input to ensure it is an integer and falls within a specified range, thereby safeguarding against potential user input errors.