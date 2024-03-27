import time
from calculate.calculate_average_execution_time import calculate_average_execution_time
from calculate.register_calculater import register_calculater
from calculate.follow_calculater import follow_calculater
from calculate.post_calculater import post_calculater
from calculate.generate_timeline_calculater import generate_timeline_calculater
from social_media import SocialMediaPlatform
from social_media_improved import SocialMediaPlatform_improved


def write_messages_to_file(messages, filename="messages_info.txt"):
    with open(filename, "a") as file:
        i=0
        for message in messages:
            for key, value in message.items():
                file.write(f"{key}: {value}\n")
            i+=1
        if i %2 ==0:
            file.write("\n\n")

if __name__ == '__main__':
    num_runs = 3
    input_arr = [10, 1000, 10000,20000,50000]
    msg = []

    social_media = SocialMediaPlatform()
    social_media.register_user("muhammad")
    social_media2 = SocialMediaPlatform_improved()
    social_media2.register_user("muhammad")

    average_time = calculate_average_execution_time(num_runs, register_calculater, social_media, input_arr=input_arr)
    msg.append({"Average registration time before improvements over 3 iterations for inputs "
                "[10, 1000, 10000, 20000, 50000] is:": average_time})
    average_time = calculate_average_execution_time(num_runs, register_calculater, social_media2, input_arr=input_arr)
    msg.append({"Average registration time after improvements over 3 iterations for inputs "
                "[10, 1000, 10000, 20000, 50000] is:": average_time})
    ###################################################################################################################
    ###################################################################################################################
    average_time = calculate_average_execution_time(num_runs, post_calculater, social_media, input_arr=input_arr)
    msg.append({"Average post_calculater time before improvements:": average_time})
    average_time = calculate_average_execution_time(num_runs, post_calculater, social_media2, input_arr=input_arr)
    msg.append({"Average post_calculater time after improvements:": average_time})
    ###################################################################################################################
    ##################################################################################################################
    average_time = calculate_average_execution_time(num_runs, follow_calculater, social_media, input_arr=input_arr)
    msg.append({"Average follow_username time before improvements over 3 iterations for inputs "
                "[10, 1000, 10000, 20000, 50000] is:": average_time})
    average_time = calculate_average_execution_time(num_runs, follow_calculater, social_media2, input_arr=input_arr)
    msg.append({"Average follow_username time after improvements over 3 iterations for inputs "
                "[10, 1000, 10000, 20000, 50000] is:": average_time})



    social_media3 = SocialMediaPlatform()
    social_media3.register_user("muhammad")
    social_media4= SocialMediaPlatform_improved()
    social_media4.register_user("muhammad")
    input_arr = [10, 1000, 5000]
    average_time = calculate_average_execution_time(1, register_calculater, social_media3, input_arr=input_arr)
    average_time = calculate_average_execution_time(1, post_calculater, social_media3, input_arr=input_arr)
    average_time = calculate_average_execution_time(1, follow_calculater, social_media3, input_arr=input_arr)
    average_time = calculate_average_execution_time(1, register_calculater, social_media4, input_arr=input_arr)
    average_time = calculate_average_execution_time(1, post_calculater, social_media4, input_arr=input_arr)
    average_time = calculate_average_execution_time(1, follow_calculater, social_media4, input_arr=input_arr)

    average_time = calculate_average_execution_time(1, generate_timeline_calculater, social_media3,
                                                    input_arr=input_arr)
    print("hi man")
    msg.append({"Average generate_timeline time before improvements with inputs "
                "[10, 1000, 5000] is:": average_time})

    average_time = calculate_average_execution_time(1, generate_timeline_calculater, social_media4,
                                                    input_arr=input_arr)
    print("hi man2")

    msg.append({"Average generate_timeline time after improvements with inputs "
                "[10, 1000, 5000] is:": average_time})

    write_messages_to_file(msg)