import requests
import json

# GitHub 仓库信息
owner = "prestodb"  # 仓库所有者
repo = "presto"     # 仓库名称
url = f"https://api.github.com/repos/{owner}/{repo}/pulls"  # API URL

headers = {
    "A*u*t*h*o*r*i*zation": "**********",
    "Accept": "************"
}

# 获取所有 PR 数据
all_prs = []
page = 1
per_page = 100  # 每页最多 100 条数据

while True:
    params = {
        "state": "all",  # 获取所有 PR（open、closed、merged）
        "per_page": per_page,
        "page": page
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break
    
    prs = response.json()
    if not prs:
        break  # 没有更多数据
    
    all_prs.extend(prs)
    print(f"Fetched page {page} with {len(prs)} PRs")
    page += 1

# 保存数据到 JSON 文件
with open("presto_prs.json", "w") as f:
    json.dump(all_prs, f, indent=4)

print(f"Total PRs fetched: {len(all_prs)}")