import requests
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# 禁用 SSL 验证
requests.packages.urllib3.disable_warnings()  # 禁用 SSL 警告
VERIFY_SSL = False  # 设置为 False 以禁用 SSL 验证

# 替换为你的 GitHub 个人访问令牌
GITHUB_TOKEN = ''
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

def search_github_repos(query, max_results=100):
    """搜索 GitHub 上与 Presto 相关的仓库"""
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': query,
        'sort': 'stars',
        'order': 'desc',
        'per_page': min(max_results, 100),  # GitHub API 每页最多返回 100 个结果
    }
    response = requests.get(url, headers=HEADERS, params=params, verify=VERIFY_SSL)
    response.raise_for_status()
    return response.json()['items']

def get_repo_languages(repo_url):
    """获取仓库的编程语言统计"""
    response = requests.get(repo_url, headers=HEADERS, verify=VERIFY_SSL)
    response.raise_for_status()
    return response.json()

def save_to_csv(data, filename='language_stats.csv'):
    """将统计结果保存为 CSV 文件"""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Language', 'Bytes of Code'])
        for language, bytes_of_code in data.items():
            writer.writerow([language, bytes_of_code])
    print(f"Data saved to {filename}")

def plot_language_stats(language_stats):
    """绘制柱状图"""
    languages = list(language_stats.keys())
    bytes_of_code = list(language_stats.values())

    plt.figure(figsize=(10, 6))
    plt.bar(languages, bytes_of_code, color='skyblue')
    plt.xlabel('Programming Language')
    plt.ylabel('Bytes of Code')
    plt.title('Language Statistics in Presto Projects')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    query = 'presto'
    repos = search_github_repos(query, max_results=100)
    
    language_stats = defaultdict(int)
    
    for repo in repos:
        repo_name = repo['full_name']
        languages_url = repo['languages_url']
        languages = get_repo_languages(languages_url)
        
        for language, bytes_of_code in languages.items():
            language_stats[language] += bytes_of_code
        
        print(f"Processed {repo_name}")
    
    # 打印统计结果
    print("\nLanguage Statistics:")
    for language, bytes_of_code in sorted(language_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{language}: {bytes_of_code} bytes")
    
    # 保存为 CSV 文件
    save_to_csv(language_stats)
    
    # 绘制柱状图
    plot_language_stats(language_stats)

if __name__ == '__main__':
    main()