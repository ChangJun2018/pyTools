from spider_jd import splider as jd
from spider_tb import spider as tb
from spider_yihaodian import spilder as yhd
from spider_dangdang import splider as ddw


def main(sn):
    """图书比价工具"""
    book_list = []
    # 当当网的数据
    print('当当网的数据爬去完成')
    ddw(sn, book_list)
    # 京东网的数据
    print('京东网的数据爬去完成')
    jd(sn, book_list)
    # 一号店的数据
    print('一号店的数据爬去完成')
    yhd(sn, book_list)
    # 淘宝网的数据
    print('淘宝网的数据爬去完成')
    tb(sn, book_list)

    # 打印所有数据列表
    for book in book_list:
        print(book)
    print('-------------------开始排序-------------')

    # 排序书的书籍
    book_list = sorted(book_list, key=lambda item: item["price"], reverse=True)
    for book in book_list:
        print(book)


if __name__ == '__main__':
    sn = input('请输入ISBN:')
    main(sn)
