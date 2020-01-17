# -----------------------------------url编码的加密和解码----------------------------
# 1.url编码的加密——--处理为：%CD%F5%B4%F3%B4%B8
def set_url(password):
    from urllib.parse import quote, unquote
    utf8_name = quote(password)  # utf-8
    return utf8_name


print('url编码加密后为：', set_url('我是蔡徐坤'))  # %E6%88%91%E6%98%AF%E8%94%A1%E5%BE%90%E5%9D%A4


# 2.url编码的解码(将的中文乱码符转换为中文),处理形如：%E6%8E%92%EF%E7%AE%97%E6%B3%95
def format_chinese(str1):
    from urllib.parse import unquote
    return unquote(str1, encoding="utf-8")


print('url编码解码后为：', format_chinese('%E6%8E%92%EF%E7%AE%97%E6%B3%95'))  # 排序算法


# --------------------------------------md5加密，不可逆向----------------------------
def set_d5(password):
    import hashlib
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


print('md5算法加密后为 ：', set_d5('123456'))  # e10adc3949ba59abbe56e057f20f883e


# ----------------------------------------base64加密和解码----------------------------
# 1.base64编码加密
def set_base64(password):
    import base64
    # 编码： 字符串 -> 二进制 -> base64编码
    b64 = base64.b64encode(password.encode())
    return b64


print('base64编码后：', set_base64('123123'))  # b'MTIzMTIz'


# 2.base64编码解码
def relieve_base64(password):
    import base64
    # 解码：base64编码 -> 二进制 -> 字符串
    return base64.b64decode(password).decode()


print('base64解码后：', relieve_base64(b'MTIzMTIz'))  # 123123


# ---------------------------------unicode编码----------------------------
# 1.加密
def set_unicode(name, ecd):
    if ecd == 'unicode_escape':
        return name.encode("unicode_escape")
    elif ecd == "utf-8":
        return name.encode("utf-8")
    elif ecd == "gbk":
        return name.encode("gbk")
    elif ecd == "gb2312":
        return name.encode("gb2312")


# 2.解码

def relieve_unicode(name, ecd):
    if ecd == 'unicode_escape':
        return name.decode("unicode_escape")
    elif ecd == "utf-8":
        return name.decode("utf-8")  # 不填默认utf-8
    elif ecd == "gbk":
        return name.decode("gbk")
    elif ecd == "gb2312":
        return name.decode("gb2312")
