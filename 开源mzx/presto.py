import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

# 设置 GitHub 个人访问令牌
TOKEN = "token"

def fetch_github_issues(repo_owner, repo_name):
    issues = []
    page = 1
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {"Authorization": f"token {TOKEN}"}

    while True:
        params = {"state": "all", "per_page": 100, "page": page}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            batch = response.json()
            if not batch:
                break
            issues.extend(batch)
            page += 1
        elif response.status_code == 403:
            time.sleep(2)
        else:
            print(f"请求失败，状态码：{response.status_code}, 响应：{response.text}")
            break

    return issues

def process_issues_data(issues):
    processed_data = []

    for issue in issues:
        if "pull_request" in issue:
            continue

        created_at = pd.to_datetime(issue.get("created_at"))
        comments = issue.get("comments", 0)
        first_reply_time = None
        response_time = None

        processed_data.append({
            "issue_number": issue.get("number"),
            "created_at": created_at,
            "is_replied": comments > 0,
            "first_reply_time": first_reply_time,
            "response_time_hours": response_time
        })

    return processed_data

def save_issues_to_csv(issues_data, filename):
    try:
        df = pd.DataFrame(issues_data)
        df.to_csv(filename, index=False, encoding='utf-8')
    except Exception as e:
        print(f"保存 CSV 文件时出错: {e}")

def analyze_issues_data(issues_data):
    # 提取每个issue的创建时间
    issue_dates = [issue.get('created_at') for issue in issues_data if issue.get('created_at')]

    # 将时间字符串转换为日期格式
    dates = pd.to_datetime(issue_dates)

    # 提取年份并统计每年issue的数量
    issue_count_per_year = dates.dt.year.value_counts().sort_index()

    # 输出统计结果
    print(issue_count_per_year)

    # 绘制折线图
    plt.figure(figsize=(10, 6))
    issue_count_per_year.plot(kind='line', marker='o')
    plt.title('Number of Issues Created per Year in Presto GitHub Repository')
    plt.xlabel('Year')
    plt.ylabel('Number of Issues')
    plt.grid(True)
    plt.xticks(issue_count_per_year.index, rotation=45)
    plt.tight_layout()

    # 显示图表
    plt.show()

def main():
    repo_owner = "prestodb"
    repo_name = "presto"

    # 获取 Issue 数据
    issues = fetch_github_issues(repo_owner, repo_name)

    if issues:
        issues_data = process_issues_data(issues)
        if issues_data:
            save_issues_to_csv(issues_data, "presto_issues.csv")
            analyze_issues_data(issues_data)
        else:
            print("未处理到有效的 Issue 数据")
    else:
        print("未能获取到 Issue 数据，请检查配置或重试。")
        print("如果问题仍然存在，可能是网络问题或链接不正确。请检查网页链接的合法性，并适当重试。")

if __name__ == "__main__":
    main()