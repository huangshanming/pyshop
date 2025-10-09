from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin

class ReconnectMysqlDatabase(PooledMySQLDatabase, ReconnectMixin):
    pass

MYSQL_DB = "ginshop"
MYSQL_HOST = "114.115.151.189"
MYSQL_USER = "ginshop"
MYSQL_PASS = "DAZikswSjTysjbmJ"
MYSQL_PORT = 3306

DB = ReconnectMysqlDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASS)