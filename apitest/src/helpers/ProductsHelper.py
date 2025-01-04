from random import random
from venv import logger

from apitest.src.dao.productdao import ProductsDao
from apitest.src.utilities.requestsUtilities import requestsUtility

class ProductsHelper(object):
    def __init__(self):
        self.requests_utility = requestsUtility()


    def get_product_by_id(self,prod_id):
        return self.requests_utility.get(f"products/{prod_id}")

    def call_create_product(self,payload):
        return self.requests_utility.post("products",payload)

    def get_all_products(self,payload=None):
        max_pages = 1000
        all_products = []
        for i in range(1,max_pages+1):
            logger.debug(f"List products page no:{i}")
            if not 'per_page' in payload.keys():
                payload['per_page']=100
            # add the current page no to the call
            payload['page'] = i
            rs_api = self.requests_utility.get("products", payload=payload)
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products