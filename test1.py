import jieba
from pprint import pprint
import csv
post = open("post_require.txt", "r", encoding="utf-8").read()
file_path = "user_dict.txt"
jieba.load_userdict(file_path)
seg_list = jieba.cut(post, HMM=False)
counter = dict()
for seg in seg_list:
    counter[seg] = counter.get(seg, 1) + 1
counter_sort = sorted(counter.items(), key=lambda value: value[1], reverse= True)
pprint(counter_sort)
with open("post_counter.csv", "w+", encoding="utf-8") as f:
    f_csv = csv.writer(f)
    f_csv.writerows(counter_sort)
