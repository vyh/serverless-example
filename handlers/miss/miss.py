from handlers import BaseHandler
from lib.responses import HTTPNotFound


class Miss(BaseHandler):

    def get(self, event, context):
        raise HTTPNotFound("Not found.\n" + str(event['test']))

    def post(self, event, context):
        raise HTTPNotFound()
