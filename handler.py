from handlers import (
    Hello, Second, ContentTypeHandler, Miss
)

hello = Hello().process_request
second = Second().process_request
ctype = ContentTypeHandler().process_request
miss = Miss().process_request
