from handlers import BaseHandler
from lib.responses import HTTPNotFound


class Miss(BaseHandler):

    def get(self, event, context):
        raise HTTPNotFound()

    def post(self, event, context):
        raise HTTPNotFound()
