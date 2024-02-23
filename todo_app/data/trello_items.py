import requests
import os
import json

BASE_URL = "https://api.trello.com/1/cards"
DEFAULT_HEADERS = {
  "Accept": "application/json"
}
API_KEY = os.getenv('TRELLO_API_KEY')
API_TOKEN = os.getenv('TRELLO_API_TOKEN')
LIST_ID = os.getenv('TRELLO_LIST_ID')

def add_trello_item(title):
    """
    Adds a new item with the specified title to the trello board.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    query = {
        'idList': LIST_ID,
        'key': API_KEY,
        'token': API_TOKEN,
        'name': title
    }
    
    try:
        response = requests.request(
            "POST",
            BASE_URL,
            headers=DEFAULT_HEADERS,
            params=query
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    except:
        print(f"Attempt to create item with title {title} failed")