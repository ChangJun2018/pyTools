import requests
from lxml import html


def spider(sn,book_list=[]):
    """爬去淘宝网的数据"""
    url = 'https://s.taobao.com/api?ajax=true&m=customized&sourceId=tb.index&q={0}'.format(sn)
    # 获取json对象
    res = requests.get(url).json()
    # 解析json数据
    bk_list = res["API.CustomizedApi"]["itemlist"]["auctions"]
    # 获取图书列表
    for bk in bk_list:
        title = bk['raw_title'] # 标题
        price = bk['view_price'] # 价格
        link = bk['detail_url'] # 链接
        store = bk['nick'] # 商家
        print('{title}: {price}: {link}: {store}'.format(
            title=title,
            price=price,
            link=link,
            store=store
        ))

        book_list.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': store[0]
        })




if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)