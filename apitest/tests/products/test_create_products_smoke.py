import pytest
from apitest.src.utilities.genericUtilities import generate_random_string
from apitest.src.helpers.ProductsHelper import ProductsHelper
from apitest.src.dao.productdao import ProductsDao
from first_test import pytestmark

pytestmark = [pytest.mark.products,pytest.mark.smoke]

@pytest.mark.tcid26
def test_create_1_simple_product():

    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = '10.99'

    # make the call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs,f"Create product response is empty,payload:{payload}"
    assert product_rs['name'] == payload['name'],f"Create product api call"\
    f"has unexpected name. Actual:{product_rs['name']} Expected:{payload['name']}"

    # verify the product exists in db
    db_prod_rs = ProductsDao().get_product_from_id(product_rs['id'])
    assert payload['name'] == db_prod_rs[0]['post_title'],f"Create product: Title in DB and API "\
    f" does not match. DB:{db_prod_rs['post_title']} API:{payload['name']}"
