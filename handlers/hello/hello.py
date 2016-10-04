# sample handler - the function, not the class, is the handler
from handlers import BaseHandler
from lib.responses import Response


class Hello(BaseHandler):

    def get(self, event, context):
        from nltk import word_tokenize
        return Response(body={"message": "Hello; import from nltk worked!",
                              "event": event})

    def post(self, event, context):
        name = event['body'].get('name')
        return Response(body={"message": "Hello, {}!".format(name),
                              "event": event})
