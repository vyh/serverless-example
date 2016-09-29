# sample handler - the function, not the class, is the handler
from . import BaseHandler
from lib.responses import Response


class Hello(BaseHandler):

    def get(self, event, context):
        return Response(content={
            "message": "Go sls v1.0! Your function executed successfully!",
            "event": event
        })

    def post(self, event, context):
        return Response(content={
            "message": "Hello, {}!".format(event['body'].get('name'))
        })
