import json
from collections import defaultdict
import matplotlib.pyplot as plt

# 1. 定义文件路径
file_path = r'C:\Users\scmb\Desktop\presto_prs.json'  # 使用原始字符串（raw string）避免转义问题

# 2. 读取 JSON 数据
with open(file_path, 'r', encoding='utf-8') as f:  # 确保使用 UTF-8 编码读取文件
    data = json.load(f)

# 3. 统计每个审阅者的审阅数量
reviewer_stats = defaultdict(int)

for pr in data:
    for reviewer in pr['requested_reviewers']:
        reviewer_stats[reviewer['login']] += 1

# 按审阅数量排序，并取前 50 名
sorted_reviewers = sorted(reviewer_stats.items(), key=lambda x: x[1], reverse=True)[:50]

# 4. 输出前 50 名审阅者的审阅数量
print("Top 50 Reviewers by Review Count:")
for reviewer, count in sorted_reviewers:
    print(f"{reviewer}: {count} reviews")

# 5. 可视化前 50 名审阅者的审阅数量
# 准备数据
reviewers = [reviewer for reviewer, count in sorted_reviewers]
review_counts = [count for reviewer, count in sorted_reviewers]

# 绘制柱状图
plt.figure(figsize=(12, 8))  # 调整图表大小以适应更多数据
plt.bar(reviewers, review_counts, color='lightgreen')
plt.xlabel('Reviewer')
plt.ylabel('Number of Reviews')
plt.title('Top 50 Reviewers by Review Count')
plt.xticks(rotation=90)  # 旋转 x 轴标签以便更好地显示
plt.tight_layout()  # 调整布局以避免标签被截断
plt.show()