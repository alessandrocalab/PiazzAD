from fastapi import APIRouter

from app.schemas.Billboard import BillboardResponse

router = APIRouter(
    prefix="/billboards",  # prefix automatically added for this router instance
    tags=["Billboards"],  # docs organization
)


@router.get("/", response_model=list[BillboardResponse])
def get_billboards():
    return [
        {
            "name": "granVisione",
            "status": "active",
            "address": {"street": "via roma 23", "CAP": "80120", "city": "Napoli"},
        },
        {
            "name": "Napoli Est",
            "status": "active",
            "address": {
                "street": "Corso San Giovanni a Teduccio 734",
                "CAP": "80146",
                "city": "Napoli",
            },
        },
    ]
