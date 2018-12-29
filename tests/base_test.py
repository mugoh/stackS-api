import unittest
from app import create_app
from flask import jsonify
import json


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        # create new user
        self.user_data = jsonify(
            username="Domesticable Cow",
            email="cow@mammals.milkable",
            password="pa55word")

        response = self.client.post('/api/v1/auth/register',
                                    data=self.user_data,
                                    content_type='application/json')
        self.new_user = json.loads(response.data.decode())
