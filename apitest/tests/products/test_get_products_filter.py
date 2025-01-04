from dataclasses import replace

import pytest
from datetime import datetime, timedelta

from apitest.src.dao.productdao import ProductsDao
from apitest.src.helpers.ProductsHelper import ProductsHelper

@pytest.mark.regression
class TestGetProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):

        # create data
        x_days_from_today = 300
        _after_date = datetime.now().replace(microsecond=0)-timedelta(days=x_days_from_today)
        after_date = _after_date.isoformat()
        payload = dict()
        payload['after'] = after_date

        # make the call
        prod_rs = ProductsHelper().get_all_products(payload)
        assert prod_rs,f"Empty response for 'list products with filter'"

        # get data from db
        db_products = ProductsDao().get_products_created_after_given_date(after_date)

        # verify the response matches db response
        assert len(prod_rs) == len(db_products), f"List products with filter 'after'"\
        f" returned unexpected number of products. Expected:{len(prod_rs)} Actual:{len(db_products)}"

        ids_in_api = [i['id'] for i in prod_rs]
        ids_in_db = [i['ID'] for i in db_products]
        id_diff = list(set(ids_in_api)-set(ids_in_db))
        assert not id_diff,f"List Products with 'after' filter: Mismatch in IDs Listed."