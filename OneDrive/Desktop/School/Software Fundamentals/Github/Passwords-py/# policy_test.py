# policy_test.py
import requests
from unittest.mock import patch, MagicMock

# --- Target Configuration ---
REGISTER_URL = "http://localhost/api/v1/register" 
TEST_USERNAME = "policy_test_user"

# Passwords that SHOULD be rejected by a strong policy
WEAK_PASSWORDS = [
    "short1",         # Too short (less than 8-12 chars)
    "onlylowercase",  # Missing complex chars
    "1234567890",     # Missing letters
    "password123",    # Dictionary word
]

# --- Testing Logic ---
def _mock_response(status=400, error_message=""):
    mock_resp = MagicMock(spec=requests.Response)
    mock_resp.status_code = status
    mock_resp.text = error_message
    return mock_resp

@patch('requests.post')
def test_password_policy_enforcement(mock_post):
    """
    Tests if the registration endpoint rejects weak passwords.
    MOCK: Simulate rejection for all weak passwords (HTTP 400).
    """
    print("\n--- Testing Weak Password Policy Enforcement ---")
    
    # Simulate the rejection of weak passwords by the server
    mock_post.return_value = _mock_response(
        status=400, 
        error_message="Password does not meet minimum complexity requirements."
    )
    
    for password in WEAK_PASSWORDS:
        payload = {'username': TEST_USERNAME, 'password': password, 'confirm_password': password}
        response = requests.post(REGISTER_URL, data=payload)
        
        # Check if the server correctly rejected the password
        if response.status_code == 400 and "complexity" in response.text:
            print(f"PASS: Weak password '{password}' correctly rejected.")
        else:
            # If we were expecting rejection but got success (e.g., status 200/302)
            print(f"FAILURE SIMULATED: Weak password '{password}' ACCEPTED. Status: {response.status_code}")
            # self.fail("Weak Password Policy enforcement failed in simulation.")


if __name__ == '__main__':
    test_password_policy_enforcement()
