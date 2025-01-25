import json
from collections import defaultdict
import matplotlib.pyplot as plt

# 1. 定义文件路径
file_path = r'C:\Users\scmb\Desktop\presto_prs.json'  # 使用原始字符串（raw string）避免转义问题

# 2. 读取 JSON 数据
with open(file_path, 'r', encoding='utf-8') as f:  # 确保使用 UTF-8 编码读取文件
    data = json.load(f)

# 3. 统计每个贡献者的 PR 数量
contributor_stats = defaultdict(int)

for pr in data:
    author = pr['user']['login']
    contributor_stats[author] += 1

# 按 PR 数量排序，并取前 50 名
sorted_contributors = sorted(contributor_stats.items(), key=lambda x: x[1], reverse=True)[:50]

# 4. 输出前 50 名贡献者的 PR 数量
print("Top 50 Contributors by PR Count:")
for author, count in sorted_contributors:
    print(f"{author}: {count} PRs")

# 5. 可视化前 50 名贡献者的 PR 数量
# 准备数据
contributors = [author for author, count in sorted_contributors]
pr_counts = [count for author, count in sorted_contributors]

# 绘制柱状图
plt.figure(figsize=(12, 8))  # 调整图表大小以适应更多数据
plt.bar(contributors, pr_counts, color='skyblue')
plt.xlabel('Contributor')
plt.ylabel('Number of PRs')
plt.title('Top 50 Contributors by PR Count')
plt.xticks(rotation=90)  # 旋转 x 轴标签以便更好地显示
plt.tight_layout()  # 调整布局以避免标签被截断
plt.show()