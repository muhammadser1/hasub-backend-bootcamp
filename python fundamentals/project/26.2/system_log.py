import datetime


def single_factory_function():
    timestamp = datetime.datetime.now()

    def msg_only(msg):
        return msg

    def msg_with_timestamp(msg):
        result = "msg:  " + msg + "  date: " + str(timestamp)
        return result

    def msg_with_timestamp_and_level(msg, level):
        result = "msg:  " +msg + "  date: "  +str(timestamp) + " level is  " + str(level)
        return result

    def event_with_timestamp(event):
        result = "date:   " + str(timestamp)+  "event:  " + str(event)
        return result

    return msg_only, msg_with_timestamp, msg_with_timestamp_and_level, event_with_timestamp


def log_processing():
    def filter_function(logs,max_len):
        list1 = []
        list2=[]
        for i in range(len(logs)):
            if "timestamp" not in logs[i] and "date" not in logs[i]:
                list1.append(logs[i])
            if len(logs[i]) <= max_len:
                list2.append(logs[i])
        return list1,list2
    return filter_function


msg_only, msg_with_timestamp, msg_with_timestamp_and_level, event_with_timestamp = single_factory_function()
returns_value = [msg_only("message"), msg_with_timestamp("message with timestamp"),
                 msg_with_timestamp_and_level("message with timestamp and level", "warn"),
                 event_with_timestamp("Event")]
for i in range(len(returns_value)):
    print(returns_value[i])
print("##############")
filter_function = log_processing()
list1,list2=filter_function(returns_value,20)
print("filter out no date/timestamp logs")
for i in list1:
    print(i)

print("\n\nonly logs with short msg")
for i in list2:
    print(i)