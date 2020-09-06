import sqlite3

from src.dao.sql_collection import SqlCollection
from src.entity.entity_time_control import EntityCalorieControl


class Dao():
    def __init__(self, conn):
        self.conn = conn

    def execute_sql(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def execute_query(self, sql):
        c = self.conn.cursor()
        res = c.execute(sql)
        return res

    def create_table(self):
        self.execute_sql(SqlCollection.SQL_CREATE_TABLE_CALORIE_CONTROL)

    def insert_record(self, entity: EntityCalorieControl):
        sql = SqlCollection.SQL_INSERT_CALORIE_CONTROL.format(
            entity.action,
            entity.cate,
            entity.detail,
            entity.ds,
        )
        self.execute_sql(sql)

    def drop_table(self):
        sql = SqlCollection.SQL_DROP_TABLE_CALORIE_CONTROL
        self.execute_sql(sql)

    def drop_by_id(self, id):
        sql = SqlCollection.SQL_DROP_CALORIE_CONTROL_BY_ID.format(id)
        self.execute_sql(sql)
