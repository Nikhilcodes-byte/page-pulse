import requests
import time
from bs4 import BeautifulSoup


def analyze_page(url):

    try:

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        start = time.time()

        response = requests.get(
            url,
            timeout=(5,5),
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/138.0 Safari/537.36"
                )
            }
        )

        end = time.time()

        content_type = response.headers.get("Content-Type", "")

        if not content_type.startswith("text/html"):
            return {
                "status": response.status_code,
                "response_time": f"{round((end-start)*1000)} ms",
                "title": "Not an HTML page",
                "description": "The URL points to a file instead of a webpage.",
                "h1_count": 0,
                "missing_alt": 0,
                "word_count": 0
            }

        soup = BeautifulSoup(response.text, "html.parser")

        return {
            "status": response.status_code,
            "response_time": f"{round((end-start)*1000)} ms",
            "title": soup.title.string.strip() if soup.title else "No Title",
            "description": (
                soup.find("meta", attrs={"name": "description"}).get("content").strip()
                if soup.find("meta", attrs={"name": "description"})
                and soup.find("meta", attrs={"name": "description"}).get("content")
                else "No Meta Description"
            ),
            "h1_count": len(soup.find_all("h1")),
            "missing_alt": len([
                img for img in soup.find_all("img")
                if not img.get("alt")
            ]),
            "word_count": len(soup.get_text(separator=" ", strip=True).split())
        }

    except requests.exceptions.Timeout:
        return {
            "status": "Timeout",
            "response_time": "--",
            "title": "Error",
            "description": "The request timed out.",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "Error",
            "response_time": "--",
            "title": "Error",
            "description": str(e),
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0
        }