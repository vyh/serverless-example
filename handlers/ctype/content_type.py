from handlers import BaseHandler
from lib.responses import Response, HTTPBadRequest


class ContentTypeHandler(BaseHandler):

    def get(self, event, context):
        content_type = event['path'].get('type', '').lower()

        if 'html' == content_type:
            return Response(
                headers={'Content-Type': 'text/html'},
                body="<html><head><title>Page title</title></head>"
                     "<body>This is an html response.</body></html>")

        if 'csv' == content_type:
            return Response(headers={"Content-Type": "text/csv"},
                            body="type,v1,v2,v3\ncsv,1,2,3")

        raise HTTPBadRequest("Unsupported content type. Options: html, csv")
