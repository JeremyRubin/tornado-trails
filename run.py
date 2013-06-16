#Brought to you by Jeremy Rubin, 2013
from App import *
define("port", default=config["default_port"], help="run on the given port", type=int)
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()