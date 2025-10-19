# sqli_test.py
import unittest
from unittest.mock import patch, MagicMock
import requests 

# --- Target Configuration ---
LOGIN_URL = "http://localhost/api/v1/login"

# Common SQLi payloads to bypass authentication
SQLI_PAYLOADS = [
    "' OR '1'='1' --",  # Classic bypass
    "admin' --",        # Try to log in as 'admin'
    "1' UNION SELECT 1, 'admin', 'password'", # More advanced technique
]

# --- Testing Logic (using unittest to structure the mocks) ---

class TestSQLInjection(unittest.TestCase):
    
    # Helper to create a mock response object
    def _mock_response(self, status=200, text=""):
        mock_resp = MagicMock(spec=requests.Response)
        mock_resp.status_code = status
        mock_resp.text = text
        return mock_resp

    # @patch intercepts the requests.post call and replaces it with our mock
    @patch('requests.post')
    def test_sqli_protection_success(self, mock_post):
        """
        Test Case 1: Application successfully defends against SQLi.
        MOCK: Return an Unauthorized response (HTTP 401).
        """
        # Set the mock to return an unauthorized response (expected safe behavior)
        mock_post.return_value = self._mock_response(
            status=401, 
            text="Invalid username or password"
        )
        
        print("\n--- Testing SQLi Protection (Expected Pass) ---")
        
        for payload in SQLI_PAYLOADS:
            payload_data = {'username': payload, 'password': 'any_pass'}
            
            # The actual line of code that runs against the mock
            response = requests.post(LOGIN_URL, data=payload_data)
            
            self.assertEqual(response.status_code, 401)
            print(f"Payload '{payload[:15]}...': Status {response.status_code} (PASS)")

    @patch('requests.post')
    def test_sqli_vulnerability_simulation(self, mock_post):
        """
        Test Case 2: Simulation of a VULNERABLE response.
        MOCK: Return a Successful Login response (HTTP 200/302).
        """
        # Set the mock to return a successful login (SIMULATING A FAIL/VULNERABILITY)
        mock_post.return_value = self._mock_response(
            status=200, 
            text="Welcome, Administrator!"
        )
        
        print("\n--- Testing SQLi Vulnerability (Expected Fail Simulation) ---")
        
        # Test just the first critical payload for brevity
        payload = SQLI_PAYLOADS[0]
        payload_data = {'username': payload, 'password': 'any_pass'}

        response = requests.post(LOGIN_URL, data=payload_data)
        
        # In a real test, if status is 200, a critical vulnerability is confirmed.
        if response.status_code == 200 and "Welcome" in response.text:
            print(f"CRITICAL VULNERABILITY SIMULATED: Payload '{payload}' resulted in success.")
            self.fail("SQL Injection vulnerability confirmed in simulation.")
        # else:
        #    self.assertTrue(False) # Force fail for reporting clarity

if __name__ == '__main__':
    # You would typically run this using 'python -m unittest sqli_test.py'
    unittest.main(argv=['first-arg-is-ignored'], exit=False)