import datetime
import requests

URL = "https://rent.591.com.tw/home/search/rsList"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://rent.591.com.tw/",
}


def fetch_today_yilan_rentals():
    params = {
        "is_new_list": 1,
        "is_format_data": 1,
        "region": "宜蘭縣",
        "firstRow": 0,
    }
    resp = requests.get(URL, headers=HEADERS, params=params, timeout=10)
    resp.raise_for_status()
    try:
        data = resp.json()
    except ValueError:
        return []

    listings = data.get("data", {}).get("data", [])
    today = datetime.date.today().strftime("%Y-%m-%d")
    result = []
    for item in listings:
        if item.get("post_date") == today:
            result.append({
                "title": item.get("title"),
                "price": item.get("price"),
                "area": item.get("area"),
                "url": item.get("shareUrl") or item.get("detail_url"),
            })
    return result


if __name__ == "__main__":
    rentals = fetch_today_yilan_rentals()
    for house in rentals:
        print(f"{house['title']} - {house['price']} - {house['area']}")
        if house.get('url'):
            print(house['url'])

