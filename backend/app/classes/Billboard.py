from app.core.exceptions import NotFoundError, ConflictError
from app.schemas.Billboard import BillboardCreate, BillboardUpdate




class BillboardClass:

    def __init__(self):
        #TODO remove
        self._billboards = {
            "granVisione": {
                "name": "granVisione",
                "status": "active",
                "address": {
                    "street": "Via Roma 23",
                    "CAP": "80120",
                    "city": "Napoli"
                }
            }
        }


    #Exception Methods
    def NotFoundError(self):
        NotFoundError("Billboard not found")

    def ConflictError(self):
        ConflictError("Billboard already exists")

    #API methods
    def get_all(self):
        return self._billboards


    

    def get_by_name(self, name: str):
        return self._billboards.get(name)



    

    def create(self, data: BillboardCreate):
        if data.name in self._billboards:
            self.ConflictError()

        billboard = data.model_dump()
        billboard["status"] = "inactive"

        self._billboards[data.name] = billboard
        return billboard



    

    def update(self, name: str, data: BillboardUpdate):
        current = self._billboards.get(name)

        if current is None:
            return None

        changes = data.model_dump(
            exclude_unset=True,
            exclude_none=True,
            mode="json"
        )

        new_name = changes.get("name", name)

        #check if the new name is already used by another billboard
        if new_name != name and new_name in self._billboards:
            raise Exception

        updated = current | changes #it create a new dict
        #in case o duplicated keys the rigth dict will override the first one

        if new_name != name:
            del self._billboards[name]

        self._billboards[new_name] = updated

        return updated




    

    def delete(self, name: str) -> bool:
        if name not in self._billboards:
            return False

        del self._billboards[name]
        return True
