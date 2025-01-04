from venv import logger

import pytest
from apitest.src.utilities.requestsUtilities import requestsUtility
from apitest.src.dao.productdao import ProductsDao
from apitest.src.helpers.ProductsHelper import ProductsHelper

pytestmark = [pytest.mark.products,pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
    req_helper = requestsUtility()
    rs_get_response = req_helper.get('products')
    assert  rs_get_response,f'Get request API response is empty'

@pytest.mark.tcid25
def test_get_product_from_id():

    # get product (test data) from db
    rand_prod = ProductsDao().get_random_product_from_db()
    rand_prod_id = rand_prod[0]['ID']
    db_post_title_name = rand_prod[0]['post_title']

    # make the call
    prod_helper = ProductsHelper()
    rs_api = prod_helper.get_product_by_id(rand_prod_id)
    api_name = rs_api['name']

    # verify the response
    assert db_post_title_name == api_name,f"Get Product by ID returned\
    wrong product. ID:{rand_prod_id}, DB_NAME:{db_post_title_name},\
    API_NAME:{api_name}"
