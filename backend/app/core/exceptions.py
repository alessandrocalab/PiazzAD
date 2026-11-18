from fastapi import HTTPException

def NotFoundError(message: str):
    raise HTTPException(
                status_code=404,
                detail=message
            )

def ConflictError(message: str):
    raise HTTPException(
                    status_code=409,
                    detail=message
                )