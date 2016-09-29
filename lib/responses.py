# common source for responses
import json


class Response(dict):
    def __init__(self, status=200, content_type='application/json', content=None):  # NOQA
        super(Response, self).__init__(status=status,
                                       content_type=content_type,
                                       content=Response.stringify(content))

    @property
    def status(self):
        return self['status']

    @status.setter
    def status(self, status):
        self['status'] = status

    @property
    def content_type(self):
        return self['content_type']

    @content_type.setter
    def content_type(self, content_type):
        self['content_type'] = content_type

    @property
    def content(self):
        return self['content']

    @content.setter
    def content(self, content):
        self['content'] = Response.stringify(content)

    @staticmethod
    def stringify(content):
        if isinstance(content, dict):
            return json.dumps(content)
        return str(content) if content else ""


class HTTPNotFound(Exception):

    def __init__(self, message="Not Found"):
        super(HTTPNotFound, self).__init__(
            json.dumps(Response(status=404, content={"message": message})))


class HTTPBadRequest(Exception):

    def __init__(self, message="Bad Request"):
        super(HTTPBadRequest, self).__init__(
            json.dumps(Response(status=400, content=message)))
