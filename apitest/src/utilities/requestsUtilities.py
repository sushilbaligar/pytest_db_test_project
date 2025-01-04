from venv import logger
import requests
from apitest.src.configs.hosts_config import API_HOSTS
import os
import json
from requests_oauthlib import OAuth1
from apitest.src.utilities.credentialUtilities import credentialutilities

class requestsUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV','test')
        self.base_url = API_HOSTS[self.env]

    def post(self,endpoint,payload=None,headers=None):
        if not headers:
            headers = {"Content-Type":"application/json"}

        url = self.base_url+endpoint
        wc_key_dict = credentialutilities.get_wc_api_keys()

        self.auth = OAuth1(wc_key_dict['wc_key'],wc_key_dict['wc_secret'])
        rs_api = requests.post(url=url,data=json.dumps(payload),headers=headers,auth=self.auth)
        logger.info(f"Status Code:{rs_api.status_code}")
        logger.debug(f"API POST RESPONSE:{rs_api.json()}")
        return rs_api.json()

    def get(self,endpoint,payload=None,headers=None):
        if not headers:
            headers = {"Content-Type":"application/json"}

        url = self.base_url+endpoint
        wc_key_dict = credentialutilities.get_wc_api_keys()

        self.auth = OAuth1(wc_key_dict['wc_key'],wc_key_dict['wc_secret'])
        rs_api = requests.get(url=url,data=json.dumps(payload),headers=headers,auth=self.auth)
        logger.info(f"Status Code:{rs_api.status_code}")
        logger.debug(f"API GET RESPONSE:{rs_api.json()}")
        return rs_api.json()