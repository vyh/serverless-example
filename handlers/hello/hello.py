# sample handler - the function, not the class, is the handler
from handlers import BaseHandler
from lib.responses import Response


class Hello(BaseHandler):

    def get(self, event, context):
        return Response(body={
            "message": "Go sls v1.0! Your function executed successfully!",
            "event": event
        })

    def post(self, event, context):
        return Response(body={
            "message": "Hello, {}!".format(event['body'].get('name'))
        })
