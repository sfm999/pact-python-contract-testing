import atexit
import requests
import unittest

from pact import Consumer, Provider

# Note how we're simulating the host and port, as well as declaring the folder we'd like our pacts to be stored in
pact = Consumer('UserConsumer').has_pact_with(Provider('UserProvider'),host_name='localhost', port='8000', pact_dir='./pacts')
# Start the external Mock Service
pact.start_service()
# Register pact.stop_service as a valid way of exiting the program.
atexit.register(pact.stop_service)

def get_user(uid: int):
    """Method used to simulate HTTP call to API.
       Returns the json data from the request"""
    uri = 'http://localhost:8000/users/' + str(uid)
    return requests.get(uri).json()

class GetUserInfoContract(unittest.TestCase):
    """Class tests the user related endpoints in our API"""
    def test_get_user(self):
        """Declares an expected response then sets up the pact
           to get the result from the mock API service then compare
           it with the expected values we declared."""
        expected = {
            "Name": "Bob",
            "Age": 32
        }

        (pact
         .given('User exists with ID of 1')
         .upon_receiving('a request for a user with an ID of 1')
         .with_request('get', '/users/1')
         .will_respond_with(200, body=expected))
        
        with pact:
            result = get_user(1)

        self.assertEqual(result, expected)
