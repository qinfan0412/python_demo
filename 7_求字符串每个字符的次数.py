str1 = 'asfhiuafjbiuvsjbauidhuivbaiuhsvofjwqfzmnvchaiuhudvnqiuvhsnfwiuhvnaljfie'

str_count_dict = dict()
for i in str1:
    if i in str_count_dict:
        str_count_dict[i] += 1
    else:
        str_count_dict[i] = 1
print(str_count_dict)

# 按出现次数，逆序排放
sort_count = sorted(str_count_dict, key=lambda x: str_count_dict[x], reverse=True)
print(sort_count)

# 输出出现次数最多的
max_count = max(str_count_dict, key=lambda x: str_count_dict[x])
print(max_count)
