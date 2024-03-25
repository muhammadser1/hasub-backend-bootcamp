import time
from calculate.calculate_average_execution_time import calculate_average_execution_time
from calculate.register_calculater import register_calculater
from calculate.follow_calculater import follow_calculater
from calculate.post_calculater import post_calculater
from calculate.generate_timeline_calculater import generate_timeline_calculater
from social_media import SocialMediaPlatform
from social_media_improved import SocialMediaPlatform_improved


def write_messages_to_file(messages, filename="messages_info.txt", msg_show="\n"):
    with open(filename, "a") as file:
        for message in messages:
            for key, value in message.items():
                file.write(f"{key}: {value}\n")


if __name__ == '__main__':
    num_runs = 3
    input_arr = [10, 100, 1000, 10000]
    msg = []

    social_media = SocialMediaPlatform()
    social_media.register_user("muhammad")

    average_time = calculate_average_execution_time(num_runs, register_calculater, social_media, input_arr=input_arr)
    msg.append({"Average registration time before improvements:": average_time})

    average_time = calculate_average_execution_time(num_runs, follow_calculater, social_media, input_arr=input_arr)
    msg.append({"Average follow_calculater time before improvements:": average_time})

    average_time = calculate_average_execution_time(num_runs, post_calculater, social_media, input_arr=input_arr)
    msg.append({"Average post_calculater time before improvements:": average_time})

    average_time = calculate_average_execution_time(num_runs, generate_timeline_calculater, social_media,
                                                    input_arr=input_arr)
    msg.append({"Average generate_timeline_calculater time before improvements:": average_time})

    #############################################################################################################################
    msg.append({"":"\n"})
    social_media2 = SocialMediaPlatform_improved()
    social_media2.register_user("muhammad")
    average_time = calculate_average_execution_time(num_runs, register_calculater, social_media2, input_arr=input_arr)
    msg.append({"Average registration time after improvements:": average_time})

    average_time = calculate_average_execution_time(num_runs, follow_calculater, social_media2, input_arr=input_arr)
    msg.append({"Average follow_calculater time after improvements:": average_time})

    average_time = calculate_average_execution_time(num_runs, post_calculater, social_media2, input_arr=input_arr)
    msg.append({"Average post_calculater time after improvements:": average_time})

    average_time = calculate_average_execution_time(num_runs, generate_timeline_calculater, social_media2,
                                                    input_arr=input_arr)
    msg.append({"Average generate_timeline_calculater time after improvements:": average_time})

    write_messages_to_file(msg, "message_data_timestamp")
