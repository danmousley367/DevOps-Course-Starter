import pymongo
import os
from todo_app.data.Status import Status
from bson import ObjectId

def get_items_list():
    db_connection_string = os.getenv('COSMOS_DB_CONNECTION_STRING')
    client = pymongo.MongoClient(db_connection_string, tlsCaFile="DigiCertGlobalRootG2.crt.pem")
    db = client.todo_app_db
    return db.todo_list

def add_db_item(title):
    """
    Adds a new item with the specified title to the database.

    Args:
        title: The title of the item.

    Returns:
        item: The new item.
    """
    items_list = get_items_list()
    
    try:
        response = items_list.insert_one({
            "name": title,
            "status": Status.TODO.value
        })
        print(response)

    except Exception as e:
        print(f"Attempt to create item with title {title} failed. Error: {e}")

def get_db_item(id):
    """
    Gets the item from the database.

    Args:
        itemId: The ID of the item.

    Returns:
        item: The requested item.
    """
    items_list = get_items_list()
    
    try:
        response = items_list.find_one({"_id": ObjectId(id)})

        return response
    except Exception as e:
        print(f"Attempt to get item failed. Error: {e}")

def get_db_items():
    """
    Fetches all saved items from the database.

    Returns:
        list: The list of saved items.
    """
    items_list = get_items_list()

    try:
        response = items_list.find()
        items = list(response)

        return items
    except Exception as e:
        print(f"Attempt to get items from database failed. Error: {e}")

def update_status(item_id, status):
    """
    Updates the status an item to the specified status in the database.

    Returns:
        card: The card that was moved to a new list.
    """
    items_list = get_items_list()
    
    try:
        response = items_list.update_one({"_id": ObjectId(item_id)}, {'$set': {"status": status}})
        print("update response", response)
    except Exception as e:
        print(f"Attempt to mark item incomplete failed. Error: {e}")

def delete_db_item(item_id):
    """
    Deletes an item in the database.

    Returns:
        None.
    """
    items_list = get_items_list()
    
    try:
        response = items_list.delete_one({"_id": ObjectId(item_id)})
        print("delete response", response)
    except Exception as e:
        print(f"Attempt to delete item failed. Error: {e}")