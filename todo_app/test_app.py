from dotenv import load_dotenv, find_dotenv
from todo_app import app
import pytest
import requests
import os
import json

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.text = json.dumps(fake_response_data)
    
def stub(method, url, params={}):
    todo_list_id = os.environ.get('TRELLO_TODO_LIST_ID')
    done_list_id = os.environ.get('TRELLO_DONE_LIST_ID')

    if url == f'https://api.trello.com/1/lists/{todo_list_id}':
        fake_response_data = {
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card 1', 'idList': todo_list_id}]
        }
        return StubResponse(fake_response_data)
    
    if url == f'https://api.trello.com/1/lists/{done_list_id}':
        fake_response_data = {
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card 2', 'idList': done_list_id}]
        }
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_get_index_page(client, monkeypatch):
    monkeypatch.setattr(requests, 'request', stub)
    monkeypatch.setattr(requests, 'request', stub)
    
    response = client.get('/')

    assert response.status_code == 200
    assert 'Tesjsdhbjs 1' in response.data.decode()
    assert 'Test card 2' in response.data.decode()
