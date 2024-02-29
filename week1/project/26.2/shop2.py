import time

day_time = 30


class Robot():
    def __init__(self, name, id, battery_type):
        self.name = name
        self.id = id
        self.battery_type = battery_type

    def __str__(self):
        return f"id: {self.id},    name: {self.name}"


class Employee(Robot):
    def __init__(self, name, id, battery_type, daily_salary):
        super().__init__(name, id, battery_type)
        self.daily_salary = daily_salary
        self.numOfDays = 0
        self.start_time = time.time()


class Robot_Pet:
    def __init__(self, main_material, animal_type):
        self.main_material = main_material
        self.animal_type = animal_type

    def __str__(self):
        return f"main_material: {self.main_material}, animal_type: {self.animal_type}"


class for_Sale_Robot:
    def __init__(self, name, id, battery_type, main_material, price, animal_type):
        self.robot = Robot(name, id, battery_type)
        self.robot_pet = Robot_Pet(main_material, animal_type)
        self.price = price

#
# class Broken_Robot(Robot, Robot_Pet):
#     def __init__(self, name, id, battery_type, main_material, animal_type):
#         self.__init__(name, id, battery_type)
#         self.__init__(main_material, animal_type)
#
#
# class In_RePair_Robot(Robot, Robot_Pet):
#     def __init__(self, name, id, battery_type, main_material, animal_type, cost_to_fix_per_day):
#         self.__init__(name, id, battery_type)
#         self.__init__(main_material, animal_type)
#         self.cost_to_fix_per_day = cost_to_fix_per_day
#         self.numOfDays = 0
#         self.start_time = time.time()

class Shop():
    def __init__(self):
        self.balance = 100
        self.list_employee = []
        self.for_sale_robots = []
        self.in_pair_robots = []
        self.broken_robots = []

        self.numOfDays = 0
        self.__start_time = time.time()

    def add_employe(self, name, id, battery_type, daily_salary):
        employee = Employee(name, id, battery_type, daily_salary)
        self.list_employee.append(employee)

    def print_employees(self):
        for employee in self.list_employee:
            print(employee)

    def calculate_balance(self):
        for employee in self.list_employee:
            current_time = time.time()
            delta_time = int(current_time - employee.start_time)
            delta_time = delta_time / day_time
            self.balance -= int(employee.daily_salary) * delta_time
        for in_pair_robot in self.in_pair_robots:
            current_time = time.time()
            delta_time = int(current_time - in_pair_robot.start_time)
            delta_time = delta_time / day_time
            self.balance -= int(in_pair_robot.cost_to_fix_per_day) * delta_time

def check_input(range1, range2):  # range1 =< get input number <= range2
    flag = 1
    while flag == 1:
        get_input = input("")
        if get_input.isdigit() == 1:
            get_input = (int)(get_input)
            if get_input >= range1 and get_input <= range2:
                flag = 0
        if flag == 1:
            print("Invalid  input.\n")
    return get_input


def get_employee_details():
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    battery_type = input("Enter battery type: ")
    daily_salary = input("Enter daily salary: ")
    return name, employee_id, battery_type, daily_salary


def operations(pet_shop):
    flag3 = 1
    while flag3 != 4:
        print("\n1. Sell a robot")
        print("2. Are there any broken robots?")
        print("3. Repair a robot")
        print("4. Back")
        flag3= check_input(1, 4)
        if flag3==4:
            return
        if flag3 == 1:
            i=0
            if len(pet_shop.for_sale_robots)>0:
                for j in range(len(pet_shop.for_sale_robots)):
                    print(str(j)+". "+ str(pet_shop.for_sale_robots[j].robot.id), end='  ')
                    print(pet_shop.for_sale_robots[j].robot.name+ str(pet_shop.for_sale_robots[j].price))
                get_sell_input=check_input(0,(len(pet_shop.for_sale_robots)-1))
                print("gegege"+str(get_sell_input))
            else:
                print("there is no robot for sale\n")

def Robot_issues(pet_shop):
    flag2=1
    while flag2 != 3:
        print("\n1. show all robots aviable on sales")
        print("2. Perform operations ( sell, break, repair")
        print("3. back")
        flag2= check_input(1, 3)
        if flag2== 2:
            operations(pet_shop)
        if flag2==3:
            return
        if flag2==1:
            for sale in pet_shop.for_sale_robots:
                print(sale.robot, end='   ')
                print(sale.robot_pet,end='   ')
                print(sale.price)



if __name__ == "__main__":
    print(10/50)
    pet_shop = Shop()
    robot_for_sale = for_Sale_Robot("Robot1", 1, "Lithium", "Steel", 1000, "Carnivore")
    pet_shop.for_sale_robots.append(robot_for_sale)
    # print(robot_for_sale.robot)
    # print(robot_for_sale.robot_pet)
    # print(robot_for_sale.price)
    # print("############################")
    issues = 1
    while issues != 4:
        print("\n1. Employee issues?")
        print("2. Robot issues?")
        print("3. Store balance")
        print("4. end")
        issues = check_input(1, 4)
        if issues == 2:
            Robot_issues(pet_shop)
        if issues == 4:
            print("end")
            break
        if issues == 3:
            pass
            pet_shop.calculate_balance()
            print(pet_shop.balance)
        elif issues == 1:
            employee_flag = 1
            while employee_flag != 3:
                print("1. Add employee?")
                print("2. print all employee salary cost?")
                print("3. back")
                employee_flag = check_input(1, 3)
                if employee_flag == 1:
                    name, employee_id, battery_type, daily_salary = get_employee_details()
                    pet_shop.add_employe(name, employee_id, battery_type, daily_salary)
                if employee_flag == 2:
                    pet_shop.print_employees()
                print("\n")
