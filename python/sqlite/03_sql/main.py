from core import config
from db import manager
config.create_dirt()
manager.DBManager(config.NAME_DB)