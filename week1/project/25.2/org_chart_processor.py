org_chart_large = {
    "name": "CEO",
    "subordinates": [
        {
            "name": "CTO",
            "subordinates": [
                {
                    "name": "Development",
                    "subordinates": [
                        {"name": "Engineering Manager"},
                        {
                            "name": "Software Engineers",
                            "subordinates": [
                                {"name": "Senior Developer"},
                                {"name": "Developer"},
                                {"name": "Junior Developer"}
                            ]
                        }
                    ]
                },
                {
                    "name": "QA",
                    "subordinates": [
                        {"name": "QA Manager"},
                        {"name": "QA Engineers"}
                    ]
                }
            ]
        },
        {
            "name": "CFO",
            "subordinates": [
                {"name": "Finance Manager"},
                {
                    "name": "Accounting",
                    "subordinates": [
                        {"name": "Senior Accountant"},
                        {"name": "Junior Accountant"}
                    ]
                }
            ]
        },
        {
            "name": "COO",
            "subordinates": [
                {
                    "name": "Operations",
                    "subordinates": [
                        {"name": "Operations Manager"},
                        {"name": "Logistics Team"}
                    ]
                },
                {
                    "name": "HR",
                    "subordinates": [
                        {"name": "HR Manager"},
                        {"name": "Recruitment Team"}
                    ]
                }
            ]
        }
    ]
}
def many_worker_under_CTO(dic,counter=0):
    for item in dic["subordinates"]:
        if item["name"]=="CTO":
            return many_worker(item,0)
def get_departments(dic, departments):
    for item in dic["subordinates"]:
        if "subordinates" in item:
            departments.append(item["name"])
            get_departments(item, departments)
        else:
            pass
    return departments

def many_worker(dic,counter=0):
    for item in dic["subordinates"]:
        if "subordinates" in item:
            counter = many_worker(item, counter)
        else:
            counter+=1
    return counter
def many_worker_with_developer(dic,counter=0):
    for item in dic["subordinates"]:
        if "subordinates" in item:
            counter = many_worker_with_developer(item, counter)
        else:
            if "Developer" in item["name"]:
                counter+=1
    return counter
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
list=["org_chart_large","tech_company_org_chart_2","tech_company_org_chart_3"]
flag = 1
while flag:
    print("Please choose one company:")
    print("1.org_chart_large")
    print("2.tech_company_org_chart_2")
    print("3.tech_company_org_chart_3")
    print("4.end")
    x = check_input(1, 4)
    if x == 4:
        break
    print("Which one do you want to know about this company?")
    print("1. how many workers are there?")
    print("2. how many work under the the CTO?")
    print("3. how many people are there with “developer” in their title?")
    print("4. how many departments are there and what are there names?")
    print("5. back")
    y = check_input(1, 5)
    if (y == 1):
        print("in " + list[x - 1] + f" there are {many_worker(org_chart_large, 0)} workers")
    if (y == 2):
        print("in " + list[x - 1] + f" there are {many_worker_under_CTO(org_chart_large, 0)} workers under the CTO")
    if (y == 3):
        print("in " + list[x - 1] + f" there are {many_worker_with_developer(org_chart_large, 0)} workers with developer")
    if (y == 4):
        print(get_departments(org_chart_large,[]))
    print("\n\n")
