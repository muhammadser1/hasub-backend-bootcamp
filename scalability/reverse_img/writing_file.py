def write_messages_to_file(messages, filename="messages_info.txt"):
    with open(filename, "a") as file:
        file.write(f"\n{messages}")
