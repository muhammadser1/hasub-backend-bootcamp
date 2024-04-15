from fastapi import HTTPException


def raise_validation_error(status_code: int, detail: str):
    """
    Helper function to raise a validation error HTTPException.
    """
    raise HTTPException(status_code=status_code, detail=detail)
