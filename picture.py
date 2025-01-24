import requests
import os

class GitHubRepoSpider():
    def __init__(self, owner, repo, save_folder):
        self.headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3642.0 Mobile Safari/537.36"}
        self.owner = owner
        self.repo = repo
        self.api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
        self.save_folder = save_folder
        self.ind = 1

    def get_file_list(self):
        """ Get the list of files in the repository """
        try:
            response = requests.get(self.api_url, headers=self.headers)
            response.raise_for_status()  # Check for a successful response
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to get file list for {self.repo}: {e}")
            return []

    def download_file(self, file_url, file_path):
        """ Download file from the GitHub URL """
        try:
            file_data = requests.get(file_url, headers=self.headers)
            file_data.raise_for_status()  # Check if the request was successful
            with open(file_path, 'wb') as fp:
                fp.write(file_data.content)
            print(f"Downloaded and saved: {file_path}")
        except requests.RequestException as e:
            print(f"Failed to download {file_url}: {e}")

    def run(self):
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

        file_list = self.get_file_list()
        for file_info in file_list:
            if file_info['type'] == 'file':  # Only download files, not directories
                file_url = file_info['download_url']
                file_path = os.path.join(self.save_folder, f"file_{self.ind}.txt")  # Adjust filename as needed
                self.download_file(file_url, file_path)
                self.ind += 1

if __name__ == '__main__':
    # Specify the owner, repo and save folder dynamically
    spider = GitHubRepoSpider(owner='prestodb', repo='presto', save_folder=r'C:\Users\Ronystar\Desktop\presto_files')
    spider.run()
