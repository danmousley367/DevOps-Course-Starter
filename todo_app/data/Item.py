class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_db(cls, db_item):
        return cls(db_item['_id'], db_item['name'], db_item['status'])
    
    def __eq__(self, other):
        return self.id == other.id and \
               self.name == other.name and \
               self.status == other.status