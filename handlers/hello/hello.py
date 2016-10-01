from handlers import BaseHandler
from lib.responses import Response


class Hello(BaseHandler):

    def get(self, event, context):
        return Response(body={"message": "Hello via Serverless v1.0!",
                              "event": event})

    def post(self, event, context):
        name = event['body'].get('name')
        return Response(body={"message": "Hello, {}!".format(name),
                              "event": event})
