import os
from os.path import dirname
from dotenv import load_dotenv

environment = os.environ.get("ENV", "development").lower()

if environment == "production":
    envfilenamesuffix = "prod"
else:
    envfilenamesuffix = "local"

environment = os.environ.get("ENV", "development").lower()
current_path = dirname(__file__)
parent = os.path.abspath(os.path.join(current_path, os.pardir))
dotenv_path = os.path.join(parent, "environments",f"env.{envfilenamesuffix}")


print("Loading .env file :",dotenv_path)


load_dotenv(dotenv_path)

if environment == "production":
    from .prod import *
else:
    from .local import *

