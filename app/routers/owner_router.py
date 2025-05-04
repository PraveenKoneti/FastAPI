from fastapi import APIRouter
from app.controllers import owner_controller
from app.models.owner_model import OwnerCreate, OwnerUpdate

router = APIRouter( prefix="/owners", tags=["owners"])

#--------------------------------------------------------------------------------------------------------------

# FETCH ALL OWNERS
@router.get("/")
async def get_owners():
    return await owner_controller.get_all_owners()

#------------------------------------------------------------------------------------------------------------------

# CREATE OWNER 
@router.post("/")
async def owner_create(owner_data : OwnerCreate):
    return await owner_controller.create_owner(owner_data)

#----------------------------------------------------------------------------------------------------------------

# UPDATE OWNER
@router.put("/{owner_id}")
async def owner_update(owner_id:str, owner_data:OwnerUpdate):
    return await owner_controller.update_owner(owner_id, owner_data)

#------------------------------------------------------------------------------------------------------------------

# DELETE OWNER
@router.delete("/{owner_id}")
async def owner_delete(owner_id:str):
    return await owner_controller.delete_owner(owner_id)