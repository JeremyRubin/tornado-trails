#Import all main libs
from Imports import *
# Import all handlers
from handlers.BaseHandler import BaseHandler
from handlers.MainPage import MainPage
from handlers.User import AddUserHandler, LoginHandler, LogoutHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/?", MainPage),
                    (r"/login/?", LoginHandler),
                    (r"/logout/?", LogoutHandler),
                     (r"/add/user/?", AddUserHandler),
                     ]
        if config["devmode"]: handlers.append((r"/d/?", Debug))

        if config["route_prefix"]:
            handlers = [(config["route_prefix"]+route,handler) for route, handler in handlers]
                    
        settings = dict(cookie_secret=config["cookie_secret"],
                        login_url="/login",
                        template_path=os.path.join(os.path.dirname(__file__), "templates"),
                        static_path=os.path.join(os.path.dirname(__file__), config["static_location"]),
                        xsrf_cookies=True,
                        debug=config["devmode"],
                        xheaders=True,
                        autoescape=None,
                        gzip=True,
                        )
        tornado.web.Application.__init__(self, handlers, **settings)


# Put Debug code here if need be
class Debug(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.db.users.find({}, callback=(yield tornado.gen.Callback("t")))
        respone = yield tornado.gen.Wait("t")
        print respone
        self.write("yes")
        self.finish()