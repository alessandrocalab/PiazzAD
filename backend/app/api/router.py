from fastapi import APIRouter
#import as module, we may access the element with . (>.<)
#more readable than as 
from app.api.routes import Billboards 

api_router=APIRouter(prefix="/api/v1")

api_router.include_router(Billboards.router)