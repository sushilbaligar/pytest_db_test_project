

import pytest
from apitest.src.utilities.requestsUtilities import requestsUtility

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_customers():
    req_helper = requestsUtility()
    rs_get_response = req_helper.get('customers')
    assert  rs_get_response,f'Get request API response is empty'