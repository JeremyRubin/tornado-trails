#Brought to you by Jeremy Rubin, 2013
from App import *

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db=self.application.settings['db']
        return self._db
    def date_handler(self, obj):
        if isinstance(obj, datetime.datetime):
            return "Time is in Progress"
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj
    def get_current_user(self):
        user_JSON = self.get_secure_cookie("user")
        if not user_JSON: return None
        return tornado.escape.json_decode(user_JSON)