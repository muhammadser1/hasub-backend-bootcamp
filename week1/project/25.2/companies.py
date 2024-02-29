
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
def get_departments(dic):
    departments = []
    for item in dic["subordinates"]:
        if "subordinates" in item:
            departments.append(item["name"])
            departments.extend(get_departments(item))
    return departments
def count_developers(dic):
    count = 0
    for item in dic["subordinates"]:
        if "subordinates" not in item:
            if "Developer" in item["name"]:
                count += 1
        else:
            count += count_developers(item)
    return count

def count_workers_under_position(dic, position_name):
    for item in dic["subordinates"]:
        if item["name"] == position_name:
            return many_worker(item, 0)
    return 0
def many_worker(dic, c):
    for item in dic["subordinates"]:
        if "subordinates" not in item:
            c += 1
        else:
            c = many_worker(item, c)
    return c
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
flag=1
while flag:
	print("Please choose one company:")
	print("1.org_chart_large")
	print("2.tech_company_org_chart_2")
	print("3.tech_company_org_chart_3")
	print("4.end")
	x=check_input(1,4)
	if x == 4:
		break
	print("Which one do you want to know about this company?")
	print("1. how many workers are there?")
	print("2. how many work under the the CTO?")
	print("3. how many people are there with “developer” in their title?")
	print("4. how many departments are there and what are there names?")
	print("5. back")
	y = check_input(1, 5)
	lst=[0]
	if(y==1):
		print(many_worker(org_chart_large,0))
	if y == 2:
		workers_under_CTO = count_workers_under_position(org_chart_large, "CTO")
		print("Number of workers under the CTO:", workers_under_CTO)
	if y == 3:
		developers_count = count_developers(org_chart_large)
		print("Number of people with 'developer' in their title:", developers_count)
	if y == 4:
		departments = get_departments(org_chart_large)
		num_departments = len(departments)
		print("Number of departments:", num_departments)
		print("Department names:")
		for department in departments:
			print("-", department)
	print("\n\n")
