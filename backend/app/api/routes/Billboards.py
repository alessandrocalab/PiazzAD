#TODO align with DB
from fastapi import APIRouter, HTTPException, status

from app.schemas.Billboard import BillboardResponse, BillboardCreate, BillboardUpdate
from app.enums.BillboardStatus import BillboardStatus

router = APIRouter(
    prefix="/billboards",  # prefix automatically added for this router instance
    tags=["Billboards"],  # docs organization
)

bill = { #TODO test dict
    "granVisione": {
        "name": "granVisione",
        "status": "active",
        "address": {
            "street": "Via Roma 23",
            "CAP": "80120",
            "city": "Napoli"
        }
    },

    "Napoli Est": {
        "name": "Napoli Est",
        "status": "active",
        "address": {
            "street": "Corso San Giovanni a Teduccio 734",
            "CAP": "80146",
            "city": "Napoli"
        }
    }
}

#return all Billboards data
@router.get("/", response_model=dict[str, BillboardResponse])
def get_billboards():
    return bill










#curly braces indicate a variable taken from url
#return one billboard info
@router.get("/{billboard_name}", response_model=BillboardResponse)
def get_billboard(billboard_name: str):

    billboard=bill.get(billboard_name)

    if billboard is None:

        raise HTTPException(
            status_code=404,
            detail="Billboard not found"
        )
    return billboard










#add a new billboard
@router.post(
    "/",
    response_model=BillboardResponse,
    status_code=status.HTTP_201_CREATED
)
def create_billboard(data: BillboardCreate):

    #check if the name already exists
    if data.name in bill:
        raise HTTPException(
        status_code=409,
        detail="Billboard already exists"
    )

    #converting into dict
    billboard=data.model_dump()
    billboard["status"]= BillboardStatus.INACTIVE

    #adding the new billboard to the dict
    bill[data.name]=billboard

    return billboard











#UPdate billboard
@router.patch(
    "/{billboard_name}",
    response_model=BillboardResponse
)
def update_billboard(billboard_name: str, data: BillboardUpdate):

    #find the billboard
    billboard=bill.get(billboard_name)

    if billboard is None:
        raise HTTPException(
            status_code=404,
            detail="Billboard not found"
        )

    changes = data.model_dump(
        exclude_unset=True,
        exclude_none=True, 
        mode="json" 
    )

    new_name=changes.get("name", billboard_name)

    #check if the new name is already used
    if new_name != billboard_name and new_name in bill:
        raise HTTPException(
            status_code=409,
            detail="Billboard name already exists"
        )

    update_billboard=billboard.copy()
    update_billboard.update(changes)

    #updating the dict if the name changed
    if new_name != billboard_name:
        del bill[billboard_name]

    bill[new_name]=update_billboard

    return update_billboard





#Delete billboard
@router.delete(
    "/{billboard_name}",
    status_code=status.HTTP_204_NO_CONTENT #204 used for good request with no content in response
)
def delete_billboard(billboard_name: str):

    if billboard_name not in bill:
        raise HTTPException(
            status_code=404,
            detail="Billboard not found"
        )

    del bill[billboard_name]