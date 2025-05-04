from fastapi import APIRouter
from app.models.user_model import UserCreate, UserUpdate
from app.controllers import user_controller

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


#-------------------------------------------------------------------------------------------------------------

# GET ALL USERS
@router.get("/")
async def get_users():
    return await user_controller.get_all_users()

#-------------------------------------------------------------------------------------------------------------

# CREATE THE USER
@router.post("/")
async def save_user(user: UserCreate):
    return await user_controller.save_user(user)

#--------------------------------------------------------------------------------------------------------------

# UPDATE THE USER DETAILS
@router.put("/{user_id}")
async def update_user(user_id: str, user_data: UserUpdate):
    return await user_controller.update_user(user_id, user_data)

#---------------------------------------------------------------------------------------------------------------

# DELETE THE USER DETAILS
@router.delete("/{user_id}")
async def delete_user(user_id: str):
    return await user_controller.delete_user(user_id)