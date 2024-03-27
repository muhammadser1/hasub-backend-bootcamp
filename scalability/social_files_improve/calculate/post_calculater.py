def post_calculater(social, input_arr=[10, 100, 1000, 10000]):
    user = social.get_user_by_username("muhammad")
    if user is None:
        print("User 'muhammad' not found.")
        return
    for input_size in input_arr:
        for i in range(input_size):
            msg = "msg" + str(i)
            user.post_message(msg)
