from models.user import User


def validate_user_input(user: User):
    """

    :param user:
    :return:
    """
    if not isinstance(user.username, str):
        raise TypeError("Username must be a string")
    if not isinstance(user.password, str):
        raise TypeError("Password must be a string")
    if not isinstance(user.role, str):
        raise TypeError("Role must be a string")