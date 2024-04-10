from fastapi import HTTPException

from utils.auth_utils.jwt_manager import check_token


def role_authorization(required_role: str):
    def _role_authorization(username: str, token: str):
        role = check_token(token=token, username=username)
        if required_role == role or required_role == "all":
            return True
        else:
            raise HTTPException(status_code=403, detail=f"Forbidden, {required_role} role required")

    return _role_authorization


check_admin_token = role_authorization("admin")
check_guest_token = role_authorization("guest")
check_all_token = role_authorization("all")
