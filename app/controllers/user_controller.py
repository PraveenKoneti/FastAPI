from app.config.db import user_collection
from app.models.user_model import UserCreate, UserUpdate
from fastapi import HTTPException
from bson import ObjectId


#--------------------------------------------------------------------------------------------------------------------

# FETCH USERS
# Asynchronous function to fetch all users from the collection
async def get_all_users():
    # Use the 'to_list()' method to convert the cursor to a list
    users_cursor = user_collection.find()  # Do NOT await here
    users = await users_cursor.to_list(length=None)  # Await this

    # Convert ObjectId to string
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]  # Remove the _id field

    print("users", users)
    # Encode using alias (to return 'id' instead of '_id')
    return users

#---------------------------------------------------------------------------------------------------------------

# CREATE USERS 
async def save_user(user_data: UserCreate):
    user_dict = user_data.dict()
    result = await user_collection.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    del user_dict["_id"]
    return {"message": "User created", "userDetails": user_dict}

#-------------------------------------------------------------------------------------------------------------------

# UPDATE USERS
async def update_user(user_id:str, user_data: UserUpdate):

    # Fetch user details from the collection
    user_details = await user_collection.find_one({"_id": ObjectId(user_id)})

    # Check if user is found
    if not user_details:
        raise HTTPException(status_code=404, detail="User not found")

    # Convert ObjectId to string in the user details
    user_details['_id'] = str(user_details['_id'])

    # Prepare the data to be updated
    update_fields = user_data.dict()

    # Update the user details in the collection
    result = await user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_fields}
    )

    # Check if any modification occurred
    if result.modified_count == 1:
        updated_user = await user_collection.find_one({"_id": ObjectId(user_id)})
        # Convert ObjectId to string in the updated user details
        updated_user['_id'] = str(updated_user['_id'])
        # Optionally, delete _id from the response
        del updated_user["_id"]
        return {"message": "User updated successfully", "user_details": updated_user}
    else:
        raise HTTPException(status_code=400, detail="User update failed")
    
#-------------------------------------------------------------------------------------------------------------------

async def delete_user(user_id:str):

    user_details = await user_collection.find_one( {"_id" : ObjectId(user_id)} )
    if not user_details:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete the user from the collection
    result = await user_collection.delete_one({"_id": ObjectId(user_id)})

    # Check if the deletion was successful
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=400, detail="User deletion failed")