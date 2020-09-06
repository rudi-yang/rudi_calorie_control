import datetime
import traceback


class EntityCalorieControl:
    def __init__(self):
        self.action = ""
        self.cate = ""
        self.detail = ""
        self.ds = None

    def build(self, action, cate, detail, ds):
        self.action = action
        self.cate = cate
        self.detail = detail
        self.ds = ds
        return True
