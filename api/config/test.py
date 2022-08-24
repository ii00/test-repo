import os

from .local import Local

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Testing settings used only from within pytest
class Test(Local):
    INSTALLED_APPS = Local.INSTALLED_APPS
    TESTING = True
