import os
import csv
import requests
from bs4 import BeautifulSoup
from queue import Queue
from gevent import monkey
import pprint
import jieba



HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

START_URL = (
    "http://search.51job.com/list/010000%252C020000%252C030200%252C040000"
    ",000000,0000,00,9,99,Python,2,{}.html? lang=c&stype=1&postchannel=00"
    "00&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lon"
    "lat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&"
    "address=&line=&specialarea=00&from=&welfare="
)

get_urls = []
company = []


def job_spider():
    """
    爬虫入口
    """
    urls = [START_URL.format(p) for p in range(2,3)]

    for url in urls:
        html = requests.get(url,headers = HEADERS).content.decode("gbk")
        bs = BeautifulSoup(html, "lxml").find("div", class_= "dw_table").find_all(
            "div", class_= "el"
        )


        for b in bs:
            try:
                href, post = b.find("a")["href"], b.find("a")["title"]
                locate = b.find("span", class_="t3").text
                salary = b.find("span", class_="t4").text
                item = {
                    "href": href, "post": post, "locate": locate, "salary": salary
                }
                get_urls.append(href)
                company.append(item)
            except Exception:
                pass

def job_details():
    for url in get_urls:
        r = requests.get(url,headers=HEADERS)
        html = r.content.decode("gbk")
        try:
            bs = BeautifulSoup(html, "lxml").find(
               "div",class_= "bmsg job_msg inbox"
            ).text
            s = bs.replace("微信", "").replace("分享", "").replace("邮件", "").replace(
                "\t", ""
            ).strip()
            with open("post_require.txt",'a', encoding="utf-8") as f:
                f.write(s)
                f.close()

        except Exception:
            continue

def post_desc_counter():
    """
    职位描述统计
    """
    post = open('post_require.txt', 'r', encoding="utf-8").read()
    file_path = "user_dict.txt"
    jieba.load_userdict(file_path)
    seg_list = jieba.cut(post, cut_all=False)
    counter = dict()
    for seg in seg_list:
        counter[seg] = counter.get(seg, 1) + 1
    counter_sort = sorted(counter.items(), key=lambda value: value[1], reverse=True)
    #pprint(counter_sort)
    print(counter_sort)
    with open(
        "post_pre_desc_counter.csv", "w+", encoding="utf-8"
    ) as f:
        f_csv = csv.writer(f)
        f_csv.writerows(counter_sort)



#job_spider()
#job_details()
post_desc_counter()
