#TODO align with DB
from fastapi import APIRouter, HTTPException

from app.schemas.Billboard import BillboardResponse

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
@router.get("/", response_model=list[BillboardResponse])
def get_billboards():
    return bill


#curly braces indicate a variable taken from url
@router.get("/{billboard_name}", response_model=BillboardResponse)
def get_billboard(billboard_name: str):

    billboard=bill.get(billboard_name)

    if billboard is None:

        raise HTTPException(
            status_code=404,
            detail="Billboard not found"
        )
    return billboard