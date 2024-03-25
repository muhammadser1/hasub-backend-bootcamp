class User:
    def __init__(self, username):
        self.username = username
        self.following = []

    def follow(self, other_user):
        """
        Allow users to follow other users.
        Parameters:
        - other_user (str): The username of the user to follow.
        Adds the username of the other user to the list of users followed by this user.
        Time Complexity: O(n) Due to other_user not in self.following:
        """
        if other_user not in self.following:
            self.following.append(other_user)

    def post_message(self, message):
        """
        Allow registered users to post messages.

        Parameters:
        - message (str): The message to be posted.

        Creates a post containing the user's username and the provided message,
        then adds it to the global list of posts.
        Time Complexity: O(1)
        """
        post = {'username': self.username, 'message': message}
        posts.append(post)


# Assume posts are stored in a global list
posts = []