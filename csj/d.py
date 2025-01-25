import requests
import pandas as pd
from datetime import datetime
import time
import matplotlib.pyplot as plt

# GitHub API URL for Presto discussions
owner = 'prestodb'
repo = 'presto'
token = ''  # 这里用引号将token括起来

headers = {
    'Authorization': f'token {token}'  # 使用token进行身份验证
}

all_discussions = []

# GitHub Discussions API URL
for i in range(1, 68):
    url = f"https://api.github.com/repos/{owner}/{repo}/discussions?per_page=100&page={i}"
    print(f"正在从 GitHub API 获取 {owner}/{repo} 的 discussions 数据...")
    try:
        # 在这里添加 verify=False 参数
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        discussions = response.json()
        all_discussions.append(discussions)
        print(f"成功获取 discussions 数据！\n本次获得 {len(discussions)} 条 discussions 记录。")
        time.sleep(2)
    except requests.RequestException as e:
        print(f"获取 discussions 数据失败：{e}")
        time.sleep(2)

# 提取每个discussion的创建时间
discussion_dates = []
for discussions in all_discussions:
    for discussion in discussions:
        created_at = discussion.get('created_at')
        if created_at:
            discussion_dates.append(created_at)

# 将时间字符串转换为日期格式
dates = pd.to_datetime(discussion_dates)

# 提取年份并统计每年讨论的数量
years = dates.year
discussion_count_per_year = years.value_counts().sort_index()

# 输出统计结果
print(discussion_count_per_year)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(discussion_count_per_year.index, discussion_count_per_year.values, marker='o')
plt.title('Number of Discussions Created per Year in Presto GitHub Repository')
plt.xlabel('Year')
plt.ylabel('Number of Discussions')
plt.grid(True)
plt.xticks(discussion_count_per_year.index, rotation=45)
plt.tight_layout()

# 显示图表
plt.show()
