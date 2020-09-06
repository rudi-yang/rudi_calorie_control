import datetime

import pandas as pd
import sqlite3
import os

from src.dao.dao import *
from src.entity.entity_time_control import EntityCalorieControl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams["font.family"] = 'Arial Unicode MS'


class RudiControl():
    def __init__(self):
        PATH_RES = "./res"
        PATH_DATABASE = os.path.join(PATH_RES, "DataBase.db")
        self.conn = sqlite3.connect(PATH_DATABASE)
        self.dao = Dao(self.conn)

        self.init()

    def init(self):
        self.dao.create_table()

    def instert_time_control(self, action, cate, detail, ds):
        # 检查数据是否冲突
        entity = EntityCalorieControl()

        if entity.build(action, cate, detail, ds):
            self.dao.insert_record(entity)
        else:
            pass

    def delete_time_control_by_id(self, *ids):
        for id in ids:
            self.dao.drop_by_id(id)

    def get_data_all(self):
        data = pd.read_sql('select * from calorie_control', self.conn)
        return data

    def get_data_recent_2_days(self):
        data = pd.read_sql('select * from calorie_control', self.conn)

        dt_now = datetime.datetime.now()
        dt_before = datetime.datetime.now() + datetime.timedelta(days=-1)
        dt_now_integer = int(dt_now.strftime("%Y%m%d"))
        dt_before_integer = int(dt_before.strftime("%Y%m%d"))

        data = data[data["ds"] <= dt_now_integer]
        data = data[data["ds"] >= dt_before_integer]
        return data

    def show_time_distribution_till_now(self, cnt_day):
        data = self.get_data_all()

        dt_now = datetime.datetime.now()
        dt_before = datetime.datetime.now() + datetime.timedelta(days=-cnt_day)

        dt_now_integer = int(dt_now.strftime("%Y%m%d"))
        dt_before_integer = int(dt_before.strftime("%Y%m%d"))

        data = data[data["ds"] <= dt_now_integer]
        data = data[data["ds"] >= dt_before_integer]

        self._show_stat(data, "近%s时间消耗 %s-%s" % (cnt_day, dt_before_integer, dt_now_integer))

        return data

    def _show_stat(self, data, title):

        data["t"] = 1
        stat = data.groupby(["action", "cate"]).agg({"t": "sum"})
        stat = stat.reset_index()

        print(stat)
        stat["name"] = stat["action"] + "-" + stat["cate"]

        print(stat)

        plt.pie(x=stat["t"], labels=stat["name"])
        plt.title(title)
        plt.show()


if __name__ == '__main__':
    rudi_control = RudiControl()
    entity = EntityCalorieControl()
