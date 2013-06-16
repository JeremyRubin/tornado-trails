#Import all main libs
from Imports import *
# Import all handlers
from BaseHandler import BaseHandler
from MainPage import MainPage
from User import AddUserHandler, LoginHandler, LogoutHandler
NAME = "Application"
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainPage),
                    (r"/login/?", LoginHandler),
                    (r"/logout/?", LogoutHandler),
                     (r"/add/user/?", AddUserHandler),
                     (r"/d/?", Debug),]
                    
        settings = dict(cookie_secret="GENERATE YOUR OWN SECRET MORE SECURE THAN THIS",
                        login_url="/login",
                        template_path=os.path.join(os.path.dirname(__file__), "templates"),
                        static_path=os.path.join(os.path.dirname(__file__), "static"),
                        xsrf_cookies=True,
                        debug=True,
                        xheaders=True,
                        autoescape=None,
                        )
        tornado.web.Application.__init__(self, handlers, **settings)

class Debug(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.db.users.find({}, callback=(yield tornado.gen.Callback("t")))
        respone = yield tornado.gen.Wait("t")
        print respone
        self.write("yes")
        self.finish()