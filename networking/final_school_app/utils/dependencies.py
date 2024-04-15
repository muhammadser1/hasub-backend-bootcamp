from fastapi import HTTPException

from utils.userAuth_utils.jwt_token_manager import check_token


def role_authorization(required_role: str):
    def _role_authorization(username: str, token: str):
        role = check_token(token=token, username=username)
        if required_role == role or required_role == "all":
            return True
        else:
            raise HTTPException(status_code=403, detail=f"Forbidden, {required_role} role required")

    return _role_authorization
