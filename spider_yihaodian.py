import requests
from lxml import html

def spilder(sn,book_list=[]):
    url = 'https://search.yhd.com/c0-0/k{0}/'.format(sn)
    # 获取到html源码
    html_doc = requests.get(url).text

    # xpath对象
    selector = html.fromstring(html_doc)

    # 书籍列表
    ul_list = selector.xpath('//div[@id="itemSearchList"]/div')

    # 解析数据
    for li in ul_list:
        # 标题
        title = li.xpath('div/p[@class="proName clearfix"]/a/@title')
        print(title)
        # 价格
        price = li.xpath('div/p[@class="proPrice"]/em/@yhdprice')
        print(price[0])
        # 商家
        store = li.xpath('div/p[@class="storeName limit_width"]/a/text()')
        print(store[0].replace('\n', ''))
        # 购买链接
        link = li.xpath('div/p[@class="proName clearfix"]/a/@href')
        print(link)

        book_list.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': store[0]
        })

if __name__ == '__main__':
    sn = "9787115428028"
    spilder(sn)
