from lib.responses import HTTPBadRequest


class BaseHandler(object):

    def process_request(self, event, context):
        if 'POST' == event['method']:
            return self.post(event, context)
        if 'GET' == event['method']:
            return self.get(event, context)

    def get(self, event, context):
        raise HTTPBadRequest("Unsupported Method")

    def post(self, event, context):
        raise HTTPBadRequest("Unsupported Method")


from hello import Hello  # NOQA
from second import Second  # NOQA
from content_type import ContentTypeHandler  # NOQA
from error import Miss
