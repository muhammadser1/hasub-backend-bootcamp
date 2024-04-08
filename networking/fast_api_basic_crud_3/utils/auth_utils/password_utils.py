import bcrypt


def hash_password(password: str):
    password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashedPassword.decode('utf-8')


def verify_password(stored_pass, user_pass):
    return bcrypt.checkpw(user_pass.encode('utf-8'), stored_pass.encode('utf-8'))
