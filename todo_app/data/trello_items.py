import requests
import os
import json

BASE_URL = "https://api.trello.com/1"
DEFAULT_HEADERS = {
  "Accept": "application/json"
}

def add_board_item(title):
    """
    Adds a new item with the specified title to the trello board.

    Args:
        title: The title of the item.

    Returns:
        item: The new item.
    """
    query = {
        'idList': os.getenv('TRELLO_TODO_LIST_ID'),
        'key': os.getenv('TRELLO_API_KEY'),
        'token': os.getenv('TRELLO_API_TOKEN'),
        'name': title
    }
    
    try:
        requests.request(
            "POST",
            f"{BASE_URL}/cards",
            headers=DEFAULT_HEADERS,
            params=query
        )

    except:
        print(f"Attempt to create item with title {title} failed")

def get_board_item(id):
    """
    Gets the item from the trello board.

    Args:
        itemId: The ID of the item.

    Returns:
        item: The requested item.
    """
    query = {
        'key': os.getenv('TRELLO_API_KEY'),
        'token': os.getenv('TRELLO_API_TOKEN'),
    }
    
    try:
        response = requests.request(
            "GET",
            f"{BASE_URL}/cards/{id}",
            headers=DEFAULT_HEADERS,
            params=query
        )

        return json.loads(response.text)
    except:
        print(f"Attempt to get item failed")

def get_board_items(list_id):
    """
    Fetches all saved items from the Trello board.

    Returns:
        list: The list of saved items.
    """

    query = {
        'key': os.getenv('TRELLO_API_KEY'),
        'token': os.getenv('TRELLO_API_TOKEN'),
        'cards': 'open'
    }

    try:
        response = requests.request(
            "GET",
            f"{BASE_URL}/lists/{list_id}",
            params=query
        )

        return json.loads(response.text)["cards"]
    except:
        print(f"Attempt to get items for board failed")

def update_status(item_id, list_id):
    """
    Moves an item to the specified list on the Trello board.

    Returns:
        card: The card that was moved to a new list.
    """

    query = {
        'key': os.getenv('TRELLO_API_KEY'),
        'token': os.getenv('TRELLO_API_TOKEN'),
        'idList': list_id
    }
    
    try:
        requests.request(
            "PUT",
            f"{BASE_URL}/cards/{item_id}",
            headers=DEFAULT_HEADERS,
            params=query
        )
    except:
        print(f"Attempt to mark item incomplete failed")

def delete_board_item(item_id):
    """
    Deletes an item on the Trello board.

    Returns:
        None.
    """

    query = {
        'key': os.getenv('TRELLO_API_KEY'),
        'token': os.getenv('TRELLO_API_TOKEN')
    }
    
    try:
        requests.request(
            "DELETE",
            f"{BASE_URL}/cards/{item_id}",
            params=query
        )
    except:
        print(f"Attempt to delete item failed")