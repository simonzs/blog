
import os
import tornado.options
from tornado.options import define

define(name='port', default=9000, type=int, multiple=False, help="run on the given port")
define('')

settings = {
    #"debug": True,
    "autoreload": True,
    "compiled_template_cache": False,
    "static_hash_cache": False,
    "serve_traceback": True,
    "path": os.path.dirname(__file__),
}

class APISettings():
    def __init__(self):
        #tornado.options.options.logging = None
        tornado.options.parse_command_line()

_settings = APISettings()
