#TODO align with DB
from fastapi import APIRouter, status

from app.schemas.Billboard import BillboardResponse, BillboardCreate, BillboardUpdate
from app.classes.Billboard import BillboardClass

router = APIRouter(
    prefix="/billboards",  # prefix automatically added for this router instance
    tags=["Billboards"],  # docs organization
)

service=BillboardClass()


#return all Billboards data
@router.get("/", response_model=dict[str, BillboardResponse])
def get_billboards():
    return service.get_all()






#curly braces indicate a variable taken from url
#return one billboard info
@router.get("/{billboard_name}", response_model=BillboardResponse)
def get_billboard(billboard_name: str):

    billboard=service.get_by_name(billboard_name)

    if billboard is None:
        service.NotFoundError()
    
    return billboard










#add a new billboard
@router.post(
    "/",
    response_model=BillboardResponse,
    status_code=status.HTTP_201_CREATED
)
def create_billboard(data: BillboardCreate):
    return service.create(data)
    






#UPdate billboard
@router.patch(
    "/{billboard_name}",
    response_model=BillboardResponse
)
def update_billboard(billboard_name: str, data: BillboardUpdate):

    try:
        billboard=service.update(billboard_name, data)
    except:
        service.ConflictError()
    
    if billboard is None:
        service.NotFoundError()

    return billboard





#Delete billboard
@router.delete(
    "/{billboard_name}",
    status_code=status.HTTP_204_NO_CONTENT #204 used for good request with no content in response
)
def delete_billboard(billboard_name: str):
    if not service.delete(billboard_name):
        service.NotFoundError()