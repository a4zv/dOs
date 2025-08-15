import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Error: No URL provided.\nUsage: python script.py <user_agent_list_url>")
        sys.exit(1)

    target_url = sys.argv[1]

    try:
        response = requests.get(target_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch the page: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")

    ua_list_container = soup.find(id="liste")
    if not ua_list_container:
        print("No UA list found — check that the URL points to a valid UA list page.")
        sys.exit(1)

    ua_items = ua_list_container.find_all("li")
    if not ua_items:
        print("No user agents found on the page.")
        sys.exit(1)

    for item in ua_items:
        ua_text = item.get_text(strip=True)
        print(ua_text)

if __name__ == "__main__":
    main()

