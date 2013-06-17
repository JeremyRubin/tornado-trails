#Brought to you by Jeremy Rubin, 2013
from App import *

class BaseModel(object):
    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = asyncmongo.Client(pool_id=config["db_pool"], host='127.0.0.1', port=27017, maxcached=10, maxconnections=50, dbname=config["db_name"])
        return self._db
    def date_handler(self, obj):
        if isinstance(obj, datetime.datetime):
            return "Time is in Progress"
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj
