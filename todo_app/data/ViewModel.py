import os

class ViewModel:
    def __init__(self, items, done_list_id = None, to_do_list_id = None):
        self._items = items
        self._done_list_id = done_list_id or os.getenv('TRELLO_DONE_LIST_ID')
        self._todo_list_id = to_do_list_id or os.getenv('TRELLO_TODO_LIST_ID')
 
    @property
    def items(self):
        return self._items
    
    @property
    def done_list_id(self):
        return self._done_list_id
    
    @property
    def done_items(self):
        return [item for item in self._items if item.list_id == self._done_list_id]
    
    @property
    def todo_items(self):
        return [item for item in self._items if item.list_id == self._todo_list_id]