import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Disable HTTPS insecure certificate warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"


def get_token(username: str, password: str) -> str:
    """Authenticate to DNA Center and return auth token."""
    url = f"{BASE_URL}/api/system/v1/auth/token"

    response = requests.post(
        url,
        auth=HTTPBasicAuth(username, password),
        headers={"Content-Type": "application/json"},
        verify=False,
    )
    response.raise_for_status()

    return response.json()["Token"]


def get_dna_data(token: str, endpoint: str) -> dict:
    """Retrieve data from a DNA Center API endpoint."""
    url = f"{BASE_URL}/api/v1/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
    }

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()

    return response.json()


def main():
    token = get_token(USERNAME, PASSWORD)
    devices = get_dna_data(token, "network-device")["response"]

    for device in devices:
        print(
            f"Device: {device.get('type')} "
            f"has an uptime of {device.get('upTime')}."
        )


if __name__ == "__main__":
    main()
