import pymysql
from pymysql import cursors
from apitest.src.utilities.credentialUtilities import credentialutilities

class dbutility(object):

    def __init__(self):
        creds_helper = credentialutilities()
        self.creds = creds_helper.get_db_credentials()
        self.host = 'localhost'


    def create_connection(self):
        connection = pymysql.connect(host=self.host,user=self.creds['db_user'],password=self.creds['db_password'],port=10006)
        return connection


    def execute_select(self,sql):
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql:{sql} \n Error:{str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self,sql):
        pass