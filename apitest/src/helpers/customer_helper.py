from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.utilities.requestsUtilities import requestsUtility

class customer_helper(object):
    def __init__(self):
        self.requests_utility = requestsUtility()

    def create_customer(self,email=None,password=None,**kwargs):
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'password'

        payload = dict()
        payload['email']=email
        payload['password']=password
        payload.update(kwargs)
        return_json = self.requests_utility.post('customers',payload=payload)
        return return_json