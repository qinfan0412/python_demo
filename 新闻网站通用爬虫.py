from gne import GeneralNewsExtractor
import requests


def get_response_text(base_url, headers=None):
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
    response = requests.get(base_url, headers=headers)
    response.encoding = 'utf-8'
    return response.text


def get_data_dict(news_url):
    extractor = GeneralNewsExtractor()
    html = get_response_text(news_url)
    result = extractor.extract(html)
    return result


if __name__ == '__main__':
    url = 'https://zhuanlan.zhihu.com/p/21645566'
    data = get_data_dict(url)
    print(data)
