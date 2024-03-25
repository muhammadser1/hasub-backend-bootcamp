from user_improved import User_improved


class SocialMediaPlatform_improved:
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        """
        Allow users to register with a unique username.
        Parameters:
        - username (str): The username to register on the social media platform.
        Check if the username is already taken. If not, create a new user with the provided username
         and add it to the list of users.
         Time Complexity: O(1) amortized. o(n) w.c
        """
        if username not in self.users:
            self.users[username]=User_improved(username)
        else:
            pass

    def _is_username_taken(self, username):
        """
        Check if the username is already taken by an existing user.

        Parameters:
        - username (str): The username to check.

        Returns:
        - bool: True if the username is already taken, False otherwise.
        Check if the username is already in the users list. If yes, return True; if not, return False.
        Time Complexity: O(1) amortized. o(n) w.c
        """
        return username in self.users

    def get_user_by_username(self, username):
        """
        return a user object based on username.
        - username (str): the username to retrieve
        :return:
        - user object or None: The user object corresponding to the username if found, None otherwise.
        Time Complexity: O(1) amortized. o(n) w.c
        """
        return self.users.get(username)

    def generate_timeline(self, username):
        """
        Provide a user with a timeline of posts from users they follow. username (str):  The username of the user
        whose timeline is to be generated. :return: list: A list of posts in the timeline. Time Complexity: O(n * m),
        where n is the number of followers of the given username, and m is the  number of posts by all followers.
        """
        user = self.users.get(username)
        if not user:
            return []

        timeline = []
        for followed_username in user.following:
            followed_user = self.users.get(followed_username)
            if followed_user:
                timeline.extend(followed_user.posts)

        return timeline
