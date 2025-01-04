import os


class credentialutilities(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("The api credentials WC_KEY and WC_SECRET env variable not set!!")
        else:
            return{'wc_key':wc_key,'wc_secret':wc_secret}

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("The api credentials db_user and db_password env variable not set!!")
        else:
            return{'db_user':db_user,'db_password':db_password}