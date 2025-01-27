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
        first_reply_time = None
        response_time = None

        processed_data.append({
            "issue_number": issue.get("number"),
            "created_at": created_at,
            "first_reply_time": first_reply_time,
            "response_time_hours": response_time
        })

    return processed_data

def save_issues_to_csv(issues_data, filename):
    try:
        df = pd.DataFrame(issues_data)
        df.to_csv(filename, index=False, encoding='utf-8')
    except Exception as e:
        print ( f"保存 CSV 文件时出错: { e } " )

defanalyze_issues_data  （问题数据）：
    问题日期 = [问题。get ( 'created_at' )  for issues in issues_data if issues.获取（'创建于' ）]
    日期 = pd. to_datetime (问题日期)
    每个月的问题计数 = 日期。dt。月。value_counts ( )。排序索引( )
    打印（每月问题计数）

    # 势差折线图
    plt。图( Figsize= ( 10 , 6 ) )
    每个月的问题数。绘图（种类= '线'，标记= 'o' ）
    plt。xlabel ( '月份' )
    plt。xticks （ issue_count_per_month.index ，旋转= 47 ）
    plt。ylabel ( '问题数量' )
    plt。title ( 'Presto GitHub 存储库中每月创建的问题数' )
    plt。网格（true ）

    plt。tigh_layout （）

    ＃显示图表
    plt。展示（）

def  main （）：
    repo_owner = “ prestodb”
    repo_name = “ presto”

    ＃获取问题数据
    问题= fetch_github_issues （ repo_owner，repo_name ）

    如果问题：
        essess_data = process_issues_data （问题）
        如果essess_data：
            save_issues_to_csv（ essess_data，“ presto_issues.csv” ）
            Analyze_issues_data（ essess_data ）
        别的：
            打印（“未处理到有效的发行数据” ）
    别的：
        打印（“未能获取到发行数据，请检查配置或重试。” ）
        打印（“如果问题仍然存在，可能是网络问题或链接不正确。请检查网页链接的合法性，并适当重试。” ）

如果__name__ == “ __ -main __”：
    主要的（）
