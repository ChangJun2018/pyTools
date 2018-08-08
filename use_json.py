import json


def python_to_json():
    """将python对象转化成json"""
    d = {
        'name': '人生苦短,我用python',
        'price': 62.8,
        "is_valid": True
    }
    rest = json.dumps(d, indent=4)
    print(rest)


def json_to_python():
    """将json对象转化成python"""
    e = '''{
        "name": "Python书籍",
        "origin_price": 66,
        "pub_date": "2018-4-14 17:00:00",
        "store": ["京东", "淘宝"],
        "author": ["张三", "李四", "Jhone"],
        "is_valid": true,
        "is_sale": false,
        "meta": {
            "isbn": "abc-123",
            "pages": 300
        },
        "desc": null
    }'''
    rest = json.loads(e)
    print(rest)


def json_to_python_from_file():
    """从文件读取内容,并转化成python对象"""
    f = open('./static/book.json', 'r', encoding='utf-8')
    s = f.read()
    rest = json.loads(s)
    print(rest['name'])


if __name__ == "__main__":
    # python_to_json()
    # json_to_python()
    json_to_python_from_file()
