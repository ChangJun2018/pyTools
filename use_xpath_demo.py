from lxml import html


def parse():
    """将html中的内容,使用xpath提取出来"""
    f = open('./static/index.html', 'r', encoding='utf-8')
    s = f.read()

    # 获取h3标题下的内容
    selector = html.fromstring(s)
    h3 = selector.xpath('/html/body/h3/text()')
    print(h3[0])

    # 获取ul下面的li的内容
    # ul = selector.xpath('/html/body/ul/li')
    ul = selector.xpath('//ul/li')
    for li in ul:
        print(li.xpath('text()')[0])

    # 获取ul下面指定class li的内容
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(ul2[0])

    # 获取指定id下面的a标签
    res = selector.xpath('//div[@id="container"]/a')
    print(res[0].xpath('text()')[0])
    print(res[0].xpath('@href')[0])

    # 获取最后一个p内的文字
    res2 = selector.xpath('//body/p[last()]/text()')
    print(res2[0])

    res3 = selector.xpath('//*[@id="container"]/p[6]/text()')
    print(res3[0])

    f.close()


if __name__ == "__main__":
    parse()
