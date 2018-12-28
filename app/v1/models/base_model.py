"""
This module contains the generic models from which other
models inherit commin functionalities from

"""
import datetime


class BaseModel:

    def __init__(self, data):
        self.created_at = datetime.datetime.utcnow()
        self.id = len(data) + 1

    def delete(self, data, item):
        return data.remove(item)
