import random
from venv import logger

from apitest.src.utilities.dbutility import dbutility


class ProductsDao(object):

    def __init__(self):
        self.db_helper = dbutility()

    def get_random_product_from_db(self,qty=1):
        sql = f"SELECT * FROM local.wp_posts WHERE post_type='product' LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql,qty)

    def get_product_from_id(self,product_id):
        sql = f"SELECT * FROM local.wp_posts WHERE ID={product_id};"
        return self.db_helper.execute_select(sql)

    def get_products_created_after_given_date(self,date):
        sql = f"SELECT * from local.wp_posts WHERE post_type='product' and post_date>'{date}' LIMIT 100;"
        return self.db_helper.execute_select(sql)
