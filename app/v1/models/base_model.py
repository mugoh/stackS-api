"""
This module contains the generic models from which other
models inherit commin functionalities from

"""
import datetime


class BaseModel:

    def __init__(self):
        self.created_at = datetime.datetime.utcnow()

    def save(self, data, item):
        data.append(item)

    def get_by_name(self, data, item):
        return [itm for itm in data
                if item['title'] == item['title']][0]

    def get_by_id(self, data, item):
        return [itm for itm in data
                if item['id'] == item['id']][0]

    def delete(self, data, item):
        return data.remove(item)
