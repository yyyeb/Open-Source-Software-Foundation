import requests
import pandas as pd
from datetime import datetime
import time
from lxml import etree
import matplotlib.pyplot as plt
# GitHub API URL for Presto issues
owner = 'prestodb'
repo = 'presto'
#token =   # 请换成GitHub您自己的个人Token

headers = {
    'Authorization': f'token {token}'  # 使用token进行身份验证
}
all_issues = []
for i in range(1, 68):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?q=is%3Aissue+is%3Aopen&page={i}"
    print(f"正在从 GitHub API 获取 {owner}/{repo} 的 issues 数据...")
    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        issues = response.json()
        all_issues.append(issues)
        print(f"成功获取 issues 数据！\n本次获得 {len(issues)} 条 issues 记录。")
        time.sleep(2)
        #return issues
    except requests.RequestException as e:
        print(f"获取 issues 数据失败：{e}")
        time.sleep(2)


# 提取每个issue的创建时间
issue_dates = []
for issues in all_issues:
    for issue in issues:
        #print(issues)
        created_at = issue.get('created_at')
        if created_at:
            issue_dates.append(created_at)

# 将时间字符串转换为日期格式
dates = pd.to_datetime(issue_dates)
#print(type(dates))
# 提取年份并统计每年issue的数量
years = dates.year
issue_count_per_year = years.value_counts().sort_index()

# 输出统计结果
print(issue_count_per_year)
# 绘制折线图
plt.figure(figsize=(10,6))
plt.plot(issue_count_per_year.index, issue_count_per_year.values, marker='o')
plt.title('Number of Issues Created per Year in Presto GitHub Repository')
plt.xlabel('Year')
plt.ylabel('Number of Issues')
plt.grid(True)
plt.xticks(issue_count_per_year.index, rotation=45)
plt.tight_layout()

# 显示图表
plt.show()