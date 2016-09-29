# sample handler - the function, not the class, is the handler
from . import BaseHandler
from lib.responses import Response


class Second(BaseHandler):

    def get(self, event, context):
        return Response(content={"message": self.message, "event": event})

    @property
    def message(self):
        return "This was sent by a message method/property. Thrills and excite."  # NOQA
