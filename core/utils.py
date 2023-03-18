from ldap3 import Server, Connection
from django import db
from functools import wraps


def close_old_connections(func):
    """
    A decorator that ensures that Django database connections that have become unusable, or are obsolete, are closed
    before and after a method is executed (see: https://docs.djangoproject.com/en/dev/ref/databases/#general-notes
    for background).

    This decorator is intended to be used to wrap APScheduler jobs, and provides functionality comparable to the
    Django standard approach of closing old connections before and after each HTTP request is processed.

    It only makes sense for APScheduler jobs that require database access, and prevents `django.db.OperationalError`s.
    """

    @wraps(func)
    def func_wrapper(*args, **kwargs):
        db.close_old_connections()
        try:
            result = func(*args, **kwargs)
        finally:
            db.close_old_connections()

        return result

    return func_wrapper