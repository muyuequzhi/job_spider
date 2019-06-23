# 前程无忧爬虫

## 今年夏天将会有很多机械专业的朋友毕业，我就爬取了前程无忧的相关职位信息进行分析，试图回答4个问题。

郑州与上海各800条，然后去除异地招聘、没有薪资的数据，数据保存为csv文件。 薪资单位为：k/月

1.通过工作经验与薪资的关系图， 来了解这个专业前景如何、是否适合长期投入

发现在两地无工作经验的比一年经验的薪资还高，猜测可能是培训机构在那里"挂羊头，卖狗肉"
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E4%B8%8A%E6%B5%B7/%E4%B8%8A%E6%B5%B7%E7%BB%8F%E9%AA%8C%E8%96%AA%E8%B5%84.png)
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E9%83%91%E5%B7%9E/%E9%83%91%E5%B7%9E%E7%BB%8F%E9%AA%8C%E8%96%AA%E8%B5%84%E5%9B%BE.png)
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E4%B8%8A%E6%B5%B7/%E4%B8%8A%E6%B5%B7%E8%96%AA%E8%B5%84%E5%89%8D%E5%87%A0%E5%90%8D.png)
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E9%83%91%E5%B7%9E/%E9%83%91%E5%B7%9E%E6%8E%92%E5%90%8D%E5%89%8D%E5%87%A0.png)

2.通过分析职位中不同学历的占比情况， 来决定是否要专升本、考研
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E4%B8%8A%E6%B5%B7/%E4%B8%8A%E6%B5%B7%E5%AD%A6%E5%8E%86%E5%8D%A0%E6%AF%94%E5%9B%BE.png)
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E9%83%91%E5%B7%9E/%E9%83%91%E5%B7%9E%E5%AD%A6%E5%8E%86%E5%8D%A0%E6%AF%94.png)

3.通过郑州与上海的对比图， 来决定将来是留在本地还是去上海

4.通过jieba、词云统计词频， 看哪些是企业招聘时看重的，来查漏补缺，找对方向提升自己。
上海地区的
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E4%B8%8A%E6%B5%B7/%E4%B8%8A%E6%B5%B7%E8%AF%8D%E4%BA%91.jpg)
郑州地区的
![image](https://github.com/muyuequzhi/job_spider/blob/master/%E9%83%91%E5%B7%9E/%E9%83%91%E5%B7%9E%E8%AF%8D%E4%BA%91.jpg)