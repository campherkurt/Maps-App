from functools import wraps
from flask import g, request, redirect, url_for

def method_handler(handler_class):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if request.method == "GET":
                return handler_class.get()
            if request.method == "POST":
                return handler_class.post()
            if request.method == "PUT":
                return handler_class.put()
            if request.method == "DELETE":
                return handler_class.delete()
        return decorated_function
    return decorator