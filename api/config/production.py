from .development import Development


class Production(Development):
    DEBUG = False
