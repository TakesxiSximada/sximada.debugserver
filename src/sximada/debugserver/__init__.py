# -*- coding: utf-8 -*-
u""""""
import sys
import argparse
import ipdb
from tornado.web import (
    Application,
    RequestHandler,

)
from tornado.ioloop import IOLoop

__version__ = '0.1.dev0'


class DebugHandler(RequestHandler):
    def get(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def head(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def post(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def delete(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def patch(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def put(self, *args, **kwds):
        ipdb.set_trace()
        pass

    def options(self, *args, **kwds):
        ipdb.set_trace()
        pass


def make_app():
    return Application([
        (r"(.*)", DebugHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8000)
    args = parser.parse_args(argv)

    app = make_app()
    app.listen(args.port)

    mainloop = IOLoop.current()
    mainloop.start()

if __name__ == '__main__':
    main()
