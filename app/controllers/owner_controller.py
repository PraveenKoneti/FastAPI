from app.config.db import owner_collection
from app.models.owner_model import OwnerCreate, OwnerUpdate
from fastapi import HTTPException
from bson import ObjectId

#------------------------------------------------------------------------------------------------------------------

# FETCH ALL OWNERS
async def get_all_owners():
    owners = await owner_collection.find().to_list(length=None)
    for owner in owners:
        owner["id"] = str(owner["_id"])
        del owner["_id"]
    return owners

#------------------------------------------------------------------------------------------------------------------

# CREATE THE OWNER
async def create_owner(owner_data : OwnerCreate):
    owner_dict = owner_data.dict()
    result = await owner_collection.insert_one(owner_dict)
    print("owner result = ",result)
    owner_dict["id"] = str(result.inserted_id)
    del owner_dict["_id"]
    return {"message": "Owner details saved", "ownerDetails":owner_dict }

#----------------------------------------------------------------------------------------------------------------

# UPDATE THE OWNER
async def update_owner(owner_id : str, owner_data : OwnerUpdate):
    existed_owner_details = await owner_collection.find_one( {"_id" : ObjectId(owner_id)} )
    if not existed_owner_details:
        raise HTTPException(status_code=404, detail="Owner not found")
    owner_dict = owner_data.dict()
    result = await owner_collection.update_one(
        {"_id":ObjectId(owner_id)},
        {"$set" : owner_dict}
    )
    if result.modified_count == 1:
        updated_owner_details = await owner_collection.find_one({"_id" : ObjectId(owner_id)})
        updated_owner_details["id"] = owner_id
        del updated_owner_details["_id"]
        return {"message":"Owner Details updated", "owner_details":updated_owner_details}
    else:
       raise HTTPException(status_code=400, detail="Owner update failed") 
    
#-----------------------------------------------------------------------------------------------------------------

# DELETE THE OWNER
async def delete_owner(owner_id:str):
    owner_details = await owner_collection.find_one( {"_id" : ObjectId(owner_id)} )
    if not owner_details:
        raise HTTPException(status_code=404, detail="Owner not found")
    result = await owner_collection.delete_one( {"_id" : ObjectId(owner_id)} )
    if result.deleted_count == 1:
        return {"message" : "Owner details deleted"}
    else:
        raise HTTPException(status_code=400, detail="Owner delete failed")
    
#-----------------------------------------------------------------------------------------------------------------