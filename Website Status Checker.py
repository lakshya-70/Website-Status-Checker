#61th github project --> Website Status Checker
print('----------Website Status Checker----------')
import requests


def check_site(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5)
        return url, response.status_code, None
    except requests.exceptions.Timeout:
        return url, None, "Timeout"
    except requests.exceptions.ConnectionError:
        return url, None, "Connection error"
    except requests.exceptions.RequestException as e:
        return url, None, str(e)


def main():
    print("WEBSITE STATUS CHECKER")

    raw = input("URLs (comma-separated): ").strip()
    urls = [u.strip() for u in raw.split(",") if u.strip()]

    if not urls:
        print("No URLs given.")
        return

    for url in urls:
        final_url, status, error = check_site(url)
        if error:
            print(f"{final_url:<40} ERROR: {error}")
        else:
            label = "OK" if 200 <= status < 400 else "FAIL"
            print(f"{final_url:<40} {status} ({label})")


if __name__ == "__main__":
    main()