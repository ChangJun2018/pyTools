def format_str():
    """格式化字符串"""
    name = 'ChangJun'
    print('Hello,%s' % name)
    num = 52.18
    # 保留整数
    print('您输入的数字是:%.f' % num)
    # 保留四位小数
    print('您输入的数字是:%.4f' % num)
    num2 = 54
    # 54
    print('您的编号是:%d' % num2)
    # 0054
    print('您的编号是:%04d' % num2)
    t = (1, 2, 3, 5)
    print('您输入的元组是:%s' % str(t))

    print('您的姓名是:%(name)s' % {'name': name})


def format_str_2():
    """使用format格式化字符串"""
    # 使用位置
    print('欢迎您,{0},{1}---{0}'.format('ChangJun', 'Hello'))
    d = {
        'name': 'ChangJun',
        'num': 12
    }
    # 使用名称
    print('您好,{username}'.format(username='ChangJun'))
    print('您好,{name}'.format(**d))
    # 格式化元组
    point = (1, 6)
    print('坐标位置:{0[0]}:{0[1]}'.format(point))
    user = User('ChangJun', '21')
    print(user)

class User(object):

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def show(self):
        return '用户名:{self.username},年龄:{self.age}'.format(self=self)

    def __str__(self):
        return self.show()


if __name__ == '__main__':
    format_str_2()
