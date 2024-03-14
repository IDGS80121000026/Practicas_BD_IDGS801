# se van a concentrar las confguraciones a inplementra 
# acceso a base de datos

import os
from sqlalchemy import create_engine
import urllib 
from dataclasses import dataclass

class Config(object):
    SECRET_KEY='clave nueva'
    SESSION_COOKIE_SECURE =False
    
    
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@127.0.0.1/pizzeria'
    SQLALQUEMY_TRANCK_MODIFICATIONS=False


