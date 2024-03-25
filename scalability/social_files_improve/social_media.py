from user import User, posts


class SocialMediaPlatform:
    def __init__(self):
        self.users = []

    def register_user(self, username):
        """
        Allow users to register with a unique username.
        Parameters:
        - username (str): The username to register on the social media platform.
        Check if the username is already taken. If not, create a new user with the provided username
         and add it to the list of users.
         Time Complexity: O(n) where n is the number of existing users.
        """
        if not self._is_username_taken(username):
            user = User(username)
            self.users.append(user)

    def _is_username_taken(self, username):
        """
        Check if the username is already taken by an existing user.

        Parameters:
        - username (str): The username to check.

        Returns:
        - bool: True if the username is already taken, False otherwise.
        Check if the username is already in the users list. If yes, return True; if not, return False.
        Time Complexity: O(n) where n is the number of existing users.
        """
        for user in self.users:
            if user.username == username:
                return True
        return False

    def get_user_by_username(self, username):
        """
        return a user object based on username.
        - username (str): the username to retrieve
        :return:
        - user object or None: The user object corresponding to the username if found, None otherwise.
        Time Complexity: O(n) where n is the number of existing users.
        """
        for user in self.users:
            if user.username == username:
                return user
        return None

    def generate_timeline(self, username):
        """
        Provide a user with a timeline of posts from users they follow.
        username (str):  The username of the user whose timeline is to be generated.
        :return:
        list: A list of posts in the timeline.
        Time Complexity: O(|N|*|M|). where N is number of user. following and M is the number of posts.
        """
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            for post in posts:
                if post['username'] == followed_user:
                    timeline.append(post)
        return timeline
