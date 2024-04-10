from fastapi import Depends, HTTPException, APIRouter

from utils.auth_utils.jwt_manager import check_token

router = APIRouter()

# Define a wrapper function for role-based authorization
def role_authorization(required_role: str):
    def _role_authorization(username: str, token: str):
        role=check_token(token=token,username=username)
        if required_role == role:
            return True
        else:
            raise HTTPException(status_code=403, detail=f"Forbidden, {required_role} role required")
    return _role_authorization

# Dependency function for admin role
check_admin_token = role_authorization("admin")

# Dependency function for guest role
check_guest_token = role_authorization("guest")

# Dependency function for all roles
check_all_token = role_authorization("all")

# Example route accessible only to admin
@router.delete("/aaa/delete_all_students_admin", tags=["aaa"])
async def delete_all_students(authorized: bool = Depends(check_admin_token)):
    # Route handler logic for admin
    print("delete_all_students_admin")
    pass
