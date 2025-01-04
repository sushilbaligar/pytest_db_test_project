
import pytest
import logging as logger

from apitest.src.helpers.customer_helper import customer_helper
from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.dao.customerdao import CustomerDao
from apitest.src.utilities.requestsUtilities import requestsUtility

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_email_pwd():

    # generate random email and password

    logger.info("create customer with email pwd only.")
    logger.debug("DEBUG - create customer with email pwd only.")
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    pwd = rand_info['password']

    # make the call

    cust_obj = customer_helper()
    cust_api_info = cust_obj.create_customer(email=email,password=pwd)
    #logger.info(f'\n customer info **************************************\n{cust_api_info}\n**************************************\n')

    # verify the email in the response

    assert cust_api_info['email'] == email,f"Wrong email. email should be {email}"
    assert cust_api_info['first_name'] == '',f'First name has value. \
    It should be empty'

    # verify customer is created in database

    cust_dao = CustomerDao()
    cust_info = cust_dao.get_customer_by_email(email)
    #logger.info(f'\n customer info **************************************\n{cust_info}\n**************************************\n')
    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db,f'create customer response ID not same as ID in DB \
    Email: {email}'

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_existing_email():

    # get random email from db

    cust_dao = CustomerDao()
    rand_cust = cust_dao.get_random_customer_email()
    rand_email = rand_cust[0]['user_email']

    # create customer with same email id
    req_helper = requestsUtility()
    payload = {'email': rand_email, 'password': 'Password1'}
    cust_api_info = req_helper.post(endpoint='customers',payload=payload)
    assert cust_api_info['code'] == 'registration-error-email-exists',f"Expected:'registration-error-email-exists',Actual:{cust_api_info['code']}"
    assert cust_api_info['message'] == 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>',\
    f"Expected:'An account is already registered with your email address. <a href=\"#\" class=\"showlogin\">Please log in.</a>'"\
    f"Actual:{cust_api_info['message']}"