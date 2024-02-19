class User:
  def __init__(self, name,gender,age,professional,tv_show,fav_food):
    self.name = name
    self.gender = gender
    self.age = age
    self.professional = professional
    self.tv_show= tv_show
    self.fav_food = fav_food
if __name__ == "__main__":

    users=[]
    numbers_user=2
    i=1
    flag=0
    while((i<=numbers_user)):
        flag=0
        print("User"+str(i)+"\n")
        name=input("whats your name? ")
        print("1. male")
        print("2. female")
        gender = input("whats your gender (Type 1 or 2)")
        if gender.isdigit() == 1:
            gender = (int)(gender)
            if gender >= 1 and gender <= 2:
                age = input("whats your age (20 =< age <= 100)")
                if age.isdigit() == 1:
                    age = (int)(age)
                    if age >= 20 and age <= 100:
                        professional = input("whats your professional")
                        tv_show = input("whats your favorite tv show")
                        print("1. salad")
                        print("2. pizza")
                        food = input("whats your favorite food (Type 1 or 2)")
                        if food.isdigit() == 1:
                            food = (int)(food)
                            if food >= 1 and food <= 2:
                                flag=1
                                if food==1:
                                    food="salad"
                                else:
                                    food="pizza"
                                print("User" + str(i) + "  has been added successfully.\n")
                                i+=1
                                users.append(User(name,str(gender),str(age),professional,tv_show,str(food)))


        if flag==0:
            print("Wrong Input, Try Again")
    i=1
    for user in users:
        print("User" + str(i) +" " + user.name +" " +str(user.gender)+" "+ str(user.age)+" "+ user.professional+" "+ user.tv_show+" "+user.fav_food)
        i+=1