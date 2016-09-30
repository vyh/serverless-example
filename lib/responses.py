# common source for responses
import json


class Response(dict):
    def __init__(self, statusCode=200, headers=None, body=None):  # NOQA
        super(Response, self).__init__(statusCode=statusCode,
                                       headers=Response.init_headers(headers),
                                       body=Response.stringify(body))

    @property
    def status(self):
        return self['status']

    @status.setter
    def status(self, status):
        self['status'] = status

    @property
    def headers(self):
        return self['headers']

    @headers.setter
    def headers(self, headers):
        # keys, values must be str - not checking that
        if isinstance(headers, dict):
            self['headers'].update(headers)

    @property
    def body(self):
        return self['body']

    @body.setter
    def body(self, body):
        self['body'] = Response.stringify(body)

    @staticmethod
    def init_headers(headers):
        default = {'Content-Type': 'application/json'}
        headers = headers if isinstance(headers, dict) else default
        if 'Content-Type' not in headers:
            headers.update(default)
        return headers

    @staticmethod
    def stringify(body):
        if isinstance(body, dict):
            return json.dumps(body)
        return str(body) if body else ""


class HTTPNotFound(Exception):

    def __init__(self, message="Not Found"):
        super(HTTPNotFound, self).__init__(
            json.dumps(Response(statusCode=404, body={"message": message})))


class HTTPBadRequest(Exception):

    def __init__(self, message="Bad Request"):
        super(HTTPBadRequest, self).__init__(
            json.dumps(Response(statusCode=400, body={"message": message})))
