import os
from todo_app.data.Status import Status

class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def done_items(self):
        return [item for item in self._items if item.status == Status.COMPLETE.value]
    
    @property
    def todo_items(self):
        return [item for item in self._items if item.status == Status.TODO.value]