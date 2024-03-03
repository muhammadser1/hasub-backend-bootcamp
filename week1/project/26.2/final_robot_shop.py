### where is the ui option to break robot? in the main menu you say its possible, but then inside the sub menu there is only sell and repair
### if 


import random
import time
day_time = 30
class Robot():
    def __init__(self, name, id, battery_type):
        self.name = name
        self.id = id
        self.battery_type = battery_type

    def __str__(self):
        return f"id: {self.id},    name: {self.name},    battery_type:  {self.battery_type}"
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
class for_Sale_Robot(Robot,Robot_Pet):
    def __init__(self, name, id, battery_type, main_material, price, animal_type):
        Robot.__init__(self, name, id, battery_type)
        Robot_Pet.__init__(self, main_material, animal_type)
        self.price = price
### dry - why not put the status of the robot in the main robot class?
class Sold_Robot(Robot,Robot_Pet):
    def __init__(self, name, id, battery_type, main_material, price, animal_type):
        Robot.__init__(self, name, id, battery_type)
        Robot_Pet.__init__(self, main_material, animal_type)
        self.price = price
class Broken_Robot(Robot, Robot_Pet):
    def __init__(self, name, id, battery_type, main_material, animal_type,cost_to_fix_per_day):
        Robot.__init__(self, name, id, battery_type)
        Robot_Pet.__init__(self, main_material, animal_type)
        self.cost_to_fix_per_day=cost_to_fix_per_day
class In_RePair_Robot(Robot, Robot_Pet):
    def __init__(self, name, id, battery_type, main_material, animal_type, cost_to_fix_per_day):
        Robot.__init__(self, name, id, battery_type)
        Robot_Pet.__init__(self, main_material, animal_type)
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.numOfDays = 0
        self.start_time = time.time()
class Shop():
    def __init__(self):
        self.balance = 100
        self.list_employee = []
        self.for_sale_robots = []
        self.in_repair_robots = []
        self.broken_robots = []
        self.sold_robot=[]
    def show_employees(self):
        print("This is a list of employees:")
        for employee in self.list_employee:
            print(employee,end=" ")
            print("    daily_salary:  "+ str(employee.daily_salary))
    def show_sales_robots(self):
        print("\nThis is a list of sales robots.")
        i=0
        for sale in self.for_sale_robots:
            print("sequence number:"+str(i),end=' ')
            i+=1
            print(sale,end=" ")
            print("    price:  "+ str(sale.price))
    def show_broken_robots(self):
        print("\nThis is a list of broken robots.")
        i = 0
        for broken in self.broken_robots:
            print("sequence number:"+str(i),end=' ')
            i+=1
            print(broken,end=" ")
            print("    cost_to_fix_per_day:  "+ str(broken.cost_to_fix_per_day))
    def show_in_pair_robots(self):
        print("\nThis is a list of in_repair robots.")
        for rep in self.in_repair_robots:
            print(rep,end=" ")
            print("    cost_to_fix_per_day:  "+ str(rep.cost_to_fix_per_day))
    def show_sold_robots(self):
        print("\nThis is a list of sold robots.")
        for sale in self.sold_robot:
            print(sale,end=" ")
            print("    price:  "+ str(sale.price))
    def init_robots(self,list):
        for i in range(3):
            random_number=random.randint(0,1)
            employee = Employee("employee_"+str(i), i, list[2][random_number], random.randint(1,5))
            sale = for_Sale_Robot("robot_"+str(i), i, list[2][random_number], list[0][random_number], random.randint(100, 500),list[1][random_number])
            self.list_employee.append(employee)
            self.for_sale_robots.append(sale)
            if(i!=2):
                broke = Broken_Robot("broken_"+str(i), i, list[2][random_number], list[0][random_number],list[1][random_number], random.randint(1, 10))
                self.broken_robots.append(broke)
            if (i==0):
                repair = In_RePair_Robot("repair_"+str(i), i, list[2][random_number], list[0][random_number],list[1][random_number], random.randint(1, 10))
                self.in_repair_robots.append(repair)
    def calculate_balance(self):
        ### better to keep it in the state, and updated it when the operation happens, and not after the fact
        current_time = time.time()
        for employee in self.list_employee:
            delta_time = int(current_time - employee.start_time)
            delta_time = delta_time / day_time
            self.balance -= int(employee.daily_salary) * delta_time
        for in_repair_robot in self.in_repair_robots:
            delta_time = int(current_time - in_repair_robot.start_time)
            delta_time = delta_time / day_time
            self.balance -= int(in_repair_robot.cost_to_fix_per_day) * delta_time
    def sell(self,robot):
        self.balance+= int(robot.price)
        print("robot "+robot.name+" has been sold. You Gained ",robot.price,"$.")
        print("The updated balance is:", self.balance)
        self.for_sale_robots.remove(robot)
        self.sold_robot.append(robot)
    def repair(self,robot):
        print("the robot  "+robot.name+" is in being repaired . It will cost you "+ str(robot.cost_to_fix_per_day)+ " per day")
        self.broken_robots.remove(robot)
        name, id, battery_type, main_material, animal_type, cost_to_fix_per_day=robot.name,robot.id,robot.battery_type,robot.main_material,robot.animal_type,robot.cost_to_fix_per_day
        self.in_repair_robots.append(In_RePair_Robot(name,id,battery_type,main_material,animal_type,cost_to_fix_per_day))
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
def Logs():
    print("\nPrint robot details:")
    print("1. Show all robots available for sale")
    print("2. Show all broken robots")
    print("3. Show all robots in repair")
    print("4. Show all sold robots")
    print("\nShop Business:")
    print("5. Show all employees")
    print("6. Show balance of the pet shop")
    print("7. Perform operations (sell, break, repair)")
    print("\nClose the pet shop")
    print("8. End program")

