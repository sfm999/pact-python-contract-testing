import unittest
import atexit
import uvicorn

from main import app

from pact import Consumer, Provider

from reqs import get_user

pact = Consumer('UserConsumer').has_pact_with(Provider('UserProvider'),host_name='localhost', port='8000', pact_dir='./pacts')
pact.start_service()
atexit.register(pact.stop_service)

class GetUserInfoContract(unittest.TestCase):
    def test_get_user(self):
        expected = {
            "Name": "Bob",
            "Age": 32
        }

        (pact
         .given('User exists with ID of 1')
         .upon_receiving('a request for a user with an ID of 1')
         .with_request('get', '/users/1')
         .will_respond_with(200, body=expected))
        
        # pact.setup()
        # uvicorn.run(app, host='localhost', port='8000')

        with pact:
            result = get_user(1)

        # pact.verify()

        self.assertEqual(result, expected)
