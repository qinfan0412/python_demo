import math

# 第一步：使用Python的字典dict构造数据集
movie_data = {"宝贝当家": [45, 2, 9, "喜剧片"],
              "美人鱼": [21, 17, 5, "喜剧片"],
              "澳门风云3": [54, 9, 11, "喜剧片"],
              "功夫熊猫3": [39, 0, 31, "喜剧片"],
              "谍影重重": [5, 2, 57, "动作片"],
              "叶问3": [3, 2, 65, "动作片"],
              "伦敦陷落": [2, 3, 55, "动作片"],
              "我的特工爷爷": [6, 4, 21, "动作片"],
              "奔爱": [7, 46, 4, "爱情片"],
              "夜孔雀": [9, 39, 8, "爱情片"],
              "代理情人": [9, 38, 2, "爱情片"],
              "新步步惊心": [8, 34, 17, "爱情片"]}
# 第二步：计算一个新样本与数据集中所有数据的距离
x = [23, 3, 17]
KNN = []
for k, v in movie_data.items():
    distance = math.sqrt((v[0] - x[0]) ** 2 + (v[1] - x[1]) ** 2 + (v[2] - x[2]) ** 2)
    KNN.append([distance, v[3]])

# 第三步：排序后的KNN,并取出前五个
KNN = sorted(KNN, key=lambda x: x[0])[:5]
print(KNN)
# 第四步：取最多的电影类型
tp_list = [v[1] for v in KNN]  # 取出前五个的电影类型
print(tp_list)
set_tp = set(tp_list)  # 去重
max, tp = 0, 0
for i in set_tp:
    if max < tp_list.count(i):
        max = tp_list.count(i)
        tp = i
print('唐人街探案的电影类型为：', tp)

