import random
from venv import logger

from apitest.src.utilities.dbutility import dbutility


class CustomerDao(object):

    def __init__(self):
        self.db_helper = dbutility()

    def get_customer_by_email(self,email):

        sql = f"SELECT * from local.wp_users WHERE user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_random_customer_email(self,qty=1):
        sql = f"SELECT * FROM local.wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql,qty)