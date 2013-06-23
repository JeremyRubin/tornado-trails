#Brought to you by Jeremy Rubin, 2013


class BaseModel(object,tornado.web.RequestHandler): #find a better way to connect?
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
