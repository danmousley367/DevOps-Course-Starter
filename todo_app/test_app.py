from dotenv import load_dotenv, find_dotenv
from todo_app import app
import pytest
import mongomock
import pymongo
from todo_app.data.Status import Status

from flask_dance.consumer.storage import MemoryStorage
from oauth import blueprint

@pytest.fixture
def client(monkeypatch):
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    storage = MemoryStorage({"access_token": "fake-token"})
    monkeypatch.setattr(blueprint, 'storage', storage)

    # Use the app to create a test_client that can be used in our tests.
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_get_index_page(client):
    mongo_client = pymongo.MongoClient('fakemongo.com')
    db = mongo_client.todo_app_db
    items_list = db.todo_list

    items_list.insert_many([
        {
            "name": "Test item 1",
            "status": Status.TODO.value
         },
         {
            "name": "Test item 2",
            "status": Status.COMPLETE.value
         },
    ])
    
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test item 1' in response.data.decode()
    assert 'Test item 2' in response.data.decode()
