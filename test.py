import os
import time
import csv
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import jieba
from collections import Counter
from wordcloud import WordCloud
from tqdm import tqdm


HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

START_URL = (
   "https://search.51job.com/list/170200,000000,0000,00,9,99,%25E6%259C%25BA%25E6%25A2%25B0"
   ",2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99"
   "&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType"
   "=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
)

get_urls = []
#lst = []
#def :
#    for i in tqdm(range(1000)):
#        time.sleep(0.001)


def job_spider():
    """
    获取职位详情的url链接
    """
    urls = [START_URL.format(p) for p in range(1,2)]
    print("正在获取链接")
    sum = 0

    for url in urls:
        html = requests.get(url, headers=HEADERS).content.decode("gbk")
        bs = BeautifulSoup(html, "lxml").find("div", class_="dw_table").find_all(
            "div", class_="el"
        )
        for b in bs:
            try:
                href, post = b.find("a")["href"], b.find("a")["title"]
#                locate = b.find("span", class_="t3").text
#                salary = b.find("span", class_="t4").text
#                item = {
#                    "href": href, "post": post, "locate": locate, "salary": salary
#                }
                get_urls.append(href)
#                company.append(item)
            except Exception:
                continue


def job_details():
    """
    获取职位详细信息，薪资待遇、任职要求等
    :return:
    """
    print("正在下载职位详细信息")
    for url in get_urls:
        r = requests.get(url, headers=HEADERS)
        html = r.text
        try:
            soup = BeautifulSoup(html,"lxml")
            post = soup.find("div",class_="cn").find("h1").text
            salary = soup.find("div",class_="cn").find("strong").text
            txt = soup.find(class_="msg ltype").text.strip()
            c_txt = txt.replace("|",",")
            t_txt = salary + "," + post +","  + c_txt
            d_txt = "".join(t_txt.split())
            e_txt = d_txt + "\n"
            with open("post_salary.csv","a",encoding="utf-8") as f:
                f.write(e_txt)
                f.close()
            bs = BeautifulSoup(html, "lxml").find(
                "div", class_="bmsg job_msg inbox"
            ).text
            s = bs.replace("微信", "").replace("分享", "").replace("邮件", "").replace(
                "\t", ""
            ).strip()
            with open("post_require.txt", 'a', encoding="utf-8") as f:
                f.write(s)
                f.close()
        except Exception:
            continue

def post_salary():
    """
    整理职位信息，取薪资、学历、经验、职位、地点
    """

    print("正在统一处理薪资单位")
    re_post = []
    with open("post_salary.csv", "r", encoding="utf-8") as f:
        f_csv = csv.reader(f)

        for row in f_csv:
            re_post.append((row[0], row[4], row[3],row[1],row[2]))
    with open("re_post_salary.csv","w",encoding="utf-8",newline="") as f:
        r_csv = csv.writer(f)
        r_csv.writerows(re_post)


def post_key():
    """
    统计职位要求中的关键字排名
    """

    print("正在提取关键字")


    txt = open("post_require.txt", "r", encoding="utf-8").read()
    seg_list = jieba.lcut(txt)
    counts = {}
    "关键字与排名之间存在对应关系，选择用字典"
    for seg in seg_list:
        if len(seg) == 1:
            continue
        else:
            counts[seg] = counts.get(seg, 1) + 1
    item_sort = sorted(counts.items(), key=lambda value: value[1], reverse=True)
    ##pprint(item_sort)
    with open("post_key.csv", "w", encoding="utf-8", newline="") as f:
        f_csv = csv.writer(f)
        f_csv.writerows(item_sort)


#def post_salary():
#    """
#    招聘职位、地点、薪资
#    """
#    print("职位、地点、薪资信息将保存在post_salary.csv")
#
#    for c in company:
#        lst.append((c.get("salary"), c.get("post"), c.get("locate")))
#    # pprint(lst)
#    with open("post_salary.csv", "w+", encoding="utf-8", newline="") as f:
#        f_csv = csv.writer(f)
#        f_csv.writerows(lst)



#            if "万/月" in row[0]:
#                mouth.append((row[0], row[4], row[3],row[1],row[2]))
#            elif "万/年" in row[0]:
#                year.append((row[0], row[4], row[3],row[1],row[2]))
#            elif "千/月" in row[0]:
#                thousand.append((row[0], row[4], row[3],row[1],row[2]))


    # pprint(mouth)

#def post_salary_counter():
#    """
#    薪酬统计
#    """
#    with open("post_salary.csv", "r", encoding="utf-8") as f:
#        f_csv = csv.reader(f)
#        lst = [row[0] for row in f_csv]
#    counter = Counter(lst).most_common()
#    # pprint(counter)
#    with open(
#            os.path.join("post_salary_counter1.csv"), "w+", encoding="utf-8", newline=""
#    ) as f:
#        f_csv = csv.writer(f)
#        f_csv.writerows(counter)
#    print("薪资统计、计数成功")


def word_cloud():
    """
    生成词云
    """
    print("词云图片将保存在wc.jpg")


    counter = {}
    with open("post_key.csv", "r", encoding="utf-8") as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            counter[row[0]] = counter.get(row[0], int(row[1]))
        # pprint(counter)
    wc = WordCloud(
        font_path="msyh.ttf", max_words=15, height=600, width=1200
    ).generate_from_frequencies(
        counter
    )
    #    plt.imshow(wc)
    #    plt.axis("off")
    #    plt.show()
    wc.to_file("wc.jpg")


job_spider()
job_details()
post_key()
post_salary()
#post_salary_counter()
word_cloud()
