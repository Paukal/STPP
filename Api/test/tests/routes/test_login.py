from http import HTTPStatus

import requests

from test.resources import credentials
from test.tests.routes.routes_tc import RoutesTC


class TestUsers(RoutesTC):
	PATH = RoutesTC.server_address+"/login"

	def test_correct_credentials(self):
		response: requests.Response = requests.post(self.PATH, json=credentials.testUserCreds)
		self.assertEqual(HTTPStatus.OK, response.status_code)

	def test_wrong_credentials(self):
		response: requests.Response = requests.post(self.PATH, json={"login": "nonexistentuser", "password": "badpassword"})
		self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)
