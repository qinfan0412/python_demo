import re
import random
import datetime
from datetime import datetime
from datetime import timezone
from datetime import timedelta


# -----------------------------------------------------------正则匹配年-月-日
def format_date(date_list):
    try:
        date_re = re.compile('\d{4}-\d{2}-\d{2}')
        for i in date_list:
            i = date_re.findall(i)
            if i:
                return i[0]
    except:
        print('未匹配到')


# -------------------------------------------------------------随机获取格式:    时:分:秒
def get_random_time():
    H = str(random.randint(0, 24))
    M = str(random.randint(0, 60))
    S = str(random.randint(0, 60))
    random_time = [H, M, S]
    for i in range(0, len(random_time)):
        if len(random_time[i]) == 1:
            random_time[i] = '0' + random_time[i]
    time_ = ':'.join(random_time)
    return time_


# -----------------------------------------------处理此类形式：2019-11-20T10:06:09+08:00
# 1.匹配时间2019-11-20T10:06:09+08:00
def verify_datetime(datetime_):
    pattern = r'((?!0000)[0-9]{4}-((0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-8])|(0[13-9]|1[0-2])-(29|30)|(0[13578]|' \
              r'1[02])-31)|([0-9]{2}(0[48]|[2468][048]|[13579][26])|(0[48]|[2468][048]|[13579][26])00)-02-29) ' \
              r'(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$'
    if re.match(pattern, datetime_):
        return True


# 2.处理匹配到的时间
def format_date_tz(raw_date):
    date = raw_date.replace('T', ' ').replace('Z', '').split('+')[0]
    if not verify_datetime(date):
        raise ValueError(raw_date, date)
    return date


# ---------------------------------------------获取Tue, 06 Nov 2018 23:00:00 CDT,先处理为正常时间形式，再处理CDT时间为utc时间
def format_cdt_to_utc(date):
    date = ' '.join(date.split(' ')[1:5])
    format_time = datetime.datetime.strptime(date, '%d %b %Y %H:%M:%S')
    utc_time = format_time.astimezone(timezone(timedelta(hours=+14))).strftime("%Y-%m-%d %H:%M:%S")
    return utc_time


# ---------------------------------------处理几天前，几月前，几年前，几小时前
def format_date_ago(date):
    time_type = re.findall('\w前', date)[0].strip('前')
    if time_type == '月':
        # '12个月前 (01-19)'   处理为：当前日期-月份+随机生成的时分秒
        # 获取字符几个月前
        month_ago = int(re.findall('(.*?)个', date)[0])
        # 获取写文章的年份
        now_month = int(datetime.datetime.now().month)
        now_year = int(datetime.datetime.now().year)
        if now_month - month_ago < 0:
            year = now_year - 1
        else:
            year = int(datetime.datetime.now().year)
        # 获取准确月-日
        get_month_year = re.findall('前 \((.*?)\)', date)[0]
        finally_time = str(year) + '-' + get_month_year + ' ' + get_random_time()
        return finally_time

    elif time_type == '时':
        # 3小时前      处理为：当前时间-小时数
        hour_ago = int(re.findall('(.*?)小时前', date)[0])
        finally_time = str(datetime.datetime.now() - datetime.timedelta(hours=hour_ago)).split('.')[0]
        return finally_time

    elif time_type == '年':
        # 1年前 (2019-01-08)  处理为：获取的年月日+随机生成时分秒
        year_ago = re.findall('年前 \((.*?)\)', date)[0]
        finally_time = year_ago + ' ' + get_random_time()
        return finally_time

    elif time_type == '天':
        # 2天前    处理为：当前时间-天数
        day = int(re.findall('(.*?)天', date)[0])
        dayAgo = (datetime.datetime.now() - datetime.timedelta(days=day))
        # 转换为其他字符串格式
        finally_time = dayAgo.strftime("%Y-%m-%d %H:%M:%S")
        return finally_time
