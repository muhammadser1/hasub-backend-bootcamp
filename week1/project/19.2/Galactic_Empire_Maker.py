import random


class Delegation:
    def __init__(self, name, number, needed_materials):
        self.needed_materials = needed_materials
        self.name = name
        self.number = number

def negotiation(delegations):
    agree=0
    for i in range(len(delegations)):
        flag=1
        for suggestion_try in range(delegations[i].number):
            suggestion_num=random.randint(1,19)
            suggestion_material=materials[suggestion_num]
            if suggestion_material in delegations[i].needed_materials:
                print(delegations[i].name +"  "+ "agree to cooperate with you.")
                agree+=1
                flag=0
                break
        if flag==1:
            print(delegations[i].name + "  " + "fail to cooperate with you.")
    return agree

if __name__ == "__main__":
    materials = []  # I will use a list because it's easy to randomly select materials and store them as wanted materials in delegations. (i need the index)
    number_allien = 10
    delegations = []
    needed_materials = set()
    for i in range(20):  # 0-19
        materials.append("Material_" + str(i))
    print(materials)
    for i in range(number_allien):  # 0-9
        needed_materials = set()
        for j in range(random.randint(1, 3)):
            random_num = random.randint(0, 19)
            needed_materials.add(materials[random_num])
        delegations.append(Delegation(("delegate ") + str(i), random.randint(1, 10), needed_materials))

    for delegation in delegations:
        print(delegation.name, delegation.needed_materials, delegation.number)
    agree=negotiation(delegations)
    if (agree/ len(delegations))*100 >= 70:
        print("you are successful")
    else:
        print("Failed")
