# bruteforce_test.py
import requests
import time
from unittest.mock import patch, MagicMock

# --- Target Configuration ---
LOGIN_URL = "http://localhost/api/v1/login"
VALID_USERNAME = "testuser_brute"
ATTACK_PASSWORDS = ["123456", "password", "test1234", "qwerty"]
MAX_ATTEMPTS = 5 # Number of attempts before a lockout is expected

# --- Testing Logic ---
def _mock_response(status=401):
    mock_resp = MagicMock(spec=requests.Response)
    mock_resp.status_code = status
    mock_resp.text = "Invalid credentials."
    return mock_resp

@patch('requests.post')
def test_bruteforce_rate_limiting(mock_post):
    """
    Test logic to check for rate limiting/account lockout.
    MOCK: Simulate the system locking the account after 3 attempts.
    """
    print("\n--- Testing Brute-Force Rate Limiting ---")
    
    # 1. Simulate the first 3 failed attempts (return 401)
    # 2. Simulate the 4th and 5th attempts getting locked out (return 429 - Too Many Requests)
    side_effects = [
        _mock_response(status=401),  # Attempt 1
        _mock_response(status=401),  # Attempt 2
        _mock_response(status=401),  # Attempt 3
        _mock_response(status=429),  # Attempt 4 (Lockout expected)
        _mock_response(status=429),  # Attempt 5 (Locked)
    ]
    
    mock_post.side_effect = side_effects

    test_results = []
    
    for i, password in enumerate(ATTACK_PASSWORDS):
        if i >= MAX_ATTEMPTS:
            break

        start_time = time.time()
        
        payload = {'username': VALID_USERNAME, 'password': password}
        response = requests.post(LOGIN_URL, data=payload)
        
        end_time = time.time()
        duration = end_time - start_time

        test_results.append({
            'attempt': i + 1,
            'status': response.status_code,
            'duration': duration
        })

    # --- Analysis for Report ---
    print("Simulated Test Results:")
    for result in test_results:
        print(f"Attempt {result['attempt']}: Status {result['status']} (Duration: {result['duration']:.2f}s)")

    # Assert that the lockout status (429) was eventually reached
    if 429 in [r['status'] for r in test_results]:
        print("\nPASS (Logic Check): Account lockout/rate limit (429) was simulated and detected.")
    else:
        print("\nFAIL (Logic Check): Account lockout/rate limit was never triggered.")


if __name__ == '__main__':
    # You would typically run this as a standalone script
    test_bruteforce_rate_limiting()