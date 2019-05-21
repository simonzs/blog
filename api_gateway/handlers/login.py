from api_gateway.handlers import base

class LoginHandler(base.DemoHandler):
    
    def do_get(self):
        self.write("this login")


class LogoutHandler(base.DemoHandler):
    
    def do_get(self):
        get_url = self.reverse_url('logout')
        self.write(get_url)
