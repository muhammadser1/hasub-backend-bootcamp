org_chart_large = {
    "name": "CEO",
    "subordinates": [
        {
            "name": "CTO",
            "subordinates": 555
        },
        {
            "name": "CFO",
            "subordinates2": {"subordinates":5}
        }
    ]
}
######################################################
# for item in org_chart_large:
#     print(item)
# name
# subordinates
######################################################
# for item in org_chart_large["subordinates"]:
#     print(item)
#{'name': 'CTO', 'subordinates': 555} this is item
#{'name': 'CFO', 'subordinates': 0} this is item
######################################################
