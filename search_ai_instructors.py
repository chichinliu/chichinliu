import requests
import argparse


def search(query, limit=5):
    params = {
        "q": query,
        "format": "json",
        "no_html": "1",
        "skip_disambig": "1"
    }
    resp = requests.get("https://api.duckduckgo.com/", params=params)
    resp.raise_for_status()
    data = resp.json()

    results = []
    for item in data.get('RelatedTopics', []):
        if 'FirstURL' in item and 'Text' in item:
            results.append({'url': item['FirstURL'], 'text': item['Text']})
        elif 'Topics' in item:
            for sub in item['Topics']:
                if 'FirstURL' in sub and 'Text' in sub:
                    results.append({'url': sub['FirstURL'], 'text': sub['Text']})
        if len(results) >= limit:
            break
    return results[:limit]


def main():
    parser = argparse.ArgumentParser(description="Search for qualified AI course instructors")
    parser.add_argument('keywords', nargs='*', default=["AI", "\u8ab2\u7a0b", "\u5408\u683c", "\u5e2b\u8cc7"],
                        help='Search keywords (default: AI \u8ab2\u7a0b \u5408\u683c \u5e2b\u8cc7)')
    parser.add_argument('-n', '--num', type=int, default=5, help='Number of results to return')
    args = parser.parse_args()
    query = ' '.join(args.keywords)
    results = search(query, args.num)
    print(f"Top {len(results)} results for: {query}")
    for i, res in enumerate(results, 1):
        print(f"{i}. {res['text']}\n   {res['url']}")


if __name__ == '__main__':
    main()
