"""from django.db import utils
from .models import RegUser


class RegUserRouter:
    def db_for_read(self, model, **hints):
        if model == RegUser:
            return 'my_sql'
        return None

    def db_for_write(self, model, **hints):
        if model == RegUser:
            return 'my_sql'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1.__class__ == obj2.__class__ == RegUser:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'pfaApp' and model_name == 'RegUser':
            return db == 'my_sql'
        return None"""