def operations(pet_shop):
    operating_flag=1
    while operating_flag!=4:
        print("1. sell robot?")
        print("2. repair robot?")
        print("3. back")
        operating_flag=check_input(1,3)
        if operating_flag == 3:
            return
        if operating_flag==1:
            if len(pet_shop.for_sale_robots) > 0:
                pet_shop.show_sales_robots()
                print("Which robot do you want to sell? (Type the sequence number of the robot)")
                get_sell_input = check_input(0, (len(pet_shop.for_sale_robots) - 1))
                pet_shop.sell(pet_shop.for_sale_robots[get_sell_input])
            else:
                print("there is no robot for sale\n")
        if operating_flag==2:
            if len(pet_shop.broken_robots) > 0:
                pet_shop.show_broken_robots()
                print("Which robot do you want to repair? (Type the sequence number of the robot)")
                get_repair_input = check_input(0, (len(pet_shop.broken_robots) - 1))
                pet_shop.repair(pet_shop.broken_robots[get_repair_input])
            else:
                print("there is no robot for sale\n")
if __name__ == "__main__":
    pet_shop = Shop()
    list=[["iron","Steel"],["herbivore","carnivore"],["lithium","alkaline"]]
    pet_shop.init_robots(list)
    input_flag=1
    while input_flag!=8:
        Logs()
        print("\nType the number of the operation you want to perform:")
        input_flag=check_input(1,8)
        if input_flag == 1:
            pet_shop.show_sales_robots()
        if input_flag == 2:
            pet_shop.show_broken_robots()
        if input_flag == 3:
            pet_shop.show_in_pair_robots()
        if input_flag == 4:
            pet_shop.show_sold_robots()
        if input_flag == 5:
            pet_shop.show_employees()
        if input_flag == 6:
            pet_shop.calculate_balance()
            print("This is the balance of the pet shop:", pet_shop.balance)
        if input_flag== 7:
            operations(pet_shop)

        time.sleep(1)
