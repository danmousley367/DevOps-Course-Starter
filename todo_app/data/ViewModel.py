class ViewModel:
    def __init__(self, items, done_list_id):
        self._items = items
        self._done_list_id = done_list_id
 
    @property
    def items(self):
        return self._items
    
    @property
    def done_list_id(self):
        return self._done_list_id