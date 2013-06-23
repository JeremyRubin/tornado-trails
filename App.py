# Brought to you by Jeremy Rubin, 2013
# Import all main libs
from Imports import *

# Import all handlers/models
from handlers_list import *
# Import Routes

import routes

class Application(tornado.web.Application):
    def __init__(self):
        handlers = routes.handlers
        if config["devmode"]: handlers.append((r"/d/?", Debug))

        if config["route_prefix"]:
            handlers = [(config["route_prefix"]+route,handler) for route, handler in handlers]

        mongodb_uri = os.environ.get('MONGOLAB_URI', 'mongodb://localhost:27017')
        _db = motor.MotorClient(mongodb_uri).open_sync()[config['db_name']]
        settings = dict(cookie_secret=config["cookie_secret"],
                        login_url="/login",
                        template_path=os.path.join(os.path.dirname(__file__), "templates"),
                        static_path=os.path.join(os.path.dirname(__file__), config["static_location"]),
                        xsrf_cookies=True,
                        debug=config["devmode"],
                        xheaders=True,
                        autoescape=None,
                        gzip=True,
                        db=_db,
                        )
        tornado.web.Application.__init__(self, handlers, **settings)


# Put Debug code here if need be
class Debug(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
            cursor = self.db.users.find({"dfadsc":'dfadsc'}).sort('_id').limit(2)
   
            response = yield motor.Op(cursor.to_list)

      
            print response
            print "yes"
            self.write("yes")
            self.finish()
    def crap():
        self.db.users.find({}).to_list( callback=(yield tornado.gen.Callback("t")))
        respone = yield tornado.gen.Wait("t")
        print respone
        self.write("yes")
        self.finish()