""" example """
import json
import falcon
import jsend
from boilerplate_sdk.example import Example

def run():
    """ run function"""
    api = falcon.API()
    api.add_route('/page/{name}', Page())
    api.add_sink(Page().default_error, '')
    return api

class Page():
    """ Page class """
    example = None

    def on_get(self, _req, _resp, name):
        """ on page GET requests """
        dispatch = None
        if hasattr(self.__class__, name) and callable(getattr(self.__class__, name)):
            dispatch = getattr(self, name)
            self.example = Example()
        else:
            dispatch = self.default_page
        dispatch(_req, _resp)

    def default_page(self, _req, _resp):
        """ default page response """
        msg = {'message': 'hello'}
        _resp.body = json.dumps(jsend.success(msg))
        _resp.status = falcon.HTTP_200

    def default_error(self, _req, resp):
        """Handle default error"""
        msg = falcon.HTTP_404
        status = falcon.HTTP_404
        resp.status = status
        msg_error = jsend.error(msg)
        resp.body = json.dumps(msg_error)

    def get_posts(self, _req, resp):
        """ example get_posts response """
        responses = self.example.get_posts({'userId':'1'})
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(responses)
