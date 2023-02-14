import os

environment = os.environ.get("ENV", "development").lower()

if environment == "production":
    from .prod import *
else:
    from .local import *
