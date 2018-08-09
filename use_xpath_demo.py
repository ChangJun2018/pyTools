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
    ul = selector.xpath('/html/body/ul/li')
    ul = selector.xpath('/html/body/ul/li')
    for li in ul:
        print(li.xpath('text()')[0])



    f.close()


if __name__ == "__main__":
    parse()
