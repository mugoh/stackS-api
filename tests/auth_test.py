from .base_test import BaseTestCase
import json
from flask import jsonify


class AuthTestCases(BaseTestCase):
    """
    Tests user authentication

    """

    def test_get_registered_users(self):
        response = self.client.get('/api/v1/auth/register',
                                   data=self.user_data,
                                   content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertTrue(isinstance(res, list),
                        msg="Fails to return user records as list")

        self.assertEqual(response.status_code, 200)

    def test_registrer_already_registered_user(self):

        response = self.client.post('/api/v1/auth/register',
                                    data=self.user_data,
                                    content_type='application/json')
        res = json.loads(response.data.decode())

        res_msg = "Account exists. Maybe log in?"
        self.assertEqual(res,
                         res_msg,
                         msg="Fails to registration of existing account")
