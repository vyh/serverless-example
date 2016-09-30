from lib.responses import HTTPBadRequest


class BaseHandler(object):

    def __call__(self, event, context):
        if 'POST' == event['method']:
            return self.post(event, context)
        if 'GET' == event['method']:
            return self.get(event, context)

    def get(self, event, context):
        raise HTTPBadRequest("Unsupported Method")

    def post(self, event, context):
        raise HTTPBadRequest("Unsupported Method")
