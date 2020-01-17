import requests
from lxml import etree
from gne import GeneralNewsExtractor


# requests获取源码返回element对象
def get_element(url, choice=0):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'cookie': '_zap=ba6ec095-36bd-432d-a416-ca6ba1982d99; _xsrf=3338e98d-7aca-49fa-baed-ed677860f8e7; d_c0="ABClj6IdhxCPTtG_zLX0Dx-3qVxGyqJOX0s=|1576725372"; l_n_c=1; n_c=1; l_cap_id="ZTgyYThmNjk5MDZiNGU4MjkxMDFkZDE4Yzg1OTcwZTc=|1578463939|e5f5b0f19ce9258f2465da4567d0c03fab68fc82"; r_cap_id="ZTQ1ODZmMGFkYTk4NGI5MDllYzdhOGYxZTQ3OGUxYWM=|1578463939|0296375198a920cdac0c1010ce651ef493ecb4ad"; cap_id="ZWQ4NDgwYzJlOTA5NDVlNTk1MzI0ZjUwZGIyMzU0Mzc=|1578463939|861d6395d7f8231d47b98b73ffae6283c6aeb33f"; client_id="MTAwNTQ0QzNCOTYyQURENTI2NzdFQzYwNDAwQzdGMzA=|1578463944|8aaf3d26504c9088081a49625e88a7681aa46056"; capsion_ticket="2|1:0|10:1578463945|14:capsion_ticket|44:ZGJmODUxY2M4NjBiNDAzOWE4NDRiZTVjYjBhYTZjMDQ=|4f0bfcc37d9eba14b125e1a06365ba812670ee5e38500578f4e43319895f23c8"; z_c0="2|1:0|10:1578463997|4:z_c0|92:Mi4xYXIwREdBQUFBQUFBRUtXUG9oMkhFQ1lBQUFCZ0FsVk5fY0FDWHdCcHU5ckVzSmhJdTQ0emxjRk5LczF6MWZFRkZ3|1ade18fb8b2bb57bc06d5f3d41f4f0c3f20b108a9e6348f767cb1d3d36ae20fc"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1578463938,1578619902,1578620187,1578897548; q_c1=bc5ed0545f3f4050a85c15347ef1b10c|1578898149000|1578898149000; __utma=51854390.579455293.1578898151.1578898151.1578898151.1; __utmb=51854390.0.10.1578898151; __utmc=51854390; __utmz=51854390.1578898151.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20200108=1^3=entry_date=20200108=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1578898207; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1578898441|1578897546',
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if choice == 0:
        html = etree.HTML(response.text)
        return html
    else:
        return response.text


# 获取开始优秀回答者的url
def get_start_doctor_url():
    html = get_element('https://www.zhihu.com/topic/19604128/top-writer')
    url_list = html.xpath('//h2[@class="zm-list-content-title"]/a/@href')
    url_list = ['https://www.zhihu.com' + i + '/posts' for i in url_list]
    return url_list


# 判断作者个人信息是否有关键字
def has_doctor_background(html):
    Experience = html.xpath('string(//div[@class="ProfileHeader-content"])')
    key_words = ['医', '药', '病', '疗', '神经', '诊', '治', '康', '瘤']
    for i in key_words:
        if i in Experience:
            return True
    return False


# 获取文章的url
def get_article_url_list(html):
    # 判断文章有几页
    page_list = html.xpath('//button[@class="Button PaginationButton Button--plain"]/text()')
    if page_list:
        max_page = int(page_list[-1])
    else:
        max_page = 1
    href_list = []
    for page in range(1, max_page + 1):
        url = 'https://www.zhihu.com/people/tian-ji-shun/posts?page={}'.format(page)
        html = get_element(url)
        href_list = html.xpath('//h2[@class="ContentItem-title"]/a/@href')
        href_list = ['https:' + i for i in href_list]
        print(href_list)
        # for article_url in href_list:
        #     article = get_article(article_url)
        #     print(article)


# 获取文章的内容
def get_article(article_url):
    html = get_element(article_url, 1)
    extractor = GeneralNewsExtractor()
    result = extractor.extract(html)
    return result


# 主函数
def main():
    # 获取开始优秀回答者的url
    start_doctor_url = get_start_doctor_url()
    for url in start_doctor_url:
        html = get_element(url)
        # 首先判断该回答者个人信息是否含有关键字
        if has_doctor_background(html):
            # 获取文章
            article = get_article_url_list(html)


if __name__ == '__main__':
    main()
