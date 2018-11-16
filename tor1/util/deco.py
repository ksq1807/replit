from util import utils
import json


def auth_login_redirect(func):
    def inner(self, *args, **kwargs):
        cookie = self.get_secure_cookie("username")
        isredict = False
        if cookie != None:
            username = cookie.decode()
            data = utils.getMem(username)
            if data != None:
                func(self, *args, **kwargs, data=json.loads(data))
                utils.setMem(key=username, values=data)
            else:
                isredict = True
        else:
            isredict = True
        if isredict == True:
            self.redirect('/')

    return inner
