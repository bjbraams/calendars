import requests
from urllib.parse import urljoin

def get_url_status_code(url: str, timeout: int = 10) -> int:
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code
    except requests.exceptions.RequestException:
        return 0

def get_url_status(url: str, timeout: int = 10) -> dict:
    """
    Fetches the HTTP status and redirect information for a given URL.
    Args:
        url (str): The URL to check.
        timeout (int): The maximum number of seconds to wait for a response.
    Returns:
        dict: A dictionary containing:
              - 'code': The HTTP status code (int).
              - 'type': A descriptive string (e.g., 'OK', 'Redirect', 'Client Error', 'Connection Error').
              - 'dest': The destination URL if it's a redirect, otherwise None.
    """
    result = {
        'code': 0,
        'type': 'Connection Error',
        'dest': None
    }

    try:
        # Perform the request without following redirects
        response = requests.head(url, timeout=timeout, allow_redirects=False)
        result['code'] = response.status_code
        if 200 <= response.status_code < 300:
            result['type'] = "OK"
        elif 300 <= response.status_code < 400:
            # It's a redirect!
            result['type'] = f"Redirect ({response.status_code})"
            # Get the destination from the 'Location' header
            destination_url = response.headers.get('Location')
            if destination_url:
                # Handling relative redirects
                result['dest'] = urljoin(url, destination_url)
            else:
                result['dest'] = "N/A (Location header missing)"
        elif 400 <= response.status_code < 500:
            result['type'] = "Client Error"
        elif 500 <= response.status_code < 600:
            result['type'] = "Server Error"
        else:
            result['type'] = "Other Status"
    except requests.exceptions.Timeout:
        result['type'] = "Timeout Error"
        result['code'] = 0
    except requests.exceptions.ConnectionError:
        result['type'] = "Connection Error"
        result['code'] = 0
    except requests.exceptions.RequestException as e:
        # Catch other requests-specific errors
        result['type'] = f"Request Error: {e}"
        result['code'] = 0
    except Exception as e:
        # Catch any other unexpected errors
        result['type'] = f"Unexpected Error: {e}"
        result['code'] = 0
    return result

# --- Example Usage ---
# if __name__ == "__main__":
#     urls_to_check = {
#         "Google (direct)": "https://www.google.com",
#         "Example.com (HTTP to HTTPS 301)": "http://example.com",
#         "Broken Link (404)": "https://www.google.com/nonexistentpage12345",
#         "Explicit 302 Redirect": "http://httpbin.org/status/302", # A service for testing HTTP responses
#         "Chained Redirect (302 -> 200)": "http://httpbin.org/redirect-to?url=http://httpbin.org/status/200", # This will return the initial 302
#         "Non-existent Domain": "http://this-domain-does-not-exist-123xyz.com",
#         "Server Error (500)": "http://httpbin.org/status/500"
#     }
# 
#     print("--- Checking URLs with Redirect Information ---")
#     print("Note: For chained redirects, this script reports only the *first* redirect.")
#     print("-------------------------------------------------")
# 
#     for name, url in urls_to_check.items():
#         print(f"\nChecking: {name}")
#         print(f"  URL: {url}")
#         info = get_url_status(url)
#         print(f"  Status: {info['code']} ({info['type']})")
#         if info['dest']:
#             print(f"  Destination: {info['dest']}")
#         else:
#             print(f"  Destination: N/A")
# 
#     print("\n-------------------------------------------------")
#     print("Check complete.")
