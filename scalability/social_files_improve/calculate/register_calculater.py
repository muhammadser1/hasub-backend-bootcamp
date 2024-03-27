def register_calculater(social, input_arr=None):
    for input_size in input_arr:
        for i in range(input_size):
            username = "user" + str(i)
            social.register_user(username)
