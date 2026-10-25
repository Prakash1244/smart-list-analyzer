from main import *
from database import *
from bson import ObjectId

def prepare_analyse(Numbers: list[int]):
    frequency = frequency_count(Numbers)
    duplicate = duplicate_detect(Numbers)

    document = {
        'Numbers': Numbers,
        'frequency': { str(key): value for key, value in frequency.items()},
        'duplicate': duplicate
    }
    return document

async def retrive_all():
    receive = analyses_collection.find({})
    m=[]

    async for i in receive:
        i['_id']= str(i['_id'])
        m.append(i)

    return m

async def update_list(analyse_id: str, Numbers: list[int]):
    update_document=prepare_analyse(Numbers)

    receive = await analyses_collection.update_one(
        {'_id': ObjectId(analyse_id)},
        {'$set': {'numbers': update_document}}
    )
    return receive.matched_count

async def delete_list(analyse_id: str):
    receive = await analyses_collection.delete_one(
        {'_id': ObjectId(analyse_id)}
    )
    return receive.deleted_count