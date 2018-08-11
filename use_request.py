import requests


def get_book():
    """获取信息"""

    url = 'http://search.dangdang.com/'
    res = requests.get(url, params={
        'key': 'python',
        'act': 'input'
    })
    # print(res.text)
    # 获取状态码
    print(res.status_code)


if __name__ == '__main__':
    get_book()
